num=int(input("Enter the Numbers: "))
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
    else:
        print("Is Prime")
         