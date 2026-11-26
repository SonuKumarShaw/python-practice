user={}
n=int(input("enter the number: "))
for i in range(n):
    username=input("Create the username: ")
    password=int(input("Create the password: "))
    user[username]=password
print("\n--- Login ---")
username=input("Enter the username: ")
password=int(input("Enter the password: "))
if username in user and user[username]==password:
    print("Login Successful")
else:
    print("Login Unsuccessful")
        