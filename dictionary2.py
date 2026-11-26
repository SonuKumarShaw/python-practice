marks={}
n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("enter the name: ")
    mark=int(input("Enter the marks: "))
    marks[name]=mark
topper=max(marks,key=marks.get)
print("marks",marks)
print("topper:",topper)
print("marks Scored:", marks[topper])