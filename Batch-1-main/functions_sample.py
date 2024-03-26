num = 4
facto = 1
while num != 1 :
    facto = facto*num
    num = num-1   
print(facto)    
print("**********************")
#**********************    
facto1 = 1   
num2 = 5
for i in range(1,num2): 
    facto1 = facto1 * i
print(facto1)
#********************** 
print("**********************")

def factorial(num):
    if num < 0:
        print("the number is a negative integer")
        return num
    if num == 1:
        return 1
    return num*factorial(num-1)

factorial_value = factorial(-4)
print(factorial_value)



