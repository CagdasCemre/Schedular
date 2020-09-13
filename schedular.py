#Çağdaş Cemre Yurtsuz

from dataParser import dateParser
import time
from digraph import Digraph
import sys
from math import isnan


def schedular(recommendations, startDate, endDate)

    sys.setrecursionlimit(3000) #Increase recursion limit for dfs

    total_time = time.time()


    '''
    PUT network_objects
    in all_rec
    nCount = len(all_rec)
    '''





    start_time = time.time()
    print('Creating corequisite udgraph..')

    coGraph = Digraph(nCount) #Instantiate corequisite graph
    marked = [False for i in range(nCount)]
    for i in range(nCount):

        if not marked[i]:
            if not isnan(all_rec[i].groupID):
            
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
    clusterCost = [0 for _ in range(len(clusterList))] #Calculate each cluster's average cost

    for clust in clusterList:
        total = 0

        for job in clust:
            total += all_rec[job].dayVol
        
        clusterCost.append(total / len(clust))
    print("---Done in %s seconds! ---" % (time.time() - start_time))

    start_time = time.time()
    print('Creating directed graph for prereq..')

    graph = Digraph(len(clusterList)) #Instantiate prerequisites between clusters with given constraints. 
    preqCounter = [0 for _ in range(len(clusterList))]

    optional = list()
    for i in range(nCount):

        
        for j in range(i+1, nCount):
            
            if all_rec[i].site == all_rec[j].site:

                if all_rec[i].priority < all_rec[j].priority:
                    
                    graph.add_edge(clusterIndex[j], clusterIndex[i])
                    preqCounter[clusterIndex[j]] += 1
                    
     

                elif all_rec[i].priority == all_rec[j].priority:

                    if clusterCost[clusterIndex[i]] > clusterCost[clusterIndex[j]] :
                        
                        graph.add_edge(clusterIndex[j], clusterIndex[i])
                        preqCounter[clusterIndex[j]] += 1
                    

                        
                    elif clusterCost[clusterIndex[i]]  < clusterCost[clusterIndex[j]] :
                        
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


    startDate = dateParser(startDate)
    endDate = dateParser(endDate)


    weekLim = (endDate[0] - startDate[0]) * 52 + (endDate[1] - startDate[1] + 1)

    weeks = [[] for _ in range(weekLim)] #Actual plan of, has the indexes of each action in each week
    weekIndex = [0 for _ in range(len(clusterList))] #Opposite of weeks list.

    maxjPerWeek = max([len(cluster) for cluster in clusterList]) #Maximum job amount per week
    avgJPerWeek = int(nCount / weekLim) #Average job per week


    weeksLeft = weekLim #Represents the weeks left at the moment dynamically while scheduling
    totalClusters = len(clusterList)

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

                weekIndex[i] = weekNo
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


    start_time = time.time()
    print('Writing to excel..')
    i = 1
    for week in weekly_plan:

        for job in week:
            all_rec[job].updRolloutDate = f'{startDate[0]}-{i}'

        if i % 52 == 0:
            startDate[0] += 1
            i = 0

        i += 1
    print("---Done in %s seconds ---" % (time.time() - start_time))  

    print("---Total %s seconds! ---" % (time.time() - total_time))


