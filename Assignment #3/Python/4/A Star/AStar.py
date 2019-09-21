import queue as Q
import input as init

pq = Q.PriorityQueue()

def AStar():
    source = input("Source Node : ")
    destination = input("Destination Node: ")
    pq.put((source, init.heuristic[source], source, 0, 0 + init.heuristic[source]))

    while not(pq.empty()):
        u = pq.get()
        if (u[0] == destination):
             print('Path: ' + u[2])
             print('Optimal Cost: ' + str((u[3] + u[4])))
             return
        for v in init.graph[u[0]]:
            pq.put((v[0], init.heuristic[v[0]], u[2] + '->' + v[0], u[3] + v[1], init.heuristic[v[0]]))

    print("Path not found!")

#Main
AStar()




