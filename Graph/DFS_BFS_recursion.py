def add_node(v):
    if v in graph:
        print(v, 'is already present in the graph')
    else:
        graph[v] = []

def add_edge_undirected_unweighted_graph(v1,v2):
    if v1 not in graph:
        print(v1,' is not present in the graph')
    elif v2 not in graph:
        print(v2,' is not present in graph')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFS(node,visited):
    if node not in graph:
        print('Node is not present in graph')
        return
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited)

def BFS(queue,visited):
    if not queue:
        return
    node = queue.pop(0)
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for i in graph[node]:
            if i not in visited:
                queue.append(i)
    BFS(queue,visited)
visited = set()
queue = ['A']
graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge_undirected_unweighted_graph('A','B')
add_edge_undirected_unweighted_graph('B','E')
add_edge_undirected_unweighted_graph('A','C')
add_edge_undirected_unweighted_graph('A','D')
add_edge_undirected_unweighted_graph('B','D')
add_edge_undirected_unweighted_graph('C','D')
add_edge_undirected_unweighted_graph('E','D')
# DFS('A',visited)
print()
BFS(queue,visited)