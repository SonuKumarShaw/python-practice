def analyze(numbers):
    largest=0
    smallest=0
    sum=0
    for num in numbers:
        if num>largest:
            largest=num
    print("the Largest number is:",largest)
    for num in numbers:
        if num<smallest:
            smallest=num
    print("the smallest number is:",smallest)
    for num in numbers:
        sum+=num
    print("the sum of the numbers is:",sum)
    for num in numbers:
        average=sum/len(numbers)
    print("the average of the numbers is:",average)
numbers=list(map(int,input("Enter the numbers:").split()))   
print(analyze(numbers))        