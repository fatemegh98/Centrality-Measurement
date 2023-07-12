import networkx as nx
import csv
import random
import time
import Algorithms

if __name__ == '__main__':

    with open('./Data/Enron_Email/Email-Enron.txt') as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)
        for i in d:
            i[0] = int(i[0])
            i[1] = int(i[1])

    time_base = time.time()

    graph = nx.MultiGraph(d[0:25])

    node = graph.nodes[random.randint(0,len(graph.nodes))]
    print("Node ",node, ": ", Algorithms.count_all(graph, node))
    print("The process took ", (time.time()-time_base)/60, "minutes to complete")

