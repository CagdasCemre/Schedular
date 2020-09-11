#Çağdaş Cemre Yurtsuz

class Digraph:

    '''
    This class implements a simple directed grpah using adjacecny List.
    Each vertex is represented as an index and it's adjacent vertices are
    added to the list in the source index (Kind of like a jagged array).
    '''

    def __init__(self, v):

        '''
        This constructer takes 1 parameter 'v' which is the total vertex count. 
        Instantiate the Edge count (e), Vertice count (v) and Adjacency list of each vertex.
        '''
        
        self.__v = v
        self.__e = 0
        self.__adj = list()

        for _ in range(v):
            self.__adj.append(list())

    def get_v(self):
        '''
        Get vertex count of Digraph object.
        '''
        return self.__v
    
    def get_e(self):
        '''
        Get edge count of Digraph object.
        '''
        return self.__e
    
    def get_adj(self):
        '''
        Get adjacency list of Digraph object
        '''
        return self.__adj

    def set_v(self, v):
        '''
        Set vertex count of Digraph object.
        '''
        self.__v = v
    
    def set_e(self, e):
        '''
        Set edge count of Digraph object.
        '''
        self.__e = e
    
    def add_edge(self, vfrom, vto):
        '''
        This method addes an edge from vfrom to vto via
        adding vto to adj[vfrom]
        '''
        self.__adj[vfrom].append(vto)
        self.__e += 1

    def reverse(self):
        '''
        This method return the reverse of the graph via
        reversing the adjacency list of Digraph object
        '''
        reverse = Digraph(self.__v)

        for i in range(len(self.__adj)):
            for vfrom in self.__adj[i]:
                reverse.add_edge(vfrom, i)

        return reverse


    
    def dfs(self, v, reversePostOrder, marked):
        '''
        This recursive method traverses the given adjacency list
        using Depth-Fisrt Search method and saves the indexes in an array
        in reverse post order.
        '''
        marked[v] = True;

        for w in self.__adj[v]:
            if not marked[w]:
                self.dfs(w, reversePostOrder, marked)
        reversePostOrder.append(v)    


    def topologicalSort(self):

        '''
        This method applies topological sort on the Digraph Object
        and returns the sorted indexes of vertices using depth-first search.
        '''

        reversePostOrder = list()
        marked = [False for _ in range(self.__v)]

        for v in range(self.__v):
            if not marked[v]:
                self.dfs(v, reversePostOrder, marked)
                
        return reversePostOrder
        
    def clusterFinder(self):

        '''
        This method uses depth-first search to find reachable indexes
        from a source index and puts them in an array along with the
        source vertex, hence each disconnected graph is grouped in a list.
        '''
        clusterList = list()
        clusterIndex = [0 for _ in range(self.__v)]
        
        marked = [False for _ in range(self.__v)]

        for v in range(self.__v):
            if not marked[v]:
                cluster = list()
                self.clusterDfs(v, cluster, marked, len(clusterList), clusterIndex)
                clusterList.append(cluster)
            

        return clusterList, clusterIndex

    def clusterDfs(self, v, cluster, marked, clusterNo, clusterIndex):

        '''
        This recursive algorithm implements depth-first search to find
        reachable vertices from vertex v.
        '''
        marked[v] = True;

        cluster.append(v)
        clusterIndex[v] = clusterNo
                    
        for w in self.__adj[v]:
            if not marked[w]:
                self.clusterDfs(w, cluster, marked, clusterNo, clusterIndex)
        



        
