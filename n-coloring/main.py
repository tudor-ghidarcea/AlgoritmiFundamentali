culori_folosite=[]

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def colorGraph(graph, n):
    result = {}

    for u in range(n):

        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])

        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1

        result[u] = color
    for v in range(n):
        culori_folosite.insert(v,colors[result[v]])
        print(f'Culoarea nodului {v} este {colors[result[v]]}')
    if len(set(culori_folosite))==2:
       print("graful este bipartit")
    else:
       print("graful nu este bipartit")


if __name__ == '__main__':
    colors = ['', 'Albastru', 'Rosu', 'Roz', 'Verde']
    f = open("bipartit.in", "r")
    lines = f.readlines()
    perechi=[]
    for line in lines:
        perechi.append(line[0]+","+line[2])
    perechi = list(map(eval, perechi))
    edges = perechi

    n = h=int(lines[0].split()[0])+1
    graph = Graph(edges, n)

    colorGraph(graph, n)
