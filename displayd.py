def student(name,maths,science,english):
 """Generation and display,s of the student report card"""
 total=maths+science+english
 percentage=total/3
 print("-----REPORT CARD------")
 print(f"Name: {name}")
 print(f"maths:{maths}")
 print(f"science: {science}")
 print(f"english: {english}")
 print()
 print(f"total:{total}")
 print(f"precentage:{percentage:.2f}%")
student("Sonu",99,98,97)
print("\nDocstring")
print(student.__doc__)
 
 