import random as rd
import networkx as nx
import matplotlib.pyplot as plt

MAX_NODES = 15
plot = 0

# Creates random graph
def random_graph(rand=True, num_nodes = 15, num_edges = 20):
    if rand:
        num_nodes = rd.randint(1,MAX_NODES)
        num_edges = rd.randint(MAX_NODES*2,MAX_NODES*3)
    return nx.gnm_random_graph(num_nodes,num_edges)

# Given two graphs, adds the second one as a new component to the first, resulting in a graph with two components.
def merge_graphs(G1,G2):
    s = len(G1.nodes())
    G1.add_nodes_from([s+n for n in G2.nodes])
    G1.add_edges_from([(s+edge[0],s+edge[1]) for edge in G2.edges()])
    return G1
	
def random_multiple_component_graph(rand=True,n=15,e=20,c=3):
	assert isinstance(c, int) and c > 0, 'El número de componentes conexas debe ser un entero positivo'
	g_ret = random_graph(rand,n,e)
	while c > 1:
		g_ret = merge_graphs(g_ret,random_graph(rand,n,e))
		c -= 1
	return g_ret

# Show Graph
def draw(G,size=7):
    global plot
    plt.figure(plot,(size,size))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,with_labels=True,pos=pos)
    plot += 1