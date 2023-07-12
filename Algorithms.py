import networkx as nx

# def edge_contraction(links, u, v):
#     graph = nx.MultiGraph(links)
#     new_node =  max(graph.nodes) +1
#     graph.add_node(new_node)
#     neighbours = list(set(graph.neighbors(u)).union(set(graph.neighbors(v))))
#     neighbours.remove(u)
#     neighbours.remove(v)
#
#     number = []
#     for i in range(len(neighbours)):
#         k = graph.number_of_edges(u, neighbours[i])
#         l = graph.number_of_edges(v, neighbours[i])
#         number.append(k + l)
#
#     graph.remove_node(u)
#     graph.remove_node(v)
#
#     for i in neighbours:
#         for k in range(number[i]):
#             graph.add_edge(new_node, i)
#
#     new_node = u
#     return graph, new_node


# algorithm 1
def count_all(multigraph, vertex):
    neighbor_list = sorted(list(multigraph.neighbors(vertex)))
    if len(neighbor_list) == 0:
        return 1
    else:
        for u in neighbor_list:
            omega = multigraph.number_of_edges(vertex, u)
            # #########################################################
            graph = nx.contracted_edge(multigraph, (vertex, u), self_loops=False)
            contracted_node = vertex
            # #########################################################
            # graph, contracted_node = edge_contraction(multigraph.edges,vertex, u)

            for i in range(0,omega):
                multigraph.remove_edge(vertex, u, key=i)

            number_multiedge = pow(2,omega)-1

            return count_all(multigraph, vertex) + number_multiedge*count_all(graph, contracted_node)


# Algorithm 2: all_subgraph_on_trees
def count_trees(tree, vertex):
    neighbor_list = sorted(list(tree.neighbors(vertex)))
    if len(neighbor_list) == 0:
        return 1
    else:
        for u in neighbor_list:
            tree.remove_edge(vertex,u)
            return count_trees(tree, vertex)*(count_trees(tree, u)+1)

