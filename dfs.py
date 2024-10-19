import matplotlib.pyplot as plt
import networkx as nx
graph={'Kankavli':['Devgad','Malvan','Kudal','Vaibhavwadi'],
   'Kudal':['Kankavli','Malvan','Sawantwadi','Vengurla'],
   'Malvan':['Kudal','Kankavli','Devgad','Vengurla'],
   'Devgad':['Malvan','Kankavli','Vaibhavwadi'],
   'Sawantwadi':['Kudal','Vengurla','Dodamarg'],
   'Dodamarg':['Sawantwadi'],
   'Vaibhavwadi':['Devgad','Kankavli'],
   'Vengurla':['Kudal','Malvan','Sawantwadi']}
visited=list()
dfs=list()
def DFS(node,visited,graph):
  if(node not in visited):
    dfs.append(node)
    visited.append(node)
    for i in graph[node]:
      DFS(i,visited,graph)
DFS('Kankavli',visited,graph)
print ("The dfs path is : ")
for i in dfs:
  print(i+" ",end="")
G = nx.Graph(graph)
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G) # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10, font_weight='bold')
plt.title('Graph Visualization')
plt.show()
