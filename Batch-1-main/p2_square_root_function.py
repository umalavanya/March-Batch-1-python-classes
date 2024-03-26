def square_root(number):
    guess = number / 2.0  

    while abs(guess * guess - number) > 1e-10:
        guess = 0.5 * (guess + number / guess)

    return guess


if __name__ == "main" :
    number = float(input("Enter a number to calculate its square root: "))
    result = square_root(number) 
    print(f"The square root of {number} is approximately \n {result:.4f}")
