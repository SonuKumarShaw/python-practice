marks = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))
    marks[name] = mark

topper = max(marks, key=marks.get)

print("Marks:", marks)
print("Topper:", topper)
print("Marks scored:", marks[topper])