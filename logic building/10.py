# Can you write the code for counting how many times 45 appears?
nums = [12, 45, 7, 89, 23, 45]
count = 0
for num in nums:
    if num==45:
        count +=1
print(count)