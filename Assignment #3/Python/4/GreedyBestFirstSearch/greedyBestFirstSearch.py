import queue as Q
import input as init

pq = Q.PriorityQueue()

def greedyBestFirstSearch():
    source = input("Source Node : ")
    destination = input("Destination Node: ")
    init.visited[source] = True
    pq.put((source, init.heuristic[source], source)) # pq -> (i,80,i)

    while not(pq.empty()):
        u = pq.get() # u -> (i,80,i)
        init.visited[u] = True #init.visited[i] -> true
        if (u[0] == destination): # i != g
            print('Path: ' + u[2]) #wont be executed
            return
        for v in init.graph[u[0]]: # for v in init.graph[u]
            # print("graph of u is : ")
            # print(init.graph[u[0]])
            # print("\n")
            if not init.visited[v[0]]:
                pq.put((v[0], init.heuristic[v[0]], u[2] + '->' + v[0]))

    print("Path not found!")


#Main
greedyBestFirstSearch()




