n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

c=input("Enter the operation (+,-,*,/):")

result=0
if c=="+":
    result=n1+n2

elif c=="-":
    result=n1-n2

elif c=="*":
    result=n1*n2

elif c=="/":
    result=n1/n2

print(n1,c,n2, ":",result)


