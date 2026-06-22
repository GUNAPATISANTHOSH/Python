# Find the count of numbers greater than 20.
nums = [12, 45, 7, 89, 23, 45]
count=0
for num in nums:
    if num>20:
        count+=1
print(count)