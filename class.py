class Flower:
    def __init__(self, name, color, classification):
        self.name = name
        self.color = color
        self.classification = classification

    def flowerInfo(self):
        print("Name of the flower is " + self.name)
        print("Color of the flower is " + self.color)

obj1 = Flower("Rose", "Red", "Shrube")
obj1.flowerInfo()