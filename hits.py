import networkx as nx

if __name__=='__main__':
    # Example extracted from 'Introduction to Information Retrieval'
    G = nx.DiGraph()
    G.add_nodes_from([1, 2, 3])
    G.add_edges_from([(1,2),(1,3),(2,3),(3,2)])
    # print G.edges()

    print nx.hits(G, max_iter=5)
