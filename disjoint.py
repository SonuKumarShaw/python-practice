set1=set(map(int,input("enter the elements:").split()))
set2=set(map(int,input("enter the elements:").split()))
if set1.isdisjoint(set2):
    print("the sets are disjint")
else:
    print("The sets are not disjoint")