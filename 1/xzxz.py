graph = {
    'A' : [['B', 3], ['G', 1], ['J', 4]],
    'G' : [['J', 6], ['F', 8], ['E', 14]],
    'B' : [['D', 10]], 'C' : [],
    'D' : [['H', 11]], 'E' : [['F', 2], ['I', 1]],
    'F' : [['H', 4], ['I', 2]], 'H' : [['C', 3]],
    'I' : [['H', 6]], 'J' : [['D', 3]]
}

Path_Cost = {
    'A' : ['empty', 0],
    'B' : ['A', 3],
    'C' : ['H', 16],
    'D' : ['J', 7],
    'E' : ['G', 15],
    'F' : ['G', 9],
    'G' : ['A', 1],
    'H' : ['F', 13],
    'I' : ['F', 11],
    'J' : ['A', 4]
}

def minimum(a):
    MinIndex = 0
    Minimum_Cost = Path_Cost[a[0][0]][1]
    for i in range(1,len(a)):
        if Path_Cost[a[i][0]][1] < Minimum_Cost:
            MinIndex = i
    return MinIndex

Explored = [] 
result = []
queue = []



def UniformCostSearch(Explored, graph, node):
    print("Searching sequence: ")
    Explored .append(node)
    queue.append(node)
    while queue:
        r = queue.pop(0) 
        print (r, end = " ") 
        if r == 'C':
            node = 'C'
            result.append(node)
            while node != 'A':
                result.append(Path_Cost[node][0])
                node =Path_Cost [node][0]
            print()
            print("Shortest path from A to C is:")

                
        while len(graph[r])>=1:
            MinIndex = minimum(graph[r])
            neighbour =graph[r][MinIndex][0]
            graph[r].pop(MinIndex)
            if neighbour not in Explored:    
                Explored.append(neighbour)
                queue.append(neighbour)


UniformCostSearch(Explored, graph, 'A')
