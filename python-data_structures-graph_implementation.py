# -*- coding: utf-8 -*-

import queue 
import sys 

class AdjacentVertex:
    """ Tuple with adjacent vertices and associated weight. Weight is 1 for 
    unweighted graphs. """

    def __init__(self, vertex, weight = None):
        self._vertex = vertex
        self._weight = weight
    
    def __str__(self):
        if self._weight:
            return '('+str(self._vertex)+','+str(self._weight)+')'
        else: # Unweighted graph.
            return str(self._vertex)

class Graph():
    def __init__(self, vertices, directed = True):

        # key = vertex of the graph
        # The value associated with the key is the list of neighboring 
        # vertex.

        self._vertices = {}
        for v in vertices:
            self._vertices[v] = []
            
        self._directed = directed
    
    def addEdge(self, start, end, weight = None):
        # start is the exit vertex and end is the arrival vertex.      
        
        if start not in self._vertices.keys():
            print(start,' does not exist')
            return
        if end not in self._vertices.keys():
            print(end,' does not exist')
            return
        
        # End is a neighbor of start.
        self._vertices[start].append(AdjacentVertex(end, weight))

        # If the graph is directed, start is a neighbor of end.
        if self._directed == False:
            self._vertices[end].append(AdjacentVertex(start, weight))

    def containsEdge(self, start, end):
        # Check if two nodes are neighbors. If they are not, returns 0.
        # If they are neighbors, returns the associated weight.
        
        if start not in self._vertices.keys():
            print(start,' does not exist')
            return 0
        if end not in self._vertices.keys():
            print(end,' does not exist')
            return 0

        for adj in self._vertices[start]:
            if adj._vertex == end:
                if adj._weight:
                    return adj._weight
                else:
                    return 1 # Unweighted graph.
        return 0  

    def removeEdge(self, start, end):
        # Remove the edge that connect start and end.
        
        if start not in self._vertices.keys():
            print(start,' no existe')
            return
        if end not in self._vertices.keys():
            print(end,' no existe')
            return

        for adj in self._vertices[start]:
            if adj._vertex == end:
                self._vertices[start].remove(adj)
        
        if self._directed == False:
            for adj in self._vertices[end]:
                if adj._vertex == start:
                    self._vertices[end].remove(adj)
                    
    def bfs(self):
        # breadth first traversal.

        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        for v in self._vertices.keys():
            if visited[v] == False:
                self._bfs(v, visited)

    def _bfs(self, v, visited): 
        # Auxiliar recursive function.
        
        q = queue.Queue()
        visited[v] = True
        q.put(v)
        
        while not q.empty(): 
            
            current = q.get()
            print (current, end = " ") 

            for adj in self._vertices[current]: 
                if visited[adj._vertex] == False:
                    q.put(adj._vertex)
                    visited[adj._vertex] = True

    def dfs(self): 
        # depth first traversal.
 
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        for v in self._vertices.keys():
            if visited[v] == False:
                self._dfs(v, visited)

    def _dfs(self, v, visited): 
        # Auxiliar recursive function.

        visited[v] = True
        print(v, end=' ')

        for adj in self._vertices[v]: 
          if visited[adj._vertex] == False: 
            self._dfs(adj._vertex, visited)
            
    def minDistance(self, distances, visited): 
        # Auxiliar function.
        
        # Inicializate the value of distances at "infinite".
        min = sys.maxsize 

        for vertex in self._vertices.keys(): 
            if distances[vertex] <= min and visited[vertex] == False: 
                min = distances[vertex] 
                min_vertex = vertex
    
        return min_vertex 

    def dijkstra(self, origin): 
        # Dijkstra algorithm.

        visited = {}

        for v in self._vertices.keys():
            visited[v] = False

        previous = {}
        for v in self._vertices.keys():
            previous[v] = None

        distances = {}
        # Inicializate the value of previous at "infinite".
        for v in self._vertices.keys():
            distances[v]=sys.maxsize

        distances[origin] = 0
        
        for n in range(len(self._vertices)): 

            u = self.minDistance(distances, visited) 
            visited[u] = True
            
            for adj in self._vertices[u]: 
                i=adj._vertex
                w=adj._weight
                if visited[i] == False and distances[i] > distances[u] + w:
                    distances[i] = distances[u] + w
                    previous[i] = u       

        self.printSolution(distances,previous,origin)
        
    def printSolution(self, distances, previous, origin): 
        print("Mininum path from ",origin)

        for i in self._vertices.keys():

            if distances[i]==sys.maxsize:
                print("There is not path from ",origin,' to ',i)
            else: 

                minimum_path=[]
                prev=previous[i]
                # This loop helps us to build the path.
                while prev!=None:
                    minimum_path.insert(0,prev)
                    prev=previous[prev]
                
                minimum_path.append(i) 
                 
                print(origin,'->',i,":", minimum_path,distances[i])
                
    def minimumPath(self,start,end): 
        # Returns a list containing the minimum path from start to end.
        
        distances,previous=self.dijkstra(start)
        minimum_path=[]
        if start==end:
            #print('start == end ')
            pass
        elif distances[end]==sys.maxsize:
            #print("There is not path from ",start,' to ',end)
            pass
        else: 
            prev=previous[end]
            while prev!=-1:
                minimum_path.insert(0,prev)
                prev=previous[prev]
                
            minimum_path.append(end)  

        return minimum_path
            
    def __str__(self):
            
        result=''
        for v in self._vertices:
            result+='\n'+str(v)+':'
            for adj in self._vertices[v]:
                result+=str(adj)+"  "
        return result

