# Text file handling
# Writing to a text file



























"""

with open("example.txt", "w") as text_file:
    text_file.write("Hello, this is a text file.\n")
    text_file.write("We can write multiple lines.\n")
    text_file.write("End of file.")

# Reading from a text file
with open("example.txt", "r") as text_file:
    content = text_file.read()
    print("Content of text file:")
    print(content)

# Binary file handling
# Writing to a binary file
with open("example.dat", "wb") as binary_file:
    binary_file.write(b"This is a binary file.\n")
    binary_file.write(b"It can contain any kind of data.\n")
    binary_file.write(b"End of file.")

# Reading from a binary file
with open("example.dat", "rb") as binary_file:
    content = binary_file.read()
    print("\nContent of binary file:")
    print(content.decode("utf-8"))  # Decode binary data to string for readability


"""