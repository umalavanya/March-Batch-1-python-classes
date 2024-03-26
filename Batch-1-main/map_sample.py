def square(num):
    return num**2

values = [ 7,3,5,7,9,17,22] 

square_list = []
for i in values:
    square_list.append(square(i))

square_list_map = list(map(square,values))

print(values)
print(f"with for loop: {square_list}")
print(f"with map: {square_list_map}")