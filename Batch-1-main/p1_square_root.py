# Calculate square root without using any built-in functions

number_str = input("Enter a number to calculate its square root: ")
number = float(number_str)


guess = number / 2.0  

while abs(guess * guess - number) > 1e-10:
    guess = 0.5 * (guess + number / guess)


print(f"The square root of {number} is approximately \n {guess:.4f}")
