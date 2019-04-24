print("------------------------Functions------------------------")


def a_function():
    print("Hey, it's me!!")

a_function()


def a_function_with_args(some_arg):
    print("--------Function--------")
    print("My attr ({0}): {1}".format(type(some_arg), some_arg))

a_function_with_args(1)
a_function_with_args("Another")

def a_function_with_default_args(some_arg, some_other_arg, optional_arg="hello"):
    print("--------Function Default Args--------")
    print("My attr1 ({0}): {1}".format(type(some_arg), some_arg))
    print("My attr2 ({0}): {1}".format(type(some_other_arg), some_other_arg))
    print("My attr3 ({0}): {1}".format(type(optional_arg), optional_arg))

a_function_with_default_args(23, 42)
a_function_with_default_args(23, "bye")
a_function_with_default_args(23, 32)
a_function_with_default_args(23, 45, optional_arg="bye")
# a_function_with_default_args(23, optional_arg="day") # fails

# Be careful with mutable arguments
def a_function_with_default_mutable_args(some_arg, optional_arg=[]):
    optional_arg.append(some_arg)
    print("--------Function Default Mutable Arg--------")
    print("My attr1 ({0}): {1}".format(type(some_arg), some_arg))
    print("My attr2 ({0}): {1}".format(type(optional_arg), optional_arg))

a_function_with_default_mutable_args(23)
a_function_with_default_mutable_args(45)


def a_function_with_extra_args(some_arg, **extra_args):
    print("--------Function Extra args--------")
    print("My attr1 ({0}): {1}".format(type(some_arg), some_arg))
    print("My attr2 ({0}): {1}".format(type(extra_args), extra_args))

a_function_with_extra_args(23, attr1=1)
a_function_with_extra_args(45, attr2=4, attr123123123=45)

