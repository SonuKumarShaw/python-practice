students=list(map(str,input("Enter the names of the students:").split()))
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3.Display Students")
    print("4.Exit")
    choice=input("Enter the choice:")
    if choice=="1":
        name = input("Enter the name of the student:")
        students.append(name)
        print("student addes Successfully")
    elif choice=="2":
        name=input("Enter the name of the student:")
        if name in students:
            students.remove(name)
            print("Student removed Successfully")
        else:
            print("Student not found")
    elif choice=="3":
        if len(students)==0:
            print("no student fpund")
        else:
            print("list of the students:")
            for student in students:
                 print(students)
    elif choice=="4":
        print("Exit")
        break
    else:
        print("Invalid choice")
                
    