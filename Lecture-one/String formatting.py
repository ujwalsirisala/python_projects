
# String formatting

first_name = "ujwal"
# print(first_name)
#
# print("hi" + first_name)
#
# # below code gives the space between the two words.
# print("hi " +first_name)

print(f"hi {first_name}")
print("hi{first_name}")

sentence = "hi {} "
print(sentence.format(first_name ))


sentence = "hi {} {} "
last_name = "sirisala"
print(sentence.format(first_name , last_name ))


print(f"hi {first_name} {last_name} i hope you are learning well")