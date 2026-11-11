t=(1,2,3,2,4,5,3,6)
duplicate=set()
for num in t:
   if t.count(num)>1:
       duplicate.add(num)
print(duplicate)