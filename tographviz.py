import networkx as nx
# import pydot as plt

bt = nx.MultiDiGraph()
bt.add_node('x0')
bt.add_node('ID')
bt.add_node('NEG')
# bt.add_link('x0','ID')
bt.add_edge('x0', 'ID')
bt.add_edge('x0', 'NEG')
bt.add_edge('NEG', 'NEG(T)')
bt.add_edge('NEG', 'NEG(F)')
bt.add_edge('ID', 'ID(T)')
bt.add_edge('ID', 'ID(F)')
