from graphviz import Digraph

dot = Digraph(comment="Binary Tree")

# Add nodes
dot.node("A", "A")
dot.node("B", "B")
dot.node("C", "C")
dot.node("D", "D")
dot.node("E", "E")
dot.node("F", "F")
dot.node("G", "G")

# Add edges
dot.edge("A", "B")
dot.edge("A", "C")
dot.edge("B", "D")
dot.edge("B", "E")
dot.edge("C", "F")
dot.edge("C", "G")

# Render and display
dot.render("binary_tree.gv", view=True)