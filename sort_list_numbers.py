"""
File: sort_list_numbers.py
Author: Dallin Williams

Purpose: Put numbers in lists and sort them.
"""

print()
print("Enter a list of numbers.\nType 0 when finished.")

numbers = []
number = -1

while number != 0:
    print()
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

sum = 0

for number in numbers:
    sum += number

print()
print(f"The sum is: {sum}")

count = len(numbers)
average = sum / count

print()
print(f"The average is: {average}")

best = -1

for number in numbers:
    if number > best:
        best = number

print()
print(f"The largest number is: {best}")

smallest = 99999999999

for number in numbers:
    if number > 0 and number < smallest:
        smallest = number

print()
print(f"The smallest positive number is: {smallest}")

sorted = sorted(numbers)

print()
print("The sorted list is: ")
for number in sorted:
    print(number)
 
print()