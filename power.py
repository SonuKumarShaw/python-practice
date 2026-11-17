def pow_of_2(n):
    if n==0:
        return 1
    else:
        return 2 * pow_of_2(n-1)
print(pow_of_2(3))