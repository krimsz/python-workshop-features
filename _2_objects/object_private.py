class Floor(object):
    def __init__(self, size, material="wood"):
        self.material = material
        self.size = size
        self.is_dirty = True

    def clean(self):
        self.is_dirty = False


class Door(object):
    def __init__(self, material="metal", is_open=True):
        self.material = material
        self.is_open = is_open

    def open(self):
        self.is_open = True


class Room(object):
    def __init__(self, name, door, floor, number_of_windows=1):
        self.name = name
        self._floor = floor
        self._door = door
        self.number_of_windows = number_of_windows

    def open_door(self):
        print("Opening the door for the room {0}".format(self.name))
        self._door.open()

    def clean_floor(self):
        print("Cleaning the room {0}".format(self.name))
        self._floor.clean()

    def __str__(self):
        return "------------------------------------\n" \
               "Room info\n" \
               "\tName: {0}\n" \
               "\tNumber of windows: {1}\n" \
               "\tFloor Clean: {2}\n" \
               "\tDoor Open {3}".format(self.name, self.number_of_windows, self._floor.is_dirty, self._door.is_open)


class House(object):
    def __init__(self, room_list):
        self._room_list = room_list
        self.__panic_room = Room("Safe Panic Room",
            door=Door(material="metal", is_open=False),
            floor=Floor(material="metal", size=(10, 10)),
            number_of_windows=0
        )

    def clean_rooms(self):
        print("-------------------------------------")
        print("The house is about to be cleaned")
        self._open_doors()
        self._clean_rooms()

    def is_walkable(self):
        return self._calculate_walkable()

    def is_clean(self):
        return self._calculate_clean()

    def __str__(self):
        return "------------------------------------\n" \
               "House info\n" \
               "\tNumber of rooms: {0}\n" \
               "\tAre the rooms clean: {1}\n" \
               "\tAll doors are open: {2}".format(len(self._room_list), self.is_clean(), self.is_walkable())

    def _calculate_walkable(self):
        return all([room._door.is_open == True for room in self._room_list])

    def _calculate_clean(self):
        return all([room._floor.is_dirty == False for room in self._room_list])

    def _open_doors(self):
        [room.open_door() for room in self._room_list]

    def _clean_rooms(self):
        [room.clean_floor() for room in self._room_list]


hall = Room(
    "Hall",
    door=Door(is_open=False),
    floor=Floor(size=(23, 45)),
    number_of_windows=0
)

main_bedroom = Room(
    "Main Bedroom",
    door=Door(is_open=True),
    floor=Floor(size=(200, 50)),
    number_of_windows=2
)

secondary_bedroom = Room(
    "Secondary Bedroom",
    door=Door(is_open=True),
    floor=Floor(size=(100, 50)),
    number_of_windows=1
)

kitchen = Room(
    "Kitchen",
    door=Door(is_open=False),
    floor=Floor(material="tile", size=(100, 50)),
    number_of_windows=1
)

bathroom = Room(
    "Bathroom",
    door=Door(is_open=False),
    floor=Floor(material="tile", size=(20, 20)),
    number_of_windows=1
)

house = House(room_list=[hall, main_bedroom, secondary_bedroom, kitchen, bathroom])

# When cleaning the house we also open the doors so it's easier to clean
print("Hi, I have a house. Mum is about to visit and it turns out that she's "
      "blind so I need to open all the doors for her")
print("Also, because she's my mum, the house must be cleaned")
print(house)
house.clean_rooms()
print(house)

# Now, I will try to access any room that is inside the house and close the door
# "_{attribute/method}" is a convention. Python will not enforces any kind of encapsulation on the attributes
house._room_list[0]._door.is_door_open = True
print(house)

# The house has a secret panic room that is not part of the list of rooms. Let's see if we can access it the same way
print("------------------------------------Accessing panic room!!------------------------------------")
try:
    print(house.__panic_room._door.is_open)
except AttributeError as e:
    # Oh snap! we can't access it. Is it private?
    # Not really...
    print("Ouch, it doesn't exist!")
    print(vars(house))
    # '_House__panic_room': <__main__.Room object at ...

print("I found it!!")
print(house._House__panic_room)

