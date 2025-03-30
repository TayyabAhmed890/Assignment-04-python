# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

list_num:list[int] = [2,3,4,5]

for num in range(len(list_num)):
    index = list_num[num]
    list_num[num] = index * 2


print(list_num)

