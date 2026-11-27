password=input("Enter the password")
if len(password)<4:
    raise ValueError("password is short")
print("Password Accepted")