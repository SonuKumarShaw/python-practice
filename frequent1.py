numbers=list(map(int,input("Enter the numbers:").split())
             )
frequent_numbers={}
for num in numbers:
    if num in frequent_numbers:
        frequent_numbers[num]+=1
    else:
        frequent_numbers[num]=1
print("The Frequency of the numbers is:",frequent_numbers)