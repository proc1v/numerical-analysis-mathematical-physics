import json
import datetime
import numpy as np
import matplotlib.pyplot as plt

def create_rectangular_mesh(num_x_elements, num_y_elements):
    num_x = num_x_elements + 1
    num_y = num_y_elements + 1
   # Generate vertices
    x = np.linspace(0, 1, num_x)
    y = np.linspace(0, 1, num_y)
    vertices = np.array([(xi, yj) for yj in y for xi in x])

    # Generate triangles
    triangles = []
    for j in range(num_y_elements):
        for i in range(num_x_elements):
            # Define the indices of the vertices for the current quad
            v0 = i + j * num_x
            v1 = v0 + 1
            v2 = v0 + num_x
            v3 = v2 + 1

            if (i + j == 0) or (i + j == (num_x_elements + num_y_elements) - 2):
                triangles.append([v0, v1, v3])
                triangles.append([v0, v3, v2])
            else:
                triangles.append([v0, v1, v2])
                triangles.append([v1, v3, v2])

    return vertices, np.array(triangles)


def calculate_triangle_area(vertices, triangle):
    # Extract vertices of the triangle
    v0, v1, v2 = vertices[triangle]

    # Calculate the area using the shoelace formula
    area = 0.5 * abs((v0[0] * (v1[1] - v2[1]) + v1[0] * (v2[1] - v0[1]) + v2[0] * (v0[1] - v1[1])))

    return area


def save_to_json(vertices, triangles, filename):
    triangle_data = []

    for i, triangle in enumerate(triangles):
        triangle_area = calculate_triangle_area(vertices, triangle)
        triangle_info = {
            "Triangle": i,
            "Vertices": dict(zip(triangle.tolist(), vertices[triangle].tolist())),
            "Area": triangle_area
        }
        triangle_data.append(triangle_info)

    with open(filename, 'w') as json_file:
        json.dump(triangle_data, json_file, indent=4)


def plot_mesh(vertices, triangles):
    plt.figure(figsize=(5, 5))
    plt.triplot(vertices[:, 0], vertices[:, 1], triangles=triangles, color='b')
    plt.plot(vertices[:, 0], vertices[:, 1], 'o', color='r')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Triangulation')
    plt.show()


if __name__ == "__main__":
    #num_x = 10  # Initial number of x elements
    #num_y = 5  # Initial number of y elements

    while True:
        user_input = input("Enter the new number of x and y elements (comma-separated, or 'q' to quit): ")
        if user_input.lower() == 'q':
            break

        try:
            num_x, num_y = map(int, user_input.split(','))
        except ValueError:
            print("Invalid input. Please enter positive integers separated by a comma or 'q' to quit.")
        break

    print(f"Creating triangulation with {num_x} x and {num_y} y elements...")
    vertices, triangles = create_rectangular_mesh(num_x, num_y)
    plot_mesh(vertices, triangles)
    
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Save vertices, triangles, and their areas to the same text file
    save_to_json(vertices, triangles, f"triangulation.json")
