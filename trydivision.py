try:
    a=int(input("Enter the Number: "))
    b=int(input("Enter the Number: "))
    print(a/b)
except ZeroDivisionError:
    print("cannnot Divide Zero!")