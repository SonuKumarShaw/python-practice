numbers=list(map(int,input("Enter the numbers:").split()))
unique_numbers=set(numbers)
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("The unique numbers are:", unique_numbers)