from PIL import Image, ImageColor, ImageDraw 

"""Reads map data from list"""
class Map:
    def __init__(self, filename):
        """Appends the 'for' loop temporary variable 'e' to the new empty list"""
        self.elevations = []
        with open(filename) as file:
            for line in file:
                self.elevations.append([int(e) for e in line.split()])
        """Finds max/min elevation point in each list with generators"""   
        self.max_elevation = max([max(row) for row in self.elevations])
        self.min_elevation = min([min(row) for row in self.elevations])


    def get_elevation(self, x, y):
        """Switches x and y coordinates for readability"""
        return self.elevations[y][x]


    def get_intensity(self, x, y):
        """Gets elevation color intensity"""
        return int((self.get_elevation(x, y) - self.min_elevation) / (
            self.max_elevation - self.min_elevation) * 255)


    def get_map(self):
        """Plots colored pixels in a new image creating a map, saves the new image"""
        
        mountain_map = Image.new('RGB', (600, 600))

        mountain_map.getpixel((0, 0))

        for x in range(600):
            for y in range(600):
                mountain_map.putpixel((x, y), (self.get_intensity(x, y), self.get_intensity(x, y), self.get_intensity(x, y)))
        mountain_map.save("mountain_map.png")
        
    

# class DrawRoute:
# """Draw colored pixel route of lowest-elevation-change"""
#     def __init__(self, ):



if __name__ == "__main__":
    map_data = Map("elevation_small.txt") 
    # get_elevation = map_data.get_elevation
    # get_intensity = map_data.get_intensity
    map_data.get_map()

