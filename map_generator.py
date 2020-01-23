from map_class import Map
from room import Room
from random_int import Random_Integer
import sys

class Map_Generator:
    def __init__(self):
        # Generate the map
        self.new_map = Map()
        self.rooms_list = []

    def __str__(self):
        output = f'total number of rooms: {len(self.rooms_list)}'
        return output

        # Generate rooms
    def generate_rooms(self):
        while len(self.rooms_list) < self.new_map.max_num_rooms:
            # generate random x/y coords
            coord_x = self.get_rando(self.new_map.width, 32)
            coord_y = self.get_rando(self.new_map.height, 25)
            # create the room
            current_room = Room((coord_x, coord_y))
            self.check_for_intersect(current_room)


    def get_rando(self, map_dimension, room_dimension):
        return Random_Integer.get_random_int(0, ((map_dimension - room_dimension)-2))


    def check_for_intersect(self, current_room):
        failed = False
        # determine whether any of the rooms in the list intersect our new Room
        for room in self.rooms_list:
            if current_room.intersect(room):
                failed = True
                break

        if not failed:
            # print(current_room)
            self.rooms_list.append(current_room)
            self.place_room_on_map(self.new_map, current_room)


    def place_room_on_map(self, new_map, new_room):
        min_y = min(new_room.y1, new_room.y2)
        max_y = max(new_room.y1, new_room.y2)
        min_x = min(new_room.x1, new_room.x2)
        max_x = max(new_room.x1, new_room.x2)
        # print(f'1: ({new_room.y1}, {new_room.x1}), 2: ({new_room.y2}, {new_room.x2})')
        # print(new_map)
        print(new_room)
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                new_map.map[y][x] = 1


def test_print():
    test_var = Map_Generator()
    test_var.generate_rooms()
    sys.stdout = open("c:\\Users\\ad9c84\\Documents\\python_map_algo\\test.txt", "w")
    print(test_var.new_map.map)

test_print()

