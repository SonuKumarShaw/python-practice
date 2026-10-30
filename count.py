n=int(input("Enter the number: "))
if n==0:
    count=1
else:
    count=0
    while n!=0:
        count+=1
        n=n//10
print("the number is: ",count)