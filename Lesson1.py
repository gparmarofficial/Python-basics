def wishes():
    print("hello, how are u!")

wishes()

# activity2
def weather():
    print("autum:cool and windy")
    print("spring: warm and sunny")
    
weather()

# activity3
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

choise = input("Enter +, -, *, or / : ")
num1 = float(input("First number:"))
num2 = float(input("Second number:"))

if choise == "+":
    add(num1,num2)
if choise == "-":
    sub(num1,num2)
if choise == "*":
    mul(num1,num2)
if choise == "/":
    div(num1,num2)