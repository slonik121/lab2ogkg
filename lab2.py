import os
import matplotlib.pyplot as plt

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

def plot_points(points, output_path, canvas_size=(960, 540)):
    """
    Plots the given points and saves the result.
    """
    plt.figure(figsize=(canvas_size[0] / 100, canvas_size[1] / 100), dpi=100)
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, c='blue', s=5)
    plt.title("Visualization of Points")
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

    try:
        # Read coordinates
        print("Reading coordinates...")
        points = read_coordinates(input_file)

        # Choose the file format
        output_file = save_file_in_format(output_file_base)

        # Generate the plot
        print("Generating the plot...")
        plot_points(points, output_file)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()