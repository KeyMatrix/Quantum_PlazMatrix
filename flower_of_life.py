import matplotlib.pyplot as plt
import numpy as np

# 🔹 Генерация узлов цветка жизни
def generate_flower_of_life(radius, layers):
    points = [(0, 0)]  # Центральный узел
    for layer in range(1, layers + 1):
        for angle in np.linspace(0, 2 * np.pi, layer * 6, endpoint=False):
            x = radius * layer * np.cos(angle)
            y = radius * layer * np.sin(angle)
            points.append((x, y))
    return points

# 🔸 Визуализация
def plot_flower_of_life(points, links=None):
    plt.figure(figsize=(8, 8))
    for (x, y) in points:
        circle = plt.Circle((x, y), 0.5, color='lightblue', fill=True)
        plt.gca().add_artist(circle)
    if links:
        for i, j in links:
            x_values = [points[i][0], points[j][0]]
            y_values = [points[i][1], points[j][1]]
            plt.plot(x_values, y_values, color='gray', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("KeyMatrix: Sacred Geometry Nodes")
    plt.show()

# 🌀 Узлы и связи
radius = 1
layers = 3
nodes = generate_flower_of_life(radius, layers)
links = [(0, i) for i in range(1, len(nodes))]  # Связи от центра к каждому узлу
plot_flower_of_life(nodes, links)