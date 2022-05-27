def read_graph(file_name: str):
    graph_list = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                graph_list.append(list(map(int, line.split())))
        return graph_list
    except:
        return None

def dfs(graph_list: list, vertex: int):
    visited = [False] * len(graph_list)

    def step(vertex):
        visited[vertex] = True        
        for sub_vertex in graph_list[vertex]:
            if not visited[sub_vertex]:
                step(sub_vertex)
    step(vertex)
    return visited

def count_component(graph_list: list):
    vertex_component = [-1] * len(graph_list)
    visited = [False] * len(graph_list)
    number = 0
    while False in visited:
       visited_dfs = dfs(graph_list, visited.index(False))
       for ind in range(len(visited_dfs)):
           if visited_dfs[ind]:
               visited[ind] = True
               vertex_component[ind] = number
       number += 1
    return number, vertex_component

def is_connected(graph_list: list, first_vertex: int, second_vertex: int):
    component = count_component(graph_list)[1]
    if component[first_vertex] == component[second_vertex]:
        return True
    else:
        return False
g = read_graph('graph1.txt')
print(dfs(g, 0))
print(count_component(g)[0])
print(count_component(g)[1])
print(is_connected(g, 1, 3))
print(is_connected(g, 0, 6))

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] \
                                for row in range(V)]
 
    def isBipartite(self, src):
         colorArr = [-1] * self.V
        colorArr[src] = 1
        queue = []
        queue.append(src)
        while queue:
            u = queue.pop()
            if self.graph[u][u] == 1:
                return False;
 
            for v in range(self.V):
                if self.graph[u][v] == 1 and colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)
 
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
        return True 
g = Graph(4)
g.graph = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]]           
print "Yes" if g.isBipartite(0) else "No"
