class AClass:

    attr1 = "Hello"
    def __init__(self):
        self.attr2 = "Bye Bye"

    @classmethod
    def a_class_method(cls):
        return "Hey, I'm a class method from the classs {0}".format(cls)
    @staticmethod
    def a_static_method():
        return "Hey, I'm a static method"

    def a_method(self):
        return self.attr2

an_instance = AClass()

print("-------Class Attributes-------")
print("Class attribute")
print(AClass.attr1)

print("-------Class/Static Methods-------")
print(AClass.a_static_method())
print(AClass.a_class_method())
print(an_instance.attr2)

print("-------Changing a class attribute-------")
AClass.attr1 = "Changed"
print(AClass.attr1)

print("-------Adding attrs to a class-------")
print(vars(AClass))
AClass.attr5 = "I'm a new attribute in the class"
print(AClass.attr5)
print(vars(AClass))

print("-------Calling a method-------")
print(an_instance.a_method())

print("-------Adding attributes to an instance-------")
print(vars(an_instance))
an_instance.some_other_attr = "I'm a new attribute in the instance"
an_instance.attr2 = "Bye"
print(vars(an_instance))
print(an_instance.some_other_attr)
