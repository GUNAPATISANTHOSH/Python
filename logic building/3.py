#Find the largest number in a list without using sort() or max().
nums = [12, 45, 7, 89, 23]
largest =nums[0]
for num in nums:
    if num > largest:
        largest = num
print(largest)