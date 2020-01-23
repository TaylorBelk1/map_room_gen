class Map:
    def __init__(self):
        self.width = 100
        self.height = 100
        self.max_num_rooms = 10
        self.map = self.generate_map()

    def __str__(self):
        output = f'Each rows length(width of map): {len(self.map[0])} \n'
        output += f'Each columns length(height of map): {len(self.map)}'
        return output

    def generate_map(self):
        tiles = [[0] * self.width] * self.height
        return tiles