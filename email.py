email=input("Enter your emails: ")
position=email.find("@")
username=email[0:position]
print(username.upper())