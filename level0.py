import random
import json


def nearest_neighbor(graph, start_vertex):
    unvisited = set(graph.keys())
    current_vertex = start_vertex
    path = [current_vertex]
    unvisited.remove(current_vertex)
    pathlength=0
    while unvisited:
        distances = graph[current_vertex]
        nearest_dist = float('inf')
        nearest_vertex = ""

        for i in range(len(distances)):
            if distances[i] <= nearest_dist and "n"+str(i) in unvisited:
                nearest_dist = distances[i]
                nearest_vertex = "n"+str(i)
 
        path.append(nearest_vertex)
        pathlength+=nearest_dist
        unvisited.remove(nearest_vertex)
        current_vertex = nearest_vertex

    path.append(start_vertex)
    return path,pathlength

if __name__ == "__main__":
    f = open('C:/Users/TEMP.CS2K16.000/Downloads/level0.json')
    data = json.load(f)
    num_vertices = data['n_neighbourhoods']
    random.seed(42)
    neigbours=data['neighbourhoods']
    adj={i:neigbours[i]['distances'] for i in neigbours.keys()}
    adj['r0']=data['restaurants']['r0']['neighbourhood_distance']
    start_vertex='r0'
    tour_temp,tour_length = nearest_neighbor(adj,start_vertex)
    print(tour_temp,tour_length)       
    print("Min_path for delivery man:")
    print("Path:", tour_temp)
    print("Total Length:", tour_length)
 
    # Data to be written
    dictionary = {
        "v0":{
        "path":tour_temp,
        },
    }
    print(dictionary)
    with open("C:/Users/TEMP.CS2K16.000/Downloads/output_level0.json", "w") as outfile:
        json.dump(dictionary, outfile)
