# coding: utf-8
import networkx as nx
G = nx.complete_graph(5)
nx.drawing.nx_pydot.write_dot(G, '5-connect.dot')
Bool_one = nx.MultiDigraph()
Bool_one = nx.MultiDiGraph()
Bool_one.add_node('True')
Bool_one.add_node('False')
Bool_one.node[0]
Bool_one.nodes()
Bool_one.nodes(data=True)
Bool_one.nodes['True']
Bool_one.node['True']
Bool_one.node['True']['label'] = 'True'
nx.drawing.nx_pydot.write_dot(G, 'Bool.dot')
nx.drawing.nx_pydot.write_dot(Bool_one, 'Bool.dot')
Bool_one.node['True']['label'] = 'True!'
nx.drawing.nx_pydot.write_dot(Bool_one, 'Bool.dot')
Bool_one.node['True']['label'] = 'True'
Bool_one.node['True']['shape'] = 'box'
nx.drawing.nx_pydot.write_dot(Bool_one, 'Bool.dot')
Bool_one.node['True']['shape'] = 'box'
Bool_one.node['False']['shape'] = 'box'
del Bool_one
B = nx.MultiDiGraph()
B[False] = {}
B.add_node(True)
B.add_node(False)
nx.drawing.nx_pydot.write_dot(B, 'Bool.dot')
B.nodes[True]['shape'] = 'box'
B.node[True]['shape'] = 'box'
B.node[False]['shape'] = 'box'
nx.drawing.nx_pydot.write_dot(B, 'Bool.dot')
B.add_edge(True, True, label='ID(True)')
B.add_edge(False, False, label='ID(False)')
nx.drawing.nx_pydot.write_dot(B, 'Bool.dot')
B.add_edge(True, False, label='!(True)')
B.add_edge(False, True, label='!(False)')
nx.drawing.nx_pydot.write_dot(B, 'Bool.dot')
B.node[True]['color'] = 'red'
nx.drawing.nx_pydot.write_dot(B, 'Bool.dot')
B.node[True]['color'] = 'blue'
B.node[False]['color'] = 'red'
nx.drawing.nx_pydot.write_dot(B, 'Bool.dot')
bt = nx.MultiDiGraph()
bt.add_node('x0')
bt.add_node('ID')
bt.add_node('NEG')
bt.add_link('x0','ID')
bt.add_edge('x0','ID')
bt.add_edge('x0','NEG')
bt.add_edge('NEG','NEG(T)')
bt.add_edge('NEG','NEG(F)')
bt.add_edge('ID','ID(T)')
bt.add_edge('ID','ID(F)')
nx.drawing.nx_pydot.write_dot(bt, 'bintree.dot')
nx.drawing.nx_agraph.to_agraph.__doc__
print nx.drawing.nx_agraph.to_agraph.__doc__
print nx.drawing.nx_agraph.write_dot.__doc__
print nx.drawing.nx_agraph.__doc__
bt
bt.nodes
bt.nodes()
get_ipython().magic(u'save')
help %save 
