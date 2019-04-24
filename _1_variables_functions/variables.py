print("------------------------Types------------------------")
a_boolean = True
print("A boolean ({0}): [{1}]".format(type(a_boolean), a_boolean))

an_integer = 23
print("An integer({0}): [{1}]".format(type(an_integer), an_integer))

a_float = 23.2
print("A float({0}): [{1}]".format(type(a_float), a_float))

a_float_scientific_representation = 23.2e10
print("A float with scientific representation: [{0}]".format(a_float_scientific_representation))

a_complex_number = 2 + 3j
print("A complex number({0}): [{1}]".format(type(a_complex_number), a_complex_number))

a_binary_representation = 0b100
print("A binary representation: [{0}]".format(a_binary_representation))

an_octal_representation = 0o703
print("An octal representation: [{0}]".format(an_octal_representation))

an_hexadecimal_representation = 0xAB12
print("An hexadecimal representation({0}): [{1}]".format(type(an_hexadecimal_representation), an_hexadecimal_representation))

double_quoted_string = "Some String"
print("Double quoted string({0}: [{1}]".format(type(double_quoted_string), double_quoted_string))

a_dict = {
    "some_key": "some_value",
    "another_key": 2
    }
print("A dict({0}): [{1}]".format(type(a_dict), a_dict))

a_list = ["some_value", 2]
print("A list({0}): [{1}]".format(type(a_list), a_list))

print("------------------------Definitions------------------------")
single_quoted_string = 'Some other String'
print("Single quoted string: [{0}]".format(single_quoted_string))

easy_escaping = "This is Anna's script"
print("Single quotes in a string: [{0}]".format(easy_escaping))
another_easy_escaping = '"The lord of the rings" is a book'
print("Double quotes in a string: [{0}]".format(another_easy_escaping))


multiple_line_string_definition = "This is supposed to be something \n" \
                                  "long and that doesn't fit in the line"
print("A multiple line string definition: [{0}]".format(multiple_line_string_definition))

a_var = 23
print("A var ({0}): {1}".format(type(a_var), a_var))
a_var = "I'm a string now"
print("A var ({0}): {1}".format(type(a_var), a_var))
