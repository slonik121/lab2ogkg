import os
import matplotlib.pyplot as plt
import math

def read_coordinates(file_path):
    """
    Reads coordinates from a file and returns a list of points.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")

    points = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                x, y = map(int, line.strip().split())
                points.append((x, y))
            except ValueError:
                print(f"Invalid line format: {line.strip()}. Skipping.")
    print(f"Successfully read {len(points)} points.")
    return points

def calculate_rotation_matrix(alpha_deg, center=(480, 480)):
    """
    Calculates the rotation matrix for rotating around a given point (center).
    """
    alpha_rad = math.radians(alpha_deg)  # Convert degree to radians
    cos_alpha = math.cos(alpha_rad)
    sin_alpha = math.sin(alpha_rad)

    # Rotation matrix M
    rotation_matrix = [
        [cos_alpha, -sin_alpha],
        [sin_alpha, cos_alpha]
    ]
    
    # Translation vector to shift points to origin and back
    translation_vector = center
    return rotation_matrix, translation_vector

def apply_affine_transformation(points, rotation_matrix, center):
    """
    Applies affine transformation (rotation) to the points based on the rotation matrix.
    """
    transformed_points = []
    for (x, y) in points:
        # Shift point to origin, apply rotation, then shift back
        x_new = rotation_matrix[0][0] * (x - center[0]) + rotation_matrix[0][1] * (y - center[1]) + center[0]
        y_new = rotation_matrix[1][0] * (x - center[0]) + rotation_matrix[1][1] * (y - center[1]) + center[1]
        transformed_points.append((x_new, y_new))
    return transformed_points

def save_file_in_format(output_path, supported_formats=("jpg", "svg", "pdf", "png")):
    """
    Saves the plot in the chosen format based on user input (1, 2, 3, 4).
    """
    print("Choose a format for the output file:")
    for i, format in enumerate(supported_formats, 1):
        print(f"{i}. {format}")
    
    while True:
        try:
            choice = int(input("Enter a number (1-4): "))
            if 1 <= choice <= 4:
                return f"{output_path}.{supported_formats[choice - 1]}"
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def plot_points(points, output_path, canvas_size=(960, 960)):
    """
    Plots the given points and saves the result.
    """
    plt.figure(figsize=(canvas_size[0] / 100, canvas_size[1] / 100), dpi=100)
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, c='blue', s=5)
    plt.title("Visualization of Rotated Points")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.axis('equal')

    try:
        plt.savefig(output_path)
        print(f"Plot successfully saved to file: {output_path}")
    except Exception as e:
        print(f"Error saving the plot: {e}")
    finally:
        plt.close()

def main():
    # Specify the input file
    input_file = r"C:\Users\Lenovo\Desktop\lab2\DS7.txt"
    output_file_base = "result"

    # Last digit of login, n = 9
    n = 9
    alpha_deg = 10 * (n + 1)  # Calculate the rotation angle

    try:
        # Read coordinates
        print("Reading coordinates...")
        points = read_coordinates(input_file)

        # Calculate rotation matrix and apply the affine transformation
        rotation_matrix, center = calculate_rotation_matrix(alpha_deg)
        print(f"Rotation angle: {alpha_deg} degrees")

        # Apply the affine transformation
        rotated_points = apply_affine_transformation(points, rotation_matrix, center)

        # Choose the file format
        output_file = save_file_in_format(output_file_base)

        # Generate the plot
        print("Generating the plot...")
        plot_points(rotated_points, output_file)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
