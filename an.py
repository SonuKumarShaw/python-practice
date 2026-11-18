numbers = list(map(int, input("Enter the numbers: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("The smallest number is:", smallest)

total = 0

for num in numbers:
    total += num

print("The sum of the numbers is:", total)

even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1

print("The number of even numbers is:", even_count)

odd_count = 0

for num in numbers:
    if num % 2 != 0:
        odd_count += 1

print("The number of odd numbers is:", odd_count)