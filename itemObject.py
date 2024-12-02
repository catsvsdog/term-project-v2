class Item:
    instances = []
    def __init__(self, image, name, pos, size, serialNum):
        self.image = image
        self.name = name
        self.pos = pos
        self.size = size
        self.bounds = None
        self.serialNum = serialNum
        Item.instances.append(self)

    def update_bounds(self, x, y, width, height):
        self.bounds = (x, y, x + width, y + height)