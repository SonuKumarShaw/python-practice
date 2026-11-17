list1=list(map(int,input("Enter the elements:").split()))
seen=set()
duplicates=set()
for items in list1:
    if items in seen:
        duplicates.add(items)
    else:
        seen.add(items)
print("Duplicates elements:",duplicates)
 