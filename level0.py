import random
import json


def nearest_neighbor(graph, num_vertices,start_vertex=0):
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
    f = open('C:/Users/TEMP.CS2K16.000/Downloads/level0.json')
    data = json.load(f)
    num_vertices = data['n_neighbourhoods']
    random.seed(42)
    neigbours=data['neighbourhoods']
    adj={i:neigbours[i]['distances'] for i in neigbours.keys()}
    graph = [[adj[j][i] for j in adj.keys()] for i in range(num_vertices-1)]
    tour_length=float('inf')
    tour=[]
    for start_vertex in range(0,num_vertices-1):
        tour_temp = nearest_neighbor(graph,start_vertex)
        tour_len_temp=calculate_path_length(graph,tour_temp)
        if tour_len_temp<tour_length:
            tour=tour_temp
            tour_length=tour_len_temp
            
    # Print the results
    print("Min_path for delivery man:")
    print("Path:", tour)
    print("Total Length:", tour_length)
    import json
 
# Data to be written
dictionary = {
    "optimallocation":tour[0],
    "path": tour,
    "tourlength": tour_length,
}
 
with open("C:/Users/TEMP.CS2K16.000/Downloads/output_level0.json", "w") as outfile:
    json.dump(dictionary, outfile)
