age=int(input("Enter the age"))
if age<18:
    raise ValueError("age must be greater than 18")
print("access granted")