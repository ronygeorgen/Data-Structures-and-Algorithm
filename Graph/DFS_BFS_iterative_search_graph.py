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

def DFS_iterative(node,graph):
    visited = []
    visited_set = set()
    if node not in graph:
        print('Node is not present in the graph')
        return []
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited_set:
            visited.append(current)
            visited_set.add(current)
            for i in graph[current]:
                stack.append(i)
    return visited

def BFS_iterative(node, graph):
    visited = []
    visited_set = set()
    if node not in graph:
        print('Node is not present in the graph')
        return []
    
    queue = [node]
    visited_set.add(node)
    
    while queue:
        current = queue.pop(0)
        visited.append(current)
        
        for i in graph[current]:
            if i not in visited_set:
                queue.append(i)
                visited_set.add(i)
    
    return visited


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
print(graph)
result = DFS_iterative('A',graph)
print('DFS traversal:', result)
result_bfs = BFS_iterative('A', graph)
print('BFS traversal:', result_bfs)

