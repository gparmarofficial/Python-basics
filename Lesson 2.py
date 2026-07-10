#activiy1
num = int(input("Enter a maximum number:"))

total_sum = 0

for i in range(1, num +1 ):
    total_sum +=i
    
print ("the sum of wholenumbers up to" , total_sum)

#activity2
text = input("Enter a string: ")
print(text[::-1])

#activity3
num = int(input("Enter a number: "))

while num >= 1:
    print(num)
    num = num - 1