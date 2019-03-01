from PIL import Image, ImageColor, ImageDraw 

"""Read map data from list"""
class Map:
    def __init__(self, filename):
        """Append the 'for' loop temporary variable 'e' to the new empty list"""
        self.elevations = []
        with open(filename) as file:
            for line in file:
                self.elevations.append([int(e) for e in line.split()])
        """Find/print max/min elevation points with generator"""   
        self.max_elevation = max([max(row) for row in self.elevations])
        self.min_elevation = min([min(row) for row in self.elevations])


def get_elevation(self, x, y):
    """Switch x and y coordinates for readability"""
    return self.elevations[y][x]


def get_intensity(self, x, y):
    """Get elevation intensity"""
    return self.get_elevation(x, y) / self.max_elevation * 255
    return (self.get_elevation(x, y) - self.min_elevation) / (
        self.max_elevation - self.min_elevation) * 255


# """Draw colored pixel image of map using coordinate data"""
# class DrawMap:
#     def __init__(self, ):


# """Draw colored pixel route of lowest-elevation-change"""
# class DrawRoute:
#     def __init__(self, ):



if __name__ == "__main__":
    map_data = Map("elevation_small.txt") 
    print(map_data.min_elevation)


# from PIL import Image

#     img = Image.new("RGBA", (600, 600))
#     img.save("what.png", "PNG")

