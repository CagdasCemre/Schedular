#Çağdaş Cemre Yurtsuz

import time
from digraph import Digraph
import sys
from math import isnan


def schedular(recommendations, processInterval, costLim):

    sys.setrecursionlimit(3000) #Increase recursion limit for dfs

    total_time = time.time()
    all_rec = list()


    for recom in recommendations:
        if recom.status == 'Optional':
            all_rec.append(recom)

    nCount = len(all_rec)


    start_time = time.time()
    print('Creating corequisite udgraph..')

    coGraph = Digraph(nCount) #Instantiate corequisite graph
    marked = [False for i in range(nCount)]
    for i in range(nCount):

        if not marked[i]:
            if all_rec[i].groupID is not None:
            
                for j in range(i+1, nCount):
                    
                    if all_rec[j].groupID is not None:
                       if all_rec[i].region == all_rec[j].region and all_rec[i].groupID == all_rec[j].groupID:
                           marked[j] = True 
                           coGraph.add_edge(i, j)
                           coGraph.add_edge(j, i)
                    else:
                        marked[j] = True 
                 
    print("---Done in %s seconds! ---" % (time.time() - start_time))


    start_time = time.time()
    print('Calculating clusters in coGraph..')
    clusterList, clusterIndex = coGraph.clusterFinder() #Finds disconnected graphs inside corequisite graph, hence distinct clusters are found
    print("---Done in %s seconds! ---" % (time.time() - start_time))



    start_time = time.time()
    print('Calculating cluster avg. cost in coGraph..')
    clusterAvgCost = list() #Calculate each cluster's average cost
    clusterCost = list() #Calculate each cluster's total cost
    
    for clust in clusterList:
        total = 0

        for job in clust:
            if all_rec[job].dayVol is not None and not isnan(all_rec[job].dayVol):
                total += all_rec[job].dayVol
                
        clusterCost.append(total)
        clusterAvgCost.append(total / len(clust))
    
    print("---Done in %s seconds! ---" % (time.time() - start_time))

    start_time = time.time()
    print('Creating directed graph for prereq..')

    graph = Digraph(len(clusterList)) #Instantiate prerequisites between clusters with given constraints. 
    preqCounter = [0 for _ in range(len(clusterList))]

    
    for i in range(nCount):

        if all_rec[i].priority != -1:
            for j in range(i+1, nCount):

                if all_rec[j].priority != -1:
                    if all_rec[i].site == all_rec[j].site:

                        if all_rec[i].priority < all_rec[j].priority:
                            
                            graph.add_edge(clusterIndex[j], clusterIndex[i])
                            preqCounter[clusterIndex[j]] += 1
                            
             

                        elif all_rec[i].priority == all_rec[j].priority:

                            if clusterAvgCost[clusterIndex[i]] > clusterAvgCost[clusterIndex[j]] :
                                
                                graph.add_edge(clusterIndex[j], clusterIndex[i])
                                preqCounter[clusterIndex[j]] += 1
                            

                                
                            elif clusterAvgCost[clusterIndex[i]]  < clusterAvgCost[clusterIndex[j]] :
                                
                                graph.add_edge(clusterIndex[i], clusterIndex[j])
                                preqCounter[clusterIndex[i]] += 1
                            


                        else:
                            
                            graph.add_edge(clusterIndex[i], clusterIndex[j])
                            preqCounter[clusterIndex[i]] += 1
                        
                   
                    
    print("---Done in %s seconds ---" % (time.time() - start_time))


    start_time = time.time()
    print('Topological Sort on DiGraph..')
    order = graph.topologicalSort() #Calculate topological sort to decide action appliance order according to prerequisites
    print("---Done in %s seconds ---" % (time.time() - start_time))




    start_time = time.time()
    print('Scheduling..')
    '''
    This part schedules the recommandations according to the result of topological sort.
    Each cluster is put as a whole into the week.
    Maximum jobs that can be put into a week is limited with max job count in all of the clusters(For uniformity)
    Maximum cluster per week is calculated according to total equal distribution of total cluster count between weeks(For uniformity)
    '''


    temp_order = list()
    totalCost = 0
    for i in order:
        if totalCost + clusterCost[i] <= costLim:
            temp_order.append(i)
            totalCost += clusterCost[i]
        else:
            break
            
    order = temp_order
    
    weekLim = len(processInterval)

    weeks = [[] for _ in range(weekLim)] #Actual plan of, has the indexes of each action in each week


    cToProcess  = list()
    for i in order:
        cToProcess.append(clusterList[i])

    if len(cToProcess) > 0:
        jAmountToProcess = 0
        for cluster in cToProcess:
            jAmountToProcess += len(cluster)

        maxjPerWeek = max([len(cluster) for cluster in cToProcess]) #Maximum job amount per week
        avgJPerWeek = int(jAmountToProcess / weekLim) #Average job per week


        weeksLeft = weekLim #Represents the weeks left at the moment dynamically while scheduling
        totalClusters = len(cToProcess)

        reverseGraph = graph.reverse()

        weekNo = 0 
        for week in weeks:

            jLim = maxjPerWeek
            schJob = list()

            clusterPerWeek = int(totalClusters / weeksLeft)
            if clusterPerWeek == 0:
                clusterPerWeek = 1
            
            for i in order:
               
                
                if preqCounter[i] != -1 and preqCounter[i] == 0 :

                    if jLim <= 0 or clusterPerWeek <= 0 or jLim < len(clusterList[i]) :
                        break


                    week.extend(clusterList[i])
                    jLim -= len(clusterList[i])
                    preqCounter[i] = -1
                    schJob.append(i)
                    clusterPerWeek -= 1
                    totalClusters -= 1
                    
            for job in schJob:
                for req in reverseGraph.get_adj()[job]:
                    preqCounter[req] -= 1
                    
                    
            weekNo += 1            
            weeksLeft -= 1       

            
                
                        
            
            
        print("---Done in %s seconds ---" % (time.time() - start_time))            


        '''
        for week in weeks:
            print(len(week))
        '''

        start_time = time.time()
        print('Writing to network elements..')

        i = 0
        for week in weeks:
            for job in week:
                all_rec[job].updRolloutDate = processInterval[i] 
                    
            i += 1
    else:
        print('Insufficient funds!! No operation can be done')
        
    for recom in recommendations:
        if recom.status == 'Approved':
            all_rec.append(recom)

    print("---Done in %s seconds ---" % (time.time() - start_time))  

    print("---Total %s seconds! ---" % (time.time() - total_time))

    return all_rec

