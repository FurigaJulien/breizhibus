from BreizhibusBDD import BDD

def getGraph():
    dict1={}
    lines=BDD.getLines()
    for line in lines:
        dict1[line.name]=sorted(BDD.getStops(line.id)[0],key= lambda x:x.sens)

    
    graph={}
    
    for value in dict1.values():
        
        for i in range(len(value)):
            dict2={}
            
            if i==0:
                dict2[value[i+1].name]=1
            elif i==len(value)-1:
                dict2[value[i-1].name]=1
            else:
                dict2[value[i-1].name]=1
                dict2[value[i+1].name]=1

            
            if value[i].name in graph:
                
                graph[value[i].name].update(dict2)
            else:
                
                graph[value[i].name]=dict2

    return graph,dict1

def dijkstra(initial,final):
    
    path = {}
    adj_node = {}
    queue = []
    finalpath=[]
    graph,lines = getGraph()
    print(graph)
    for node in graph:
        path[node] = float("inf")
        adj_node[node] = None
        queue.append(node)
        print(queue)
        
    path[initial] = 0
    while queue:
        # find min distance which wasn't marked as current
        key_min = queue[0]
        min_val = path[key_min]
        for n in range(1, len(queue)):
            if path[queue[n]] < min_val:
                key_min = queue[n]  
                min_val = path[key_min]
        cur = key_min
        queue.remove(cur)
        
        
        for i in graph[cur]:
            alternate = graph[cur][i] + path[cur]
            if path[i] > alternate:
                path[i] = alternate
                adj_node[i] = cur
                
                
    x = final
    print('The path between A to H')
    print(x, end = '<-')
    finalpath.append(x)
    while True:
        x = adj_node[x]
        if x is None:
            print("")
            break
        print(x, end='<-')
        finalpath.append(x)
    finalpath.reverse()
    return finalpath,lines

def getItineraire(path,lines):
    potentialStarts={}
    for line,orderedStopList in lines.items():
        if path[0] in orderedStopList:
            potentialStarts[line]=path[0]

    for line in potentialStarts.keys():
        path=2
            
        

print(dijkstra('Karadoc','Perceval'))


