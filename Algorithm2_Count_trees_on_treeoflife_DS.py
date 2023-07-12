import json
import networkx as nx
import time
import Algorithms


if __name__ == '__main__':
    # reading the dataset "Tree of Life"
    f = open('./Data/tree_of_life/treeoflife.json', )
    time_base = time.time()

    # returns JSON object as a dictionary
    data = json.load(f)

    directed = data["directed"]
    multigraph = data["multigraph"]
    nodes = data["nodes"]
    links = data["links"]

    f.close()


    tree_links = []
    for i in links:
        tree_links.append((i['source'], i['target']))

    tree = nx.DiGraph(tree_links)

    print("The built graph is a tree?", nx.is_tree(tree))

    nodes = sorted(list(tree.nodes))
    file = open("Algorithm2_tree_of_life_results.txt", 'w')
    for node in nodes:
        tree = nx.DiGraph(tree_links)
        file.write("\n" + str(str(node)+ "\t" + str(sorted(list(tree.neighbors(node))))))
        file.write("\n" + str("Node "+ str(node) +  " : "+ str(Algorithms.count_trees(tree, node))))

    file.close()

    print("The process took ", (time.time()-time_base)/60, "minutes to accomplish")