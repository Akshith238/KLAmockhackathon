import random
import math

def nearest_neighbor(graph, start_vertex=0):
    num_vertices = len(graph)
    unvisited = set(range(num_vertices))
    current_vertex = start_vertex
    path = [current_vertex]
    unvisited.remove(current_vertex)

    while unvisited:
        nearest_vertex = min(unvisited, key=lambda vertex: graph[current_vertex][vertex])
        path.append(nearest_vertex)
        unvisited.remove(nearest_vertex)
        current_vertex = nearest_vertex

    path.append(start_vertex)
    return path

def calculate_path_length(graph, path):
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i]][path[i+1]]
    return length

def generate_random_graph(num_vertices):
    return [[random.randint(1, 10) if i != j else 0 for j in range(num_vertices)] for i in range(num_vertices)]

if __name__ == "__main__":
    num_vertices = 21
    random.seed(42)
    graph = [[random.randint(0,100) for j in range(num_vertices)] for i in range(num_vertices)]
    tour_length=float('inf')
    tour=[]
    # Apply Nearest Neighbor Algorithm
    for start_vertex in range(0,21):
        tour_temp = nearest_neighbor(graph, start_vertex)
        tour_len_temp=calculate_path_length(graph, tour_temp)
        if tour_len_temp<tour_length:
            tour=tour_temp
            tour_length=tour_len_temp
            

    # Print the results
    print("Min_path for delivery man:")
    print("Path:", tour)
    print("Total Length:", tour_length)