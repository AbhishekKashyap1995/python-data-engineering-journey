#simple function
def helloWorld():
    print("Hello World")

helloWorld() # calling function

# Function with parameter
def sayHello(name):
    print(name)    

sayHello("Abhishek") # calling function

# function with parameters and sarguments with return
def sum(num1, num2):
    return num1 + num2

print(sum(10,20)) # calling function

#lambda function
multiply = lambda x : x * 10

print(multiply(10))

# Recursion function

def countdown(n):
    if n == 0:
        return 
    print(n)
    countdown(n-1)

countdown(3)    