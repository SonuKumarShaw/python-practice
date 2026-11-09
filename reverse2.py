def reverse(numbers):
    return numbers[::-1]
numbers = list(map(int, input("enter the numbers:").split()))
print("the reversed list is:", reverse(numbers))
