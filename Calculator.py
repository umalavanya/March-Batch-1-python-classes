# Our Calculator

#Addition
def add(num1,num2):
    return num1+num2

#Subtraction
def sub(num1,num2):
    return num1-num2

#Multiplication
def mul(num1, num2):
    return num1*num2

#Division
def divi(num1, num2):
    return num1/num2

operations = {
    "+":add, 
    "-":sub, 
    "*":mul,
    "/":divi
    }

final = "n"

num1 = float(input("Enter your first number:"))

function_operation = input("Enter your operation: ")

num2 = float(input("Enter your second number: "))

function_name = operations[function_operation]

result = function_name(num1,num2)

print(result)

final = input("Do you want to quit? (y/n)")

while final != 'y' : 
     
    num1 = result
    function_operation = input("Enter your operation: ")
    num2 = float(input("Enter your second number: "))
    function_name = operations[function_operation]
    result = function_name(num1,num2)
    print(result)
    final = input("Do you want to quit? (y/n)")
    
print(f"final result:  {result}")