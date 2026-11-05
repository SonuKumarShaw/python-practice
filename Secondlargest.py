def Second_Largest(numbers):
    numbers=sorted(set(numbers))
    return numbers[-2]
numbers=list(map(int,input("enter the numbers:").split()))
print("Second largest number is:",Second_Largest(numbers))