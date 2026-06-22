# Find how many even numbers are present.
nums = [10, 15, 20, 25, 30, 35]
count=0
for num in nums:
    if num % 2==0:
        count +=1;
print(count)