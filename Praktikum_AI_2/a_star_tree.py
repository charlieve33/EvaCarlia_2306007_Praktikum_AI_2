# -*- coding: utf-8 -*-
"""a_star_tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GK7ya4Si6HNd4ds0u3XaQlrZzqi0avl9
"""

# -*- coding: utf-8 -*-
"""a_star_tree

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hujGW8WcdclJ8MjqNkPaRM8E5MqgU6fw
"""

# -*- coding: utf-8 -*-
"""a_star_tree

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i5a9mF6vbdRh6DTJ3qwblQAvs3KWMa28
"""

from queue import PriorityQueue

#Fungsi untuk algoritma A* Tree Search
def a_start_search(graph, start, goal, heuristic):
    frontier = PriorityQueue() #antrian prioritas untuk menyimpan simpul dan dieksplorasi
    frontier.put((0, start)) #menambahkan simpul awal ke dalam antrian dengan nilai prioritas 0
    explored = set() #set untuk menyimpan simpul yang sudah dieksplorasi

    while not frontier.empty():
        priority, current_node = frontier.get()

        if current_node == goal:
            print("Simpul tujuan sudah ditemukan")
            return True

        explored.add(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in explored:
                priority = heuristic[neighbor] + graph[current_node][neighbor]
                frontier.put((priority, neighbor))

    print("Simpul tujuan tidak ditemukan!")
    return False

heuristic = {
    'A' : 9,
    'B' : 4,
    'C' : 2,
    'D' : 5,
    'E' : 3,
    'F' : 7,
    'G' : 0
}

graph = {
    'S': {'A': 3, 'E': 2},
    'A': {'B': 3, 'C': 4},
    'B': {'D': 5},
    'C': {'D': 7},
    'D': {'G': 3},
    'E': {'D': 6}
}


start_node = 'S'
goal_node = 'G'

a_start_search(graph, start_node, goal_node, heuristic)