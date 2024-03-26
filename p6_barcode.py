import matplotlib.pyplot as plt
import numpy as np

def name_to_binary_list(name):
    binary_list = []
    for char in name:
        # Convert character to ASCII value
        ascii_value = ord(char)
        # Convert ASCII value to binary representation
        binary_representation = bin(ascii_value)[2:]  # [2:] to remove '0b' prefix
        # Pad binary representation with leading zeros to make it 8 bits long
        padded_binary = binary_representation.zfill(8)
        # Append padded binary representation to the list as integers
        binary_list.extend([int(bit) for bit in padded_binary])
    return binary_list



def barcode_generator(code):
    
    pixel_per_bar = 4
    dpi = 100

    fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
    ax.set_axis_off()
    ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
    return None
    

# Example usage
name = "madhu"
binary_list = name_to_binary_list(name)
print(binary_list)
binary_name = np.array(binary_list)

code = np.array([
    1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

barcode_generator(code)
plt.show()
barcode_generator(binary_name)
plt.show()
