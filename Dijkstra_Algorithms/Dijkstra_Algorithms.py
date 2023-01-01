
Shortest_Path ={}
def dijkstra(graph , Node):
    global Shortest_Path
    Shortest_Path[Node] = 0
    growing_node = {Node}
    while (len(growing_node) != len(graph) ):
        mini = 1000000
        mini_edge = (None , None)
        for node in growing_node:
            for edge in graph[node]:
                head_node = edge.split(",")[0]
                length = int(edge.split(",")[1])
                if head_node not in growing_node:
                    if Shortest_Path[node]+ length < mini:
                        mini_edge = (node ,head_node)
                        mini = Shortest_Path[node] + length
        if mini_edge != (None , None):
            growing_node.add(mini_edge[1])
            Shortest_Path[mini_edge[1]] = mini
        else:
            for key in graph.keys():
                if key not in growing_node:
                    growing_node.add(key)
                    Shortest_Path[key] = mini
                
graph = {}
with open('Dijkstra_Data.txt') as f:
    data = f.readlines()
    for line in data:
        elements = list(map(str,line.split('\t')[:-1]))
        graph[str(elements[0])] = elements[1:]
f.close()

dijkstra(graph , "1")

ans = ' '
for i in ['7','37','59','82','99','115','133','165','188','197']:
    ans += str(Shortest_Path[i]) + ","

ans = ans[:-1]

print(ans)