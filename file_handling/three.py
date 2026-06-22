# # file = open("1.txt", "a")
# # file.write("\nFastAPI")
# # file.close()

# # file = open("1.txt", "r")
# # print(file.read())
# # file.close()

# import os
# print(os.getcwd())
with open("1.txt", "r") as file:
    for line in file:
        print(line.strip())




        