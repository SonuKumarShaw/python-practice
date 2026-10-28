a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
op=input("Enter the operator (+,-,*,/)")
match op:
     case "+":
         print(a+b)
     case  "-":
         print(a-b)
     case "*":
         print(a*b)
     case "/":
         print(a/b)
     case _:
         print("Invalid Case")