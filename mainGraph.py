#Çağdaş Cemre Yurtsuz

from dataParser import dataParser
import time
from digraph import Digraph
import sys
from math import isnan

print(sys.getrecursionlimit())
sys.setrecursionlimit(3000) #Increase recursion limit for dfs

total_time = time.time()


file = 'Recommendations.csv' #Source file for Recommendation
parser = dataParser(file)

start_time = time.time()
print('Parsing data..')
all_rec,  nCount = parser.parse(file) #Parse the data inside the csv file, return dictionary with same data and number of actions
print("---Done in %s seconds! ---" % (time.time() - start_time))





start_time = time.time()
print('Creating corequisite udgraph..')

coGraph = Digraph(nCount) #Instantiate corequisite graph
marked = [False for i in range(nCount)]
for i in range(nCount):

    if not marked[i]:

        for j in range(i+1, nCount):
            
            if not (isnan(all_rec[i].groupID) and isnan(all_rec[j].groupID)):
               if all_rec[i].region == all_rec[j].region and isnan(all_rec[i].groupID == isnan(all_rec[j].groupID:
                   marked[j] = True 
                   coGraph.add_edge(i, j)
                   coGraph.add_edge(j, i)
             
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
        
        if all_rec['SITE'][i] == all_rec['SITE'][j]:

            if all_rec['PRIORITY'][i] < all_rec['PRIORITY'][j]:
                
                graph.add_edge(clusterIndex[j], clusterIndex[i])
                preqCounter[clusterIndex[j]] += 1
                
 

            elif all_rec['PRIORITY'][i] == all_rec['PRIORITY'][j]:

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
weekLim = 52

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
       

        if preqCounter[i] != -1 and preqCounter[i] == 0:

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
parser.write(weeks, clusterIndex, weekIndex, nCount) #Write back to excel file
print("---Done in %s seconds ---" % (time.time() - start_time))  

for week in weeks:
    print(len(week))

print("---Total %s seconds! ---" % (time.time() - total_time))

input('Press any key')
