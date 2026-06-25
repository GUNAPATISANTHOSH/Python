rows=4
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    for j in range(2*(rows-i)):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(3,0,-1):
    for j in range(i):
        print("*",end=" ")
    for j in range(2*(rows-i)):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()