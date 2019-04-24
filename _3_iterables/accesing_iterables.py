a_list = list(range(23))

print("The list: {0}".format(a_list))
# By index
print("Index: {0}".format(a_list[4]))

# By negative index
print("Negative index: {0}".format(a_list[-1]))

# Slicing
print("By slice [1:5]: {0}".format(a_list[1:5]))

print("By slice [:5]: {0}".format(a_list[:5]))
print("By slice [5:]: {0}".format(a_list[5:]))

print("By step [::2]: {0}".format(a_list[::2]))

print("By slice and step [6:20:2]: {0}".format(a_list[6:20:2]))

print("Negative index step [::-1]: {0}".format(a_list[::-1]))
