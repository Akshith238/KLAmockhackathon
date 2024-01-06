
import random
import json


def nearest_neighbor(graph, start_vertex, capacity_limit):
    unvisited = set(graph.keys())
    current_vertex = start_vertex
    path = [current_vertex]
    unvisited.remove(current_vertex)
    pathlength = 0
    capacity_used = 0

    while unvisited:
        distances = graph[current_vertex]
        nearest_dist = float('inf')
        nearest_vertex = ""
        for i in range(len(distances)):
            if  "n"+str(i) not in visited and distances[i] < nearest_dist and "n" + str(i) in unvisited:
                nearest_dist = distances[i]
                nearest_vertex = "n" + str(i)
        if nearest_vertex=="" or capacity_used + orders[nearest_vertex]>capacity_limit:
            break

        path.append(nearest_vertex)
        visited.add(nearest_vertex)
        pathlength += nearest_dist
        capacity_used += orders[nearest_vertex]
        unvisited.remove(nearest_vertex)
        current_vertex = nearest_vertex

    path.append(start_vertex)
    return path, pathlength,capacity_used
def format_paths_to_dictionary(paths):
    path_dict = {}
    for i, path in enumerate(paths):
        path_dict[f"path{i+1}"] = path
    return path_dict

if __name__ == "__main__":
    f = open('C:/Users/TEMP.CS2K16.000/Downloads/level1b.json')
    data = json.load(f)
    num_vertices = data['n_neighbourhoods']
    neigbours=data['neighbourhoods']
    adj={i:neigbours[i]['distances'] for i in neigbours.keys()}
    adj['r0']=data['restaurants']['r0']['neighbourhood_distance']
    start_vertex='r0'
    keys=data['neighbourhoods'].keys()
    scooter_capacity=data['vehicles']['v0']['capacity']
    orders={i:0 for i in keys}
    for i in orders.keys():
        orders[i]=data['neighbourhoods'][i]['order_quantity']
    visited=set()
    paths=[]
    while(len(visited)<=num_vertices-1):
        tour_temp,tour_length,capacity=nearest_neighbor(adj, start_vertex,scooter_capacity)
        paths.append(tour_temp)
    formatted_paths = format_paths_to_dictionary(paths)
    dictionary = {
        "v0": formatted_paths,
    }        
    print(dictionary)
    with open("C:/Users/TEMP.CS2K16.000/Downloads/level1b_output.json", "w") as outfile:
        json.dump(dictionary, outfile)