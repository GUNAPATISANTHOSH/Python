rows=4
for i in range(1,rows+1):
    if i%2==0:
        num=1
    else:
        num=2
    for j in range(i,0,-1):
        print(j,end=" ")
        # num+=1
    print()