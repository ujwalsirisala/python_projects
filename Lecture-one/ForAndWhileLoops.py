
# for loop and while loop

# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])


# for iterator in my_list:
#     print(iterator)
# for x in my_list:
#     print(x)

# sum_of_for_loop = 0
# for x in my_list:
#     sum_of_for_loop += x
# print(sum_of_for_loop)


# my_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
#
# for x in my_list:
#     print(f"happy {x}!")


# while loop

# x = 0
#
# while x < 10 :
#     x += 1
#     print(x)


x = 0

while x < 10 :
    x += 1
    if x == 6:
        continue
    if x == 7:
        break
    print(x)
else:
    print("x is now larger or equal to 10")

