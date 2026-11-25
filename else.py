nums=list(map(int,input("Enter the numbers: ").split()))
for num in nums:
    if num==7:
        print("Found")
        break
    else:
        print("Not found")