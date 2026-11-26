n=int(input("Enter the number of key_value: ")
      )
d={}
for i in range(n):
    key=input("enter key: ")
    value=int(input("enter the value: "))
    d[key]=value
reverse_d={}
for key, value in d.items():
    reverse_d[value]=key
print("original Dictionary: ",d)
print("Reverse Dictionary: ",reverse_d)