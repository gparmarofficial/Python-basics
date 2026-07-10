#activity1
num = 5
total = 0

while num > 0:
    total = total + num
    num = num - 1
    
print(total)

#activity2
#while True:
   # print("This is an infinite loop! press Ctrl+C to stop it.")
    
#activity3
n = int(input("Enter a number:"))
temp = n
total = 0

while temp > 0 :
    digit = temp % 10
    total +=digit ** 3
    temp //= 10

if n == total:
        print(total,"armstrong number")
    
else:
        print(total, "ts aint a armstrong number")
        