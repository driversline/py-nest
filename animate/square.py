import os
import math
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_cube(a, b):
    vertices = [[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
                [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    
    height, width = 20, 40
    screen = [[' ' for _ in range(width)] for _ in range(height)]
    z_buffer = [[-float('inf')] * width for _ in range(height)]

    for edge in edges:
        v1, v2 = vertices[edge[0]], vertices[edge[1]]
        x_proj1, y_proj1, z_proj1 = project_vertex(*rotate_vertex(*v1, a, b), width, height)
        x_proj2, y_proj2, z_proj2 = project_vertex(*rotate_vertex(*v2, a, b), width, height)
        draw_line(screen, z_buffer, x_proj1, y_proj1, z_proj1, x_proj2, y_proj2, z_proj2)

    clear_screen()
    print('\n'.join(''.join(row) for row in screen))

def rotate_vertex(x, y, z, a, b):
    x_rotated = x * math.cos(b) - z * math.sin(b)
    z_rotated = x * math.sin(b) + z * math.cos(b)
    y_rotated = y * math.cos(a) - z_rotated * math.sin(a)
    return x_rotated, y_rotated, y * math.sin(a) + z_rotated * math.cos(a)

def project_vertex(x, y, z, width, height):
    factor = 3 / (3 + z)
    return int(width / 2 + width / 4 * factor * x), int(height / 2 - height / 4 * factor * y), z

def draw_line(screen, z_buffer, x1, y1, z1, x2, y2, z2):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx, sy = (1 if x1 < x2 else -1), (1 if y1 < y2 else -1)
    err = dx - dy

    while True:
        if 0 <= x1 < len(screen[0]) and 0 <= y1 < len(screen):
            if z1 > z_buffer[y1][x1]:
                z_buffer[y1][x1] = z1
                screen[y1][x1] = '/'

        if x1 == x2 and y1 == y2:
            break
        err2 = err * 2
        if err2 > -dy:
            err -= dy
            x1 += sx
        if err2 < dx:
            err += dx
            y1 += sy

def main():
    a, b = 0, 0
    while True:
        draw_cube(a, b)
        a += 0.05
        b += 0.1
        time.sleep(0.1)

if __name__ == "__main__":
    main()
