name_list=input("Enter the list: ").split()
search_name=input("enter the name")
for name in name_list:
    if name.lower()==search_name.lower():
        print("name Found")
        break
else:
    print("not found")