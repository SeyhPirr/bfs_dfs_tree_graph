cities_tree = {
    'Ankara': ['Konya', 'Eskisehir'],
    'Konya': ['Kayseri'],
    'Kayseri': ['Adana', 'Mersin'],
    'Eskisehir': ['Antalya', 'Izmir'],
    'Izmir': ['Bursa'],
    'Bursa': ['Istanbul'],
    'Istanbul': ['Kocaeli'],
    'Kocaeli': ['Sakarya'],
    'Adana': [],
    'Mersin': [],
    'Antalya': [],
    'Sakarya': []
}
cities_graph = {
    'Ankara': ['Konya', 'Eskisehir'],
    'Konya': ['Ankara', 'Kayseri'],
    'Kayseri': ['Konya', 'Adana'],
    'Adana': ['Kayseri', 'Mersin'],
    'Mersin': ['Adana', 'Antalya'],
    'Antalya': ['Mersin', 'Izmir'],
    'Izmir': ['Antalya', 'Bursa'],
    'Bursa': ['Izmir', 'Istanbul'],
    'Istanbul': ['Bursa', 'Kocaeli'],
    'Kocaeli': ['Istanbul', 'Sakarya'],
    'Sakarya': [],
    'Eskisehir': [] 
}
from collections import deque

def bfs_shortest_path_with_count(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  
    iterations = 0  

    while queue:
        iterations += 1  
        city, path = queue.popleft()

        if city == goal:
            return path, iterations  

        if city not in visited:
            visited.add(city)
            for neighbor in graph[city]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None, iterations  

path, iterations = bfs_shortest_path_with_count(cities_graph, 'Ankara', 'Sakarya')
print(f"Ankaradan sakaryaya giden yol(BFS(GRAPH): {path}")
print(f"Toplam tekrar sayisi(BFS): {iterations}")
def dfs_shortest_path_with_count(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path, len(path)  

    shortest_path = None  

    for neighbor in graph[start]:
        if neighbor not in visited:
            result, iterations = dfs_shortest_path_with_count(graph, neighbor, goal, visited.copy(), path.copy())
            
            if result and (shortest_path is None or len(result) < len(shortest_path)):
                shortest_path = result

    return shortest_path, len(shortest_path) if shortest_path else float('inf')  
path, iterations = dfs_shortest_path_with_count(cities_graph, 'Ankara', 'Sakarya')
print(f"Ankaradan Sakaryaya giden yol(DFS)(GRAPH): {path}")
print(f"Toplam iterasyon(DFS): {iterations}")

#siradan tree yapilari var
path, iterations = bfs_shortest_path_with_count(cities_tree, 'Ankara', 'Sakarya')
print(f"Ankaradan Sakaryaya giden yol(BFS)(TREE): {path}")
print(f"Toplam iterasyon(DFS)(TREE): {iterations}")
#dfs
path, iterations = dfs_shortest_path_with_count(cities_tree, 'Ankara', 'Sakarya')
print(f"Ankaradan Sakaryaya giden yol(DFS)(TREE): {path}")
print(f"Toplam iterasyon(DFS)(TREE): {iterations}")