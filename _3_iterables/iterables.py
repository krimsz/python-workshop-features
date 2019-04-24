print("Let's create and manipulate a list, set and tuple from scratch")
a_list = ["something"]
a_set = {"something"}
a_tuple = ("something",)

print("----------------------")
print("The list is: {0}".format(a_list))
print("The set is: {0}".format(a_set))
print("The tuple is: {0}".format(a_tuple))

print("----------------------")
a_list.append(12)
a_set.add(12)
# a_tuple.append(12) # NOPE
print("The list after adding a number: {0}".format(a_list))
print("The set after adding a number: {0}".format(a_set))

print("----------------------")
a_list.append("Hello")
a_set.add("Hello")
# a_list.append("Hello") # NOPE
print("The list after adding a string: {0}".format(a_list))
print("The set after adding a string: {0}".format(a_set))

print("----------------------")
a_list.append("Hello")
a_set.add("Hello")
# a_list.append("Hello") # NOPE
print("The list after adding the same string: {0}".format(a_list))
print("The set after adding the same string: {0}".format(a_set))

print("----------------------")
a_list.remove("Hello")
a_set.remove("Hello")
# a_list.append("Hello") # NOPE
print("The list after removing the string: {0}".format(a_list))
print("The set after removing the string: {0}".format(a_set))


print("----------------------")
a_list.remove("Hello")
# a_set.remove("Hello") # NOPE
# a_list.append("Hello") # NOPE
print("The list after removing the string: {0}".format(a_list))
