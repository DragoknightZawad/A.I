import queue as Q

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','J','G'],
    'B' : ['D','A'],
    'J' : ['A','D','G'],
    'G' : ['A','J','F','E'],
    'D' : ['B','J','H'],
    'H' : ['D','F','I','C'],
    'F' : ['H','G','E''I'],
    'C':['H']
}


frontier =  {
    'A' :0,
    'B' :3,
    'J' :4,
    'G' :1,
    'D' :10,
    'H' :11,
    'F' :8,
    'C':3
}
goalState = ['C']



def loop():
    if not frontier:
        return
    l=frontier.pop(random.randint(0,len(frontier)-1))
    if l == goalState:
        return
    visited.append(l)
    for neighbour in graph[l]:
        if neighbour not in frontier and neighbour not in visited:    
            frontier.append(neighbour)
    loop()

goalState = ['C']
visited1 = [] 

def search(graph, frontier,goalState ):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return
    
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        
        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break
        
        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))
        
def readGraph():
    lines = int( input() )
    graph = {}
    
    for line in range(lines):
        line = input()
            
        tokens = line.split()
        node = tokens[0]
        graph[node] = {}
        
        for i in range(1, len(tokens) - 1, 2):
            # print(node, tokens[i], tokens[i + 1])
            # graph.addEdge(node, tokens[i], int(tokens[i + 1]))
            graph[node][tokens[i]] = int(tokens[i + 1])
    return graph

def main():
    graph = readGraph()
    search(graph, 'Arad', 'Bucharest')
    
if __name__ == "__main__":
    main()
