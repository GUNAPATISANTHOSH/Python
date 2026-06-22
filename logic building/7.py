# # # Find the Second Largest Number (without sort)
# # nums = [12, 45, 7, 89, 23]
# # largest = nums[0]
# # second_largest = float('-inf')

# # for num in nums:
# #     if num > largest:
# #         second_largest = largest
# #         largest = num
# #     elif num > second_largest and num != largest:
# #         second_largest = num
# # print(second_largest)
# nums = [12, 45, 7, 89, 23]
# total=0
# for num in nums:
#     total+=num;
# print(total)
nums = [5, 12, 8, 3, 15, 10]
total=0
for num in nums:
    if num%2==0:
        total+=num
print(total)