# Python code to find the sum of negative numbers:
nums = [5, -2, 10, -8, 7, -1, 3]
total=0
for num in nums:
    if num<0:
        total+=num
print(total)