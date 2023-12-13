import numpy
from numpy import Inf

# create our graph using an adjacency list representation
# each "node" in our list should be a node name and a distance
if __name__ == "__main__":
    # Adjacency list representation of the graph
    adjList = []
    f = open("adiacenta.in", "r")
    lines = f.readlines()
    n = int(lines[0].split()[0])
    m = int(lines[0].split()[1])

'''

for j in range(n+1):
    aux = []
    for line in lines[1:]:
        if line[0]==str(j):
            aux.append(int(line[2]))
    adjList.append(aux)
adjList=adjList[1:]
graf={}
for i in range(len(adjList)):
    graf[i]=list(tuple(adjList[i]))
'''
graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]}

def naive_dijkstras(graph, root):
    n = len(graph)
    # initialize distance list as all infinities
    dist = [Inf for _ in range(n)]
# set the distance for the root to be 0
    dist[root] = 0
# initialize list of visited nodes
    visited = [False for _ in range(n)]

# loop through all the nodes
    for _ in range(n):
        # "start" our node as -1 (so we don't have a start/next node yet)
        u = -1
        # loop through all the nodes to check for visitation status
        for i in range(n):
            # if the node 'i' hasn't been visited and
            # we haven't processed it or the distance we have for it is less
            # than the distance we have to the "start" node
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        # all the nodes have been visited or we can't reach this node
        if dist[u] == Inf:
            break
        # set the node as visited
        visited[u] = True
        # compare the distance to each node from the "start" node
        # to the distance we currently have on file for it
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l

    return dist
print(naive_dijkstras(graph,1))