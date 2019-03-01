"""Reads map data from list"""
class Map:
    def __init__(self, filename):
        self.elevations = []
        with open(filename) as file:
            for line in file:
                self.elevations.append([int(e) for e in line.split()])

        "Finds/prints max/min elevation points"   
        self.max_elevation = max([max(row) for row in self.elevations])
        self.min_elevation = min([min(row) for row in self.elevations])
        print(self.max_elevation)
        print(self.min_elevation)


def get_elevation(self, x, y):
    """Switches x and y for readability"""
    return self.elevations[y][x]

def get_intensity(self, x, y):
    return self.get_elevation(x, y) / self.max_elevation * 255
    return (self.get_elevation(x, y) - self.min_elevation) / (
        self.max_elevation - self.min_elevation) * 255


"""Draws colored pixels using map data"""
class Draw:
    def __init__(self, filename):




if __name__ == "__main__":
    