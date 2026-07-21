def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2

try:
    val1 = float(input("Enter first number:"))
    op = input("Enter operator (+ , -, *, /, )")
    val2 = float(input("Enter  second number:"))
    
    if op == "+":
        print("Result:", add(val1 , val2))
    elif op == "-":
        print("Result:", subtract(val1 , val2))
    elif op == "*":
        print("Result:", multiply(val1 , val2))
    elif op == "/":
        print("Result:", divide(val1 , val2))
    else:
        print("Invalid operator entered")
        
except ZeroDivisionError:
    print("Error : Cannot divide by Zero!")
    
except ValueError:
    print("Error: Please enter numbers only!")
    