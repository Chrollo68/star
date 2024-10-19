import heapq
def a_star (graph, heurastics, start, goal):
    open_list=[]
    heapq.heappush(open_list,(heurastics.get(start),0,start,[]))
    came_from={}
    cost_so_far={start:0}

    while open_list:
        f,current_cost,current_node,path=heapq.heappop(open_list)

        if(current_node==goal):
            return path+[current_node]
        
        for neighbour,cost in graph.get(current_node,{}).items():
            new_cost = current_cost+cost
            
            if neighbour not in cost_so_far or new_cost<cost_so_far[neighbour]:
                cost_so_far[neighbour]=new_cost
                priority=new_cost+heurastics.get(neighbour)
                heapq.heappush(open_list,(priority,new_cost,neighbour,path+[current_node]))
                came_from[neighbour]=current_node
    return None

graph={
    'A':{'B':1,'C':4},
    'B':{'C':2,'D':5},
    'C':{'D':1},
    'D':{}
}

heurastics={
    'A':7,
    'B':6,
    'C':2,
    'D':0
}

start='A'
goal='D'

path=a_star(graph,heurastics,start,goal)

if(path):
    print("Path found :",path)
else:
    print("Path not found ")
