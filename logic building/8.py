#find the largest even number
nums = [5, 12, 8, 3, 15, 10]

largest_even = 0
for num in nums:
    if num%2==0:
        if num>largest_even:
            largest_even=num
print(largest_even)