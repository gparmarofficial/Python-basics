empty_list = []
print("Empty list:", empty_list)

my_list = [10 , 20 , 30]
print("List with elements:",my_list)

repeated_list = my_list * 2
print("Repeated list:", repeated_list)


print("Reversed list:", my_list[::-1])

#activity2
words = ["abc" , "xyz" , "aba" , "1221", "a" , "aa"]
count = 0
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
        
print("Number of matching strings:", count)

#activity3
numbers = [4, 13 , 17 , 29 , 5]
total_sum = sum(numbers)
average = total_sum / len(numbers)

largest = max(numbers)
smallest = min(numbers)

print("list:",numbers)
print("Sum:", total_sum)
print("Average:", average)
print("Largest number", largest)
print("smallest number:", smallest)