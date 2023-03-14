import networkx as nx

with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read()
    df = [[int(x) for x in line] for line in data.splitlines()]
    w, h = len(df), len(df[0])
    G = nx.grid_2d_graph(w, h, create_using=nx.DiGraph())
    nx.set_edge_attributes(G, {e: df[e[1][0]][e[1][1]] for e in G.edges()}, 'cost')
    assert nx.shortest_path_length(G, source=(0, 0), target=(w - 1, h - 1), weight='cost') == 462
