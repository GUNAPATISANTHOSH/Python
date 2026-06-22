# Find the smallest number in the list:
nums = [12, 45, 7, 89, 23]
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
print(smallest)