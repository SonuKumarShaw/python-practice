# n=int(input("enter the Number: "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         cout+=1
#     if count==2:
#         print("The Number is prime ")
#     else:
#         print("The Number is not prime")
n = int(input("Enter a number: "))

is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime and n > 1:
    print("Prime Number")
else:
    print("Not a Prime Number")