################################################## Tests

if __name__ == '__main__':

    labels=['A','B','C','D','E']
    g=Graph(labels,False)
    g.addEdge('A','B') # A:0, B:1
    g.addEdge('A','C') # A:0, C:2
    g.addEdge('A','E') # A:0, E:5
    g.addEdge('B','D') # B:1, D:4
    g.addEdge('B','E') # C:2, B:1
    #g.addEdge('A','H',8)

    print(g)

    labels=['A','B','C','D','E']

    g=Graph(labels)

    # Add edges
    g.addEdge('A','C',12) #A->(12)C
    g.addEdge('A','D',60) #A->(60)D
    g.addEdge('B','A',10) #B->(10)A
    g.addEdge('C','B',20) #C->(20)B
    g.addEdge('C','D',32) #C->(32)D
    g.addEdge('E','A',7)  #E->(7)A

    print(g)

    print(g.containsEdge('C','B'))

    print(g.containsEdge('B','C'))
    g.removeEdge('C','B')
    print(g)
    
################################################ Tests #2

if __name__ == '__main__':

    # BFS
    labels=['A','B','C','D','E']

    g = Graph(labels)

    g.addEdge('A','C',12) #A->(12)C
    g.addEdge('A','D',60) #A->(60)D
    g.addEdge('B','A',10) #B->(10)A
    g.addEdge('C','B',20) #C->(20)B
    g.addEdge('C','D',32) #C->(32)D
    g.addEdge('E','A',7)  #E->(7)A

    print(g)
    print()

    g.bfs()
    print()

    label='C'
    visited={}
    for v in labels:
        visited[v]=False

    print('BFS desde ', label)
    g._bfs(label,visited)
    print()

    label='E'
    visited={}
    for v in labels:
        visited[v]=False
    print('BFS desde ', label)
    g._bfs(label,visited)


    labels=['A','B','C','D','E']
    g=Graph(labels,False)
    g.addEdge('A','B') # A:0, B:1
    g.addEdge('A','C') # A:0, C:2
    g.addEdge('A','E') # A:0, E:5
    g.addEdge('B','D') # B:1, D:4
    g.addEdge('B','E') # C:2, B:1

    print(g)

    print('bfs traversal from A (A is the first vertex):')
    g.bfs()
    print()
    label='E'
    visited={}
    for v in labels:
        visited[v]=False
    print('bfs traversal from ', label)
    #we have to pass the index of the vertex 
    g._bfs(label,visited)

    # DFS

    labels=['A','B','C','D','E']

    g=Graph(labels)

    g.addEdge('A','C',12) #A->(12)C
    g.addEdge('A','D',60) #A->(60)D
    g.addEdge('B','A',10) #B->(10)A
    g.addEdge('C','B',20) #C->(20)B
    g.addEdge('C','D',32) #C->(32)D
    g.addEdge('E','A',7)  #E->(7)A

    print(g)
    print()

    g.dfs()
    print()

    visited={}
    for v in labels:
        visited[v]=False
    print('DFS desde B')
    g._dfs('B',visited)
    
############################################## Tests #3: Dijkstra

if __name__ == '__main__':

    labels=['A','B','C','D','E']

    g = Graph(labels)

    g.addEdge('A','C',12) #A->(12)C
    g.addEdge('A','D',60) #A->(60)D
    g.addEdge('B','A',10) #B->(10)A
    g.addEdge('C','B',20) #C->(20)B
    g.addEdge('C','D',32) #C->(32)D
    g.addEdge('E','A',7)  #E->(7)A

    print(g)

    g.dijkstra('A')

    labels=['a','b','c','d','e','f']

    g=Graph(labels,False)

    g.addEdge('a','b',7) 
    g.addEdge('a','c',9) 
    g.addEdge('a','f',14) 
    g.addEdge('b','c',10) 
    g.addEdge('b','d',15) 
    g.addEdge('c','d',11)  
    g.addEdge('c','f',2)
    g.addEdge('d','e',6)
    g.addEdge('e','f',9)

    print(g)

    g.dijkstra('a')
    g.dijkstra('f')
    g.dijkstra('b')