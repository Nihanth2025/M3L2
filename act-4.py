def emp(name):
    return name

def sal(exp):
    if exp>5:
        return 300000
    elif exp>3:
        return 250000
    else:
        return 80000

print("Employe name:",emp("Nihanth"))
print("Salary=",sal(4))
print("Welcome to company")