print("------------COROUTINES ------------")
print("A generator on steroids")

# Focused on "waiting" for a response more than lazy-loading files
# Terminology is usually used with no "order"
def sample_coroutine():
    answer = yield "Hello"
    yield answer

c = sample_coroutine()
print(next(c))
print(c.send("Mobiquity"))