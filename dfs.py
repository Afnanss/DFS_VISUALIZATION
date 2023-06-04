# -*- coding: utf-8 -*-
"""dfs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ko-i_MPRwO4JzfH96pET5moeQrB9dMbk
"""

import time
Afnan = {
    'A': ['N'],
    'N': ['F'],
    'F': [],
    'Z': [] 
    }
Nanfa = {
    'A': ['F','N'],
    'N': ['B','F'],
    'F': ['A','B'],
    'B': ['F','N'] 
    }
def dfs(graph, start_vertex):
    visited = set()  # To track visited nodes
    stack = [start_vertex]  # Initialize stack with the start vertex
    while stack:
        vertex = stack.pop()  # Take the top vertex from the stack
        if vertex not in visited
            visited.add(vertex)  # Mark the current node as visited
            print(vertex, end=' ')
            # Push unvisited adjacent vertices to the stack
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
# Call DFS starting from a specific vertex
start_time = time.time_ns()  # Get the start time in nanoseconds
print("DFS Traversal for first grapgh:")
dfs(Afnan, 'A')
print()
end_time = time.time_ns()  # Get the end time in nanoseconds
execution_time1 = (end_time - start_time) / 1000  # Convert to microseconds
start_time = time.time_ns()  # Get the start time in nanoseconds
print("DFS Traversal for second grapgh:")
dfs(Nanfa, 'A')
print()
end_time = time.time_ns()  # Get the end time in nanoseconds
execution_time2 = (end_time - start_time) / 1000  # Convert to microseconds
print("Execution Time for the first is: {:.6f} microseconds".format(execution_time1))
print("Execution Time for the second is: {:.6f} microseconds".format(execution_time2))

import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([('A', 'N'), ('N', 'F'),('Z','Z')])

# Create figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot the best case scenario (not going to any other grapgh)
nx.draw_networkx(G, ax=ax1, with_labels=True, node_color='lightblue')
ax1.set_title('Best Case Scenario (Afnan grapgh)')
# Plot the worst case scenario (visit all edges)
G.clear()
G.add_edges_from([('A', 'F'), ('F', 'B'), ('B', 'N')])
nx.draw_networkx(G, ax=ax2, with_labels=True, node_color='lightblue')
ax2.set_title('Worst Case Scenario(Nnafa grapgh)')

# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.5)

# Display the plots
plt.show()