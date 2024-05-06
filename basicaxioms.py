import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes (axioms and beliefs)
G.add_node("There is order to the universe", type="axiom")
G.add_node("I can understand the order", type="axiom")
G.add_node("Data input varies in reliablity", type="axiom")
G.add_node("I need to continually reassess the reliablity of this data ", type="belief")

G.add_node("My base sensory data is somewhat reliable", type="belief")
G.add_node("If you score the data reliablity along a linear axis this will produce more reliable results than binary data", type="belief")
G.add_node("I can add data by querying third parties", type="axiom")
G.add_node("This aggregated data is known as phenomonological scope", type="definition")

# Add edges (relationships)
G.add_edge("There is order to the universe", "My base sensory data is somewhat reliable")
G.add_edge("I can add data by querying third parties", "This aggregated data is known as phenomonological scope")


# Visualize the tree
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")
plt.show()
