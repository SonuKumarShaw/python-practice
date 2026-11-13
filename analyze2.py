numbers=list(map(int,input("Enter the numbers:").split()))

largest=numbers[0]
    
for num in  numbers:
        
        if num>largest:
            largest=num
            print("The largest number is:",largest[numbers])
smallest=numbers[0]
for num in numbers:
    if num<smallest:
        smallest=num
print("The smallest number is:",smallest[numbers])
for num in numbers:
    sum=0
    sum+=num
print("The sum of the numbers is:",sum)
for num in numbers:
    even_count=0
    if num%2==0:
        even_count+=1
print("The even numbers are:",numbers)
for num in numbers:
    odd_count=0
    if num%2 !=0:
        odd_count+=1
print("The odd numbers are:",numbers)
print(analyze(numbers))
    