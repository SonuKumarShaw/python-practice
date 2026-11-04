def sum(numbers):
    total=0
    for n in numbers:
        total+=n
    return total
numbers=list(map(int,input("enter the numbers:").split()))
print("sum of the numbers:",sum(numbers))