# Lets do something creative with our time
#from pip._vendor import requests

# Something goes here
"""
def get_flight_data():
    url = 'https://opensky-network.org/api/states/all'
    response = requests.get(url)
    data = response.json()
    return data
flight_data = get_flight_data()
print(flight_data)
"""
"""
def rotate_matrix_inplace(matrix):

    # Step 1. Transpose the matrix
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


rotate_matrix_inplace(matrix)
print(matrix)
"""

import heapq

class Suurballe:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: {} for i in range(vertices)
        }
    
    def add_edge(self, u, v, weight):
        self.adj[u][v] = weight