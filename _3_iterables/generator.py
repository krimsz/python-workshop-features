some_range = iter(range(10))
print("------------A generator doesn't return something we can inspect------------")
print("Generator: {0}".format(some_range))
# print("Length of the generator: {0}".format(len(some_range))) # TypeError aas we can't check the lenght of something we can't see inside
print("First element of the generator: {0}".format(next(some_range)))
print("Second element of the generator: {0}".format(next(some_range)))

print("Rest of items:")
[print(next_item) for next_item in some_range]

print("Generator is now exhausted, we can't access it anymore")
try:
    print("Next item in the generator".format(next(some_range)))
except StopIteration as si:
    print("I'm exhausted")


print("------------First let's define a custom Sequence ------------")
class Sentence:
     def __init__(self, text):
         self.text = text
         self.words = text.split(" ")
     def __getitem__(self, index):
        return self.words[index]
     def __len__(self):
        return len(self.words)
     def __repr__(self):
        return str(self.words)


sentence = Sentence('"Well, this should be tokenized soon')
print("The length of the list is: {0}".format(len(sentence)))
print("The list is {0}".format(sentence))


print("------------Then let's define a custom iterator object------------")
class CustomIterator:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max_val:
            raise StopIteration
        else:
            self.current += 1
            return self.current**2

print("Let's iterate over the custom Iterable")
for c in CustomIterator(5):
    print(c)

print("------------Now let's create a generator------------")
def GeneratorFunction(max_val):
    for i in range(1,max_val):
        yield i**2

generator = GeneratorFunction(6)
for item in generator:
    print(item)


print("------------Some checks?------------")

from helper import show_memory_allocation

print("We can create a generator for a very big number")
big_generator = GeneratorFunction(50000000)
for i in range(5):
    print("I am the infinite generator, this is number: {0}".format(next(big_generator)))
show_memory_allocation()
print("If we try to create a list out of the generator")
big_list = list(big_generator)
show_memory_allocation()
