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

def add_edge_undirected_weighted_graph(v1,v2, cost):
    if v1 not in graph:
        print(v1,' is not present in the graph')
    elif v2 not in graph:
        print(v2,' is not present in graph')
    else:
        list1 = [v1,cost]
        list2 = [v2,cost]
        graph[v1].append(list2)
        graph[v2].append(list1)

def add_edge_directed_weighted_graph(v1,v2, cost):
    if v1 not in graph:
        print(v1,' is not present in the graph')
    elif v2 not in graph:
        print(v2,' is not present in graph')
    else:
        list1 = [v1,cost]
        graph[v2].append(list1)

def add_edge_directed_unweighted_graph(v1,v2):
    if v1 not in graph:
        print(v1,' is not present in the graph')
    elif v2 not in graph:
        print(v2,' is not present in graph')
    else:
        graph[v2].append(v1)

def delete_node_except_weighted_graph(v):
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

def delete_node_for_weighted_graph(v):
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break

def delete_edge_for_undirected_unweighted_graph(v1,v2):
    if v1 not in graph:
        print(v1,' is not present in the graph')
    elif v2 not in graph:
        print(v1,' is not present in the graph')
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

def delete_edge_for_directed_unweighted_graph(v1,v2):
    if v1 not in graph:
        print(v1,' is not present in the graph')
    elif v2 not in graph:
        print(v1,' is not present in the graph')
    else:
        if v1 in graph[v2]:
            graph[v2].remove(v1)

def delete_edge_for_undirected_weighted_graph(v1,v2,cost):
    if v1 not in graph:
        print(v1,' is not present in the graph')
    elif v2 not in graph:
        print(v1,' is not present in the graph')
    else:
        temp1 = [v1,cost]
        temp2 = [v2,cost]
        if temp2 in graph[v1]:
            graph[v1].remove(temp2)
            graph[v2].remove(temp1)

def delete_edge_for_directed_weighted_graph(v1,v2,cost):
    if v1 not in graph:
        print(v1,' is not present in the graph')
    elif v2 not in graph:
        print(v1,' is not present in the graph')
    else:
        temp = [v2,cost]
        if temp in graph[v1]:
            graph[v1].remove(temp)

graph = {}
add_node('A')
add_node('B')
add_node('E')
add_node('D')
# add_edge_undirected_unweighted_graph('A','B')
# add_edge_undirected_unweighted_graph('A','E')
# add_edge_undirected_weighted_graph('D','E',11)
# add_edge_directed_weighted_graph('A','B',3)
# add_edge_directed_unweighted_graph('A','B')
# delete_node_except_weighted_graph('A')
# delete_node_for_weighted_graph('E')
# delete_edge_for_undirected_unweighted_graph('A','B')
# delete_edge_for_directed_unweighted_graph('A','B')
# delete_edge_for_undirected_weighted_graph('D','E',11)
# delete_edge_for_directed_weighted_graph('B','A',3)
print(graph)