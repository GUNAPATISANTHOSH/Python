#Find the second largest number.
nums = [4, 2, 8, 1, 9,9,3]
second=list(set(nums))
second.sort()
print(second[-2])