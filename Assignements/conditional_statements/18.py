a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
min= a if a > b and a > c else b if b > c else c
print(min)