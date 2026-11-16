def SecondLargest(numbers):
    largest=-1
    second_largest=-1
    for num in numbers:
        if num > largest:
            second_largest=largest
            largest=num
        elif num > second_largest and num != largest:
            second_largest=num
    return second_largest
numbers=list(map(int,input("Enter the numbers: ").split()))

print(SecondLargest(numbers))