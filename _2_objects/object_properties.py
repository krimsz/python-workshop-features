class Celsius(object):
    def __init__(self, temperature):
        self._temperature = temperature


# No constraint enforcing
temperature1 = Celsius(2)
print(temperature1._temperature)

# Hmmmm??
temperature2 = Celsius(-1000)
print(temperature2._temperature)

# Getter/Setter constraint enforcing
class CelsiusGetterSetter(object):
    def __init__(self, temperature):
        self.set_temperature(temperature)

    def set_temperature(self, temperature):
        if temperature < -273:
            raise ValueError("You are breaking the laws of physics!!!")
        self._temperature = temperature

    def get_temperature(self):
        return self._temperature

temperature_getter_setter1 = CelsiusGetterSetter(2)
print(temperature_getter_setter1.get_temperature())

try:
    temperature_getter_setter2 = CelsiusGetterSetter(-1000)
except ValueError as ve:
    print(ve)

# Aha!!! it works!!! but in python since we can't define private attrs, we normally access them by name (no getter and setter)
# @property helps us

# @property constraint enforcing
class CelsiusWithProperty(object):
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        if temperature < -273:
            raise ValueError("You are breaking the laws of physics!!!")
        self._temperature = temperature



temperature_property1 = CelsiusWithProperty(2)
print(temperature_property1.temperature)

try:
    temperature_property2 = CelsiusWithProperty(-1000)
except ValueError as ve:
    print(ve)
try:
    temperature_property1.temperature = -2000
except ValueError as ve:
    print(ve)
print(temperature_property1.temperature)

# We can't create truly private attributes though, so any caller can modify the internal state of the object
temperature_property1._temperature = -12313210
print(temperature_property1.temperature)
