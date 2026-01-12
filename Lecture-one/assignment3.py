# - Create a list of 5 animals called zoo
#
# - Delete the animal at the 3rd index.
#
# - Append a new animal at the end of the list
#
# - Delete the animal at the beginning of the list.
#
# - Print all the animals
#
# - Print only the first 3 animals


zoo_list = ["lion", "tiger" , "elephant", "snake" , "peacock"]
print(zoo_list)
zoo_list.pop(3)
print(zoo_list)
zoo_list.append("zebra")
print(zoo_list)
#
# for x in zoo_list:
#     print(x)

zoo_list.pop(0)
print(zoo_list)

print(zoo_list[0:3])