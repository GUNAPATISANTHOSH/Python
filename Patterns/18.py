# # # # solid square
# # # rows=4
# # # for i in range(rows):
# # #     for j in range(rows):
# # #         print("*",end=" ")
# # #     print()
# # # hollow square
# # rows=4
# # for i in range(rows):
# #     for j in range(rows):
# #         if i==0 or i==rows-1 or j==0 or j==rows-1:
# #             print("*",end=" ")
# #         else:
# #             print(" ",end=" ")
# #     print()

# # Increasing triangle
# rows =4
# for i in range(1,rows+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# Diamond
# rows=4
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()
# for i in range(3,0,-1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()
rows=4
columns=3
for i in range(rows):
    for j in range(columns):
        if i==0 or i==rows-1 or j==0 or j==columns-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()