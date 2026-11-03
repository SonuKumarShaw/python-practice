a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
def largest_of_three(a,b,c):
    if a>b and a>c:
        print("a is the largest number")
    elif b>a and b>c:
        print("b is the largest number")
    else:
        print("c is the largest number")
print(largest_of_three(a,b,c))