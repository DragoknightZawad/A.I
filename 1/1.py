graph = {
    'Oradea' : [['Zerind', 71],['Sibiu' : 151]],
    'Zerind' : [['Oradea', 71], ['Arad', 75]],
    'Arad' : [['Zerind', 75], ['Timisoara', 118], ['Sibiu', 140]],
    'Timisoara' : [['Arad', 118],['Lugoj', 111]],
    'Lugoj' : [['Timisoara', 111], ['Mehadia', 70]],
    'Mehadia' : [['Lugoj', 70], ['Drobeta', 75]],
    'Drobeta' : [['Mehadia', 75],['Craiova', 120]],
    'Craiova' : [['Drobeta', 120]], ['Pitesti',138],['Rimnicu Vilcea',146]],
    'Pitesti' :[['Craiova',138],['Rimnicu Vilcea',97]],['Bucharest',101]],
    'Rimnicu Vilcea':[['Pitesti',97],['Craiova',146],['Sibiu',80]],
    'Sibiu':[['Rimnicu Vilcea',80],['Arad',140],['Oradea',151]],['Fagaras',99]],
    'Fagaras':[['Sibiu',99],['Bucharest',211]],
    'Bucharest':[[ 'Pitesti',101],['Fagaras',211],['Urziceni',85]]],
    'Urziceni':[['Bucharest',85],['Hirsova':86],['Vaslui',142]],
    'Hirsova':[['Urziceni',98],['Eforic',86]],
    'Vaslui':[['Urziceni',142],['lasi',92]]
    'lasi':[['Vaslui',92],['Neamt',87]]
    'Neamt':[['lasi',87]]
    
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
            print("Shortest path from A to C is:".format(Path_Cost['C'][1]))
            for i in result[::-1]:
                print(i, end = " ")
            print()
           
          

                
        while len(graph[r])>=1:
            MinIndex = minimum(graph[r])
            neighbour =graph[r][MinIndex][0]
            graph[r].pop(MinIndex)
            if neighbour not in Explored:    
                Explored.append(neighbour)
                queue.append(neighbour)

# Driver Code
UniformCostSearch(Explored, graph, 'A')
