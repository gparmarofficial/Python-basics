ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
else:
    print("Not Alphabet")
    
#hmrkcheckage
age = int(input())

if age >= 10 and age <= 20:
    print("Between 10 and 20")
else:
    print("Not between 10 and 20")
    
#hmrkpowercalculater

num = int(input("Enter number: "))
n = int(input("Enter power: "))

result = 1

for i in range(n):
    result = result * num

print("Answer =", result)
