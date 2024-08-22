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

def has_cycle_iterative(graph):
    visited = set()
    
    for start_node in graph:
        if start_node in visited:
            continue
        
        stack = [(start_node, None)]  # (node, parent)
        
        while stack:
            node, parent = stack.pop()
            
            if node in visited:
                return True
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return True
                stack.append((neighbor, node))
    
    return False

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
print(has_cycle_iterative(graph))