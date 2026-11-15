number=list(map(int,input("Enter the numbers:").split()))
if number==sorted(number):
    print("The list is sorted")
else:
    print("The list is not sorted")