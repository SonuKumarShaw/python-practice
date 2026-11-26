contact={}
n=int(input("enter the numbers of contact: "))
for i in range(n):
    name=input("enter the names: ")
    phone=int(input("enter the phone number: "))
    contact[name]=phone
search_name=input("Enter the contct to be search: ")
if search_name in contact:
    print("Phone Number: ",contact[search_name])
else:
    print("contact not found: ")