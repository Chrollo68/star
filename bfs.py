graph={'Kankavli':['Devgad','Malvan','Kudal','Vaibhavwadi'],
   'Kudal':['Kankavli','Malvan','Sawantwadi','Vengurla'],
   'Malvan':['Kudal','Kankavli','Devgad','Vengurla'],
   'Devgad':['Malvan','Kankavli','Vaibhavwadi'],
   'Sawantwadi':['Kudal','Vengurla','Dodamarg'],
   'Dodamarg':['Sawantwadi'],
   'Vaibhavwadi':['Devgad','Kankavli'],
   'Vengurla':['Kudal','Malvan','Sawantwadi']}
visited=list()
queue=list()
bfs=list()
def BFS(node,visited,graph):
  if(node not in visited):
    visited.append(node)
    queue.append(node)
    while queue:
      m=queue.pop(0)
      bfs.append(m)
      for i in graph[m]:
        if (i not in visited):
          visited.append(i)
          queue.append(i)
BFS('Kankavli',visited,graph)
print ("The bfs path is : ")
for i in bfs:
  print(i+" ",end="")
