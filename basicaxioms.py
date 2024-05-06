import networkx as nx
import matplotlib.pyplot as plt
import textwrap

# Create a directed graph
G = nx.DiGraph()

# Add nodes (axioms, beliefs, and definitions)
G.add_node("There is order to the universe", type="axiom")
G.add_node("I can understand the order", type="axiom")
G.add_node("Data input varies in reliability", type="axiom")
G.add_node("I need to continually reassess the reliability of this data", type="belief")
G.add_node("My base sensory data is somewhat reliable", type="belief")
G.add_node("If you score the data reliability along a linear axis this will produce more reliable results than binary data", type="belief")
G.add_node("I can add data by querying third parties", type="axiom")
G.add_node("This aggregated data is known as phenomenological scope", type="definition")

# Add edges (relationships)
G.add_edge("There is order to the universe", "My base sensory data is somewhat reliable")
G.add_edge("I can add data by querying third parties", "This aggregated data is known as phenomenological scope")

# Create a layout for the graph
pos = nx.spring_layout(G, seed=42)

# Set figure size
plt.figure(figsize=(12, 8))

# Draw nodes with different colors based on their type
node_colors = ["lightblue" if G.nodes[node]['type'] == 'axiom' else 
               "lightgreen" if G.nodes[node]['type'] == 'belief' else 
               "lightyellow" for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_colors)

# Draw edges
nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True)

# Draw labels with line wrapping
labels = {node: textwrap.fill(node, width=30) for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight="bold")

# Create a legend
axiom_legend = plt.Line2D([], [], color='lightblue', marker='o', markersize=10, label='Axiom')
belief_legend = plt.Line2D([], [], color='lightgreen', marker='o', markersize=10, label='Belief')
definition_legend = plt.Line2D([], [], color='lightyellow', marker='o', markersize=10, label='Definition')
plt.legend(handles=[axiom_legend, belief_legend, definition_legend])

plt.axis('off')
plt.tight_layout()
plt.show()