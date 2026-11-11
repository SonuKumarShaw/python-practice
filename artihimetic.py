def calculator(a,b):
    """Performs basic arithmetic operations."""
    print ( f"{a} + {b} = {a+b}")
    print  (f"{a} * {b} = {a*b}")
    print  (f"{a} - {b} = {a-b}")
    print (f"{a} / {b} = {a/b}")
print(calculator(10,5))
print(calculator.__doc__)