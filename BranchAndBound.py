import heapq

class Node:
    def __init__(self, level, path, cost, bound):
        self.level = level
        self.path = path
        self.cost = cost
        self.bound = bound

    def __lt__(self, other):
        return self.bound < other.bound

def calculate_bound(node, distance_matrix, n):
    cost = node.cost
    visited = set(node.path)
    for i in range(n):
        if i not in visited:
            min_edge = min([distance_matrix[i][j] for j in range(n) if j != i and j not in visited], default=0)
            cost += min_edge
    return cost

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def branch_and_bound_tsp(distance_matrix):
    n = len(distance_matrix)
    pq = []
    initial_path = [0]
    initial_node = Node(0, initial_path, 0, calculate_bound(Node(0, initial_path, 0, 0), distance_matrix, n))
    heapq.heappush(pq, initial_node)

    min_cost = float('inf')
    best_path = []

    while pq:
        current_node = heapq.heappop(pq)

        if current_node.bound < min_cost:
            for i in range(1, n):
                if i not in current_node.path:
                    new_path = current_node.path + [i]
                    new_cost = current_node.cost + distance_matrix[current_node.path[-1]][i]
                    new_node = Node(current_node.level+1, new_path, new_cost, 0)

                    if new_node.level == n-1:
                        final_cost = new_cost + distance_matrix[i][0]
                        if final_cost < min_cost:
                            min_cost = final_cost
                            best_path = new_path + [0]
                    else:
                        new_node.bound = calculate_bound(new_node, distance_matrix, n)
                        if new_node.bound < min_cost:
                            heapq.heappush(pq, new_node)
    return best_path, min_cost

# Ví dụ sử dụng
path, distance = branch_and_bound_tsp(distance_matrix)
print("Đường đi ngắn nhất (Branch and Bound):", path)
print("Chi phí:", distance)