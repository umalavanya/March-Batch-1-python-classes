import random

def random_float(min_value, max_value):
    return round(random.uniform(min_value, max_value), 5)  # Round to 5 decimal places

# Function to generate a 5x5 matrix of random floating-point values
def generate_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = [random_float(0, 100) for _ in range(columns)]
        matrix.append(row)
    return matrix

# Function to write the matrix to a text file with 5 decimal places formatting
def write_to_file(matrix, filename):
    with open(filename, "w") as file:
        for row in matrix:
            row_str = "\t".join("{:.8f}".format(value) for value in row)  # Format each value to have 5 decimal places
            file.write(row_str + "\n")  # Write row to file, append newline

# Generate a 5x5 matrix of random floating-point values
matrix = generate_matrix(5, 5)

# Write the matrix to a text file with 5 decimal places formatting
write_to_file(matrix, "random_values_formatted.txt")

print("File 'random_values_formatted.txt' generated successfully.")
