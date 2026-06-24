rows=4
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()