import constraint
import matplotlib.pyplot as plt
import networkx as nx
problem = constraint.Problem()
regions = ['Kankavli', 'Kudal', 'Malvan', 'Devgad', 'Vaibhavwadi', 'Dodamarg', 'Vengurla', 'Sawantwadi']
colors = ['Red', 'Green', 'Blue', 'Pink', "Yellow"]
for region in regions:
    problem.addVariable(region, colors)
neighbours = {
    'Vaibhavwadi': ['Kankavli', 'Devgad'],
    'Kankavli': ['Kudal', 'Devgad', 'Malvan', 'Vaibhavwadi'],
    'Devgad': ['Kankavli', 'Malvan', 'Vaibhavwadi'],
    'Malvan': ['Kudal', 'Kankavli', 'Devgad', 'Vengurla'],
    'Kudal': ['Sawantwadi', 'Kankavli', 'Vengurla', 'Malvan'],
    'Vengurla': ['Malvan', 'Kudal', 'Sawantwadi'],
    'Sawantwadi': ['Kudal', 'Vengurla', 'Dodamarg'],
    'Dodamarg': ['Sawantwadi'] }
for region, adjacent in neighbours.items():
    for neighbour in adjacent:
        problem.addConstraint(lambda r, n: r != n, (region, neighbour))
solution = problem.getSolution()
for city, color in solution.items():
    print(city, " has color ", color)
G = nx.Graph()
for city, color in solution.items():
    G.add_node(city, color=color)
for region, adjacent in neighbours.items():
    for neighbour in adjacent:
        G.add_edge(region, neighbour)
node_colors = [G.nodes[node]['color'] for node in G.nodes]
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=10, font_weight='bold')
plt.show()
