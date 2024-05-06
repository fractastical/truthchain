import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes (axioms and beliefs)
G.add_node("Axiom1", type="axiom")
G.add_node("Axiom2", type="axiom")
G.add_node("Belief1", type="belief")
G.add_node("Belief2", type="belief")
G.add_node("Belief3", type="belief")

# Add edges (relationships)
G.add_edge("Axiom1", "Belief1")
G.add_edge("Axiom1", "Belief2")
G.add_edge("Axiom2", "Belief2")
G.add_edge("Belief1", "Belief3")

# Visualize the tree
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")
plt.show()
