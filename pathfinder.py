from PIL import Image, ImageColor, ImageDraw 

"""Reads map data from list"""
class Map:
    def __init__(self, filename):
        """Appends the 'for' loop temporary variable 'e' to the new empty list"""
        self.elevations = []
        with open(filename) as file:
            for line in file:
                self.elevations.append([int(e) for e in line.split()])
        """Finds max/min elevation points with 'generators'?"""   
        self.max_elevation = max([max(row) for row in self.elevations])
        self.min_elevation = min([min(row) for row in self.elevations])


def get_elevation(self, x, y):
    """Switches x and y coordinates for 'readability'?"""
    return self.elevations[y][x]


def get_intensity(self, x, y):
    """Gets elevation color intensity"""
    return self.get_elevation(x, y) / self.max_elevation * 255
    return (self.get_elevation(x, y) - self.min_elevation) / (
        self.max_elevation - self.min_elevation) * 255


def __init__get_map:(self, x, y):
    """Plots colored pixels in a new image creating a map, saves the new image"""
    
    im = Image.new('RGBA', (600, 600))

    im.getpixel((0, 0))

    for x in range(600):
        for y in range(600):
            im.putpixel((x, y), ("""color intensity"""))
    from PIL import ImageColor
    for x in range(600):
        for y in range
    

# """Draw colored pixel route of lowest-elevation-change"""
# class DrawRoute:
#     def __init__(self, ):



if __name__ == "__main__":
    map_data = Map("elevation_small.txt") 
    


# from PIL import Image
    # img = Image.new("RGB", (600, 600), (255, 255, 255))
    # draw = ImageDraw.Draw(img)
    # square = Square((50, 50), 30)
    # draw.rectangle([
    #     square.origin,
    #     (square.origin[0]) + square.width, square.origin[1] + square.length)],
    #                 fill=0
    # img.save("test.jpg", "JPEG")




