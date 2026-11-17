python_students={"Aman", "Rohit","Priya","Raj"}
java_students={"Priya","Raj","Ankit","neha"}
print("Both",python_students.intersection(java_students))
print("only python",python_students.difference(java_students))
print("only java",java_students.difference(python_students))
print("total unique",python_students.union(java_students))