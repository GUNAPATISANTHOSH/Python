a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
max= a if a < b and a < c else b if b < c else c
print(max)