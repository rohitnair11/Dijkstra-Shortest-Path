# Dijkstra's Shortest Path First algorithm with priority queue implementation using heap
class Dijkstra:        

    # Priority Queue
    Q = []

    # Find index of left child of a node in the priority queue
    def left(self,i):
        return (2*i +1)
    
    # Find index of right child of a node in the priority queue
    def right(self,i):
        return (2*(i+1))

    # Find index of parent of a node in the priority queue
    def parent(self,i):
        return ((i-1)//2)

    # Decrease the key of a node in the priority queue
    def decrease_key(self,vertex, newWeight):
        index = -1
        for i in range(len(self.Q)):
            if self.Q[i].v == vertex:
                index = i
                break
        self.Q[index].w = newWeight
        while(index > 0 and self.Q[self.parent(index)].w > self.Q[index].w):
            self.Q[self.parent(index)], self.Q[index] = self.Q[index], self.Q[self.parent(index)]
            index = self.parent(index)

    # Builds a priority queue/ min-heap
    def build_min_heap(self,n):
        for i in range((len(self.Q)/2)-1,-1,-1):
            self.min_heapify(i,n)

    # Places a node in its appropriate position in the priority queue
    def min_heapify(self,i,n):
        l = self.left(i)
        r = self.right(i)
        if(l<n and self.Q[l].w<self.Q[i].w):
            smallest = l
        else:
            smallest = i
        if(r<n and self.Q[r].w<self.Q[smallest].w):
            smallest = r
        if smallest != i:
            temp = self.Q[i]
            self.Q[i] = self.Q[smallest]
            self.Q[smallest] = temp
            self.min_heapify(smallest,n)
    
    # Returns and removes the minimum element from the priority queue
    def extract_min(self):
        minim = self.Q[0].v
        self.Q[0] = self.Q[len(self.Q)-1]
        self.Q = self.Q[:-1]
        self.min_heapify(0, len(self.Q))
        return minim

    # Updates the distance between nodes if shorter path is found
    def relax(self, u, v, w, d, p ,usp):
        if ((d[u] + w)<d[v]):
            d[v] = d[u] + w
            p[v] = u
            usp[v] = usp[u]
            self.decrease_key(v, d[v])
        elif ((d[u] + w) == d[v]):
            usp[v]=0

    # Dijkstra's algorithm
    # See test case file for detailed information on inputs
    def Dijkstra_alg(self, n, e, mat, s):

        d = {}  # Stores shortest distance
        p = {}  # Stores the parent of a node
        usp = {}  # Stores the number of unique shortest paths
        self.Q = []

        # Initialize
        for i in range(1, n+1):
            d[i] = float("inf")
            p[i] = None
            usp[i] = 1

        # Set distance of source vertex to 0
        d[s] = 0

        # Insert all the vertices in the queue
        for i in range(1, n+1):
            self.Q.append(Node(i, d[i]))

        # Build a min heap/ priority-queue
        self.build_min_heap(len(self.Q))
        
        while len(self.Q)>0:
            u = self.extract_min()
            for i in range(e):
                if mat[i][0] == u:
                    self.relax(mat[i][0], mat[i][1], mat[i][2], d, p, usp)
                elif mat[i][1] == u:
                    self.relax(mat[i][1], mat[i][0], mat[i][2], d, p, usp)
        ans = []
        i=1
        for key,val in usp.items():
            ans.append([d[i],val])
            i=i+1
        return ans


class Node:
    v, w = 0, 0

    def __init__(self, a, b):
        self.v = a
        self.w = b