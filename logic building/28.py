s = "Python1234"
count=0
for ch in s:
    if ch in "1,2,3,4,5":
        count+=1
print(count)