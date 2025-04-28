import itertools

def calculate_distance(path, distance_matrix):
    return sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path)-1)) + distance_matrix[path[-1]][path[0]]

def brute_force_tsp(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_path = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities):
        current_distance = calculate_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm

    return min_path, min_distance

# Ví dụ sử dụng
distance_matrix = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

path, distance = brute_force_tsp(distance_matrix)
print("Đường đi ngắn nhất:", path)
print("Chi phí:", distance)