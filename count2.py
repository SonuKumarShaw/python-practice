def count_char(n):
    if n == "":
        return 0
    else:
        return 1+count_char(n[1:])
print(count_char("Sonu"))
