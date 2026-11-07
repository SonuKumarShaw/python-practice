def check(numbers):
    if numbers == sorted(set(numbers)):
        print("the list is sorted")
    else:
        print("the list is not sorted")
numbers=list(map(int,input("enter the numbers:").split()))
check(numbers)
