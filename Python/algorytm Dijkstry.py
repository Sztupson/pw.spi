# trasa a-b-c-d-e
# A - A = 0
# B, C ,D ,E = nieskonczonosc
# Majac dana mape sieci drogowej miedzy miastami z odleglosciami pomiedzy nimi jako wagi krawedzi, uzyj algorytmu dijkstry, aby znalezc 

#  Dane wejsciowe

graph = {
    'A' : {'B':2, 'D':4},
    'B' : {'C':3, 'D':4},
    'C' : {'E':2},
    'D' : {'C':3, 'E':4},
    'E' : {}
}

def algorytm_dijkstra(graph, start, goal):
    
    # ustaw odleglosci na nieskonczonosc
    shortest_distances = {vortex:float('infinity')for vortex in graph}
    # dla wierzcholka startowego odleglosc ustaw na 0
    shortest_distances[start] = 0

    predecessors = {}
    # nieodwiedzone wierzchołki
    unvisited = graph.copy()
    # peetle nieodwiedzonych wierzcholkow
    while unvisited:
        # wybierz wierzcholek z najmniejsza odlegloscia
        current_min_vortex = None
        for vortex in unvisited:
            if current_min_vortex is None:
                current_min_vortex = vortex
            elif shortest_distances[vortex] < shortest_distances[current_min_vortex]:
                current_min_vortex = vortex
        # sprawdz wsyzstkich sasiadow aktualnego wierzcholka
    for neighbour, cost in graph[current_min_vortex].item():
        if cost + shortest_distances[current_min_vortex] < shortest_distances[neighbour]:
            shortest_distances[neighbour] = cost + shortest_distances[current_min_vortex]
            predecessors[neighbour] = current_min_vortex
        # usun z listy przetworzony wierzcholek
        unvisited.pop(current_min_vortex)
    # odtworzenie sciezki od startu do celu
    current_vortex = goal
    path = []

    while current_vortex != start:
        path.append(current_vortex)
        current_vortex - predecessors[current_vortex]
    path.append(start)

    return path[::-1], shortest_distances[goal]

