import networkx as nx
import matplotlib.pyplot as plt
import textwrap

# Create a directed graph
G = nx.DiGraph()

# TODO: lots of problems here mainly that the axioms disappear out of scope so you can't see the bottom ones and the definitions appear partially out of the right side of the frame. Overall it appears to be dynamically readjusting.


# Add nodes (axioms, beliefs, and definitions)
G.add_node("()", type="axiom")
# G.add_node("There is order to the universe", type="axiom")
G.add_node("I can understand the order", type="axiom")
G.add_node("Data input varies in reliability", type="axiom")
G.add_node("I can add data by querying third parties", type="axiom")
G.add_node("There is order to the universe", type="axiom")
G.add_node("I need to continually reassess the reliability of this data", type="belief")
G.add_node("My base sensory data is somewhat reliable", type="belief")
G.add_node("If you score the data reliability along a linear axis this will produce more reliable results than binary data", type="belief")
G.add_node("This data can be aggregated", type="belief")

G.add_node("phenomenological scope", type="definition")

# Add edges (relationships)
G.add_edge("There is order to the universe", "My base sensory data is somewhat reliable")
G.add_edge("This data can be aggregated", "phenomenological scope")
G.add_edge("Data input varies in reliability", "I need to continually reassess the reliability of this data")
G.add_edge("I can add data by querying third parties", "This data can be aggregated")
G.add_edge("This data can be aggregated", "If you score the data reliability along a linear axis this will produce more reliable results than binary data")



# Human social dynamics




# Create a custom layout
# pos = {}
pos = nx.spring_layout(G, scale=2)  # scale parameter to spread nodes further apart

axioms = [node for node in G.nodes() if G.nodes[node]['type'] == 'axiom']
beliefs = [node for node in G.nodes() if G.nodes[node]['type'] == 'belief']
definitions = [node for node in G.nodes() if G.nodes[node]['type'] == 'definition']

# Position axioms along the left side
for i, axiom in enumerate(axioms):
    pos[axiom] = (0, i - 0.9)

# Position beliefs to the right of axioms
for i, belief in enumerate(beliefs):
    pos[belief] = (0.1, i)  # Adjust the vertical position

# Position definitions to the right of beliefs
for i, definition in enumerate(definitions):
    pos[definition] = (0.2, i)  # Adjust the vertical position

# Set figure size
plt.figure(figsize=(16, 10))  # Increase the figure size

# Draw nodes with different colors based on their type
node_colors = ["lightblue" if G.nodes[node]['type'] == 'axiom' else 
               "lightgreen" if G.nodes[node]['type'] == 'belief' else 
               "lightyellow" for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=4000, node_color=node_colors)  # Increase the node size

# Draw edges
nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True)

# Draw labels with line wrapping
labels = {node: textwrap.fill(node, width=20) for node in G.nodes()}  # Adjust width as needed
nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight="bold", horizontalalignment='left', verticalalignment='center')

# Create a legend
axiom_legend = plt.Line2D([], [], color='lightblue', marker='o', markersize=10, label='Axiom')
belief_legend = plt.Line2D([], [], color='lightgreen', marker='o', markersize=10, label='Belief')
definition_legend = plt.Line2D([], [], color='lightyellow', marker='o', markersize=10, label='Definition')
plt.legend(handles=[axiom_legend, belief_legend, definition_legend])

plt.axis('off')
plt.tight_layout()
plt.show()