import itertools
a_list = list(range(5))

print("------------Zipping------------")
another_list = [str(element) for element in reversed(a_list)]
zip_list = list(zip(a_list, another_list))
print("Zipped list with another list {0}".format(zip_list))


print("------------Cartesian Product------------")
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
small_deck = list(zip(vals, suits))
print("Not what we want {0}".format(small_deck))

good_deck = list(itertools.product(suits, vals))
print("Now we talk. Size of deck {0}. {1}".format(len(good_deck),good_deck))

print("------------Grouping------------")
print("Grouped deck by suit:")
for suit,sub_deck in itertools.groupby(good_deck, lambda x: x[0]):
    print("\tSuit: {0}. Values: {1}".format(suit,list(sub_deck)))


print("------------Unzipping------------")
def some_function(arg1, arg2, arg3, **kwargs):
    print("({0},{1},{2})".format(arg1,arg2, arg3))
    print("Extra: ({0})".format(kwargs))


list_of_args = [0,6,-34]
some_function(*list_of_args)

a_dict = {
    "arg4": "Extra",
    "arg5": "Argument",
    "arg6": 23
}
some_function(*list_of_args, **a_dict)