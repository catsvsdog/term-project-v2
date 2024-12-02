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

class Top(Item):
    def __init__(self, name, color, season, type, serialNum = 0):
        self.super()
        self.name = name
        self.color = color
        self.season = season
        self.type = type #baggy or not
        self.serialNum = serialNum
        self.isTop = "Top"

    def getType(self):
        return self.type
    def getSeason(self):
        result = list(self.season)
        final = ", ".join(result) 
        return final
    
    def changeName(self, other):
        self.name = other
    def changeSeason(self, other):
        self.season = other
    def changeColor(self, other):
        self.color = other
    def changeType(self, other):
        self.type = other
        
    def getColor(self):
        # result = ""
        # if isinstance(self.color, list):
        #     for i in self.color:
        #         result = ",".join(i)
        #     return result
        # else:
        return self.color
    
    def __eq__(self, other):
        if ((self.name == other.name) and (self.color == other.color) and (self.season == other.season) and (self.type == other.type)):
            return True
        else:
            return False

    def __repr__(self):
        return f"Top: {self.name}"

class Bottom(Item):
    def __init__(self, name, color, season, type, serialNum = 0):
        self.name = name
        self.color = color
        self.season = season
        self.type = type
        self.serialNum = serialNum
        self.isBottom = "bottom"
    def getType(self):
        return self.type
    def changeName(self,other):
        self.name = other
    def changeSeason(self, other):
        self.season = other
    def changeColor(self, other):
        self.color = other
    def changeType(self, other):
        self.type = other
    
    def getSeason(self):
        return self.season
    
    def getColor(self):
        # result = ""
        # if isinstance(self.color, list):
        #     for i in self.color:
        #         result = ",".join(i)
        #     return result
        # else:
        return self.color
    def __repr__(self): 
        return f"Bottom: {self.name}"#, color: {self.color}, season: {self.season}"
    def __eq__(self, other):
        if (self.name == other.name) and (self.color == other.color) and (self.season == other.season) and (self.type == other.type):
            return True
        else:
            return False
types = {
    "baggy": "tight",
    "tight": "baggy",
    "wellfit" : ["baggy", "tight"]
}

colorsThatGoWith = {
    "red": ["black", "white", "blue", "beige", "gray"],
    "orange": ["white", "brown", "beige","blue", "lightGray", "black"],
    "yellow": ["gray", "white", "navy", "beige"],
    "green": ["brown", "white", "black", "beige", "lightGray"],
    "blue": ["white", "gray", "beige", "brown", "black"],
    "lightBlue": ["white", "beige", "gray", "black", "pink"],
    "purple": ["white", "black", "beige", "gray"],
    "pink": ["white", "gray", "blue","navy", "lightBlue", "brown"],
    "beige": ["brown", "white", "black", "pink"],
    "white": ["black", "gray", "beige", "navy", "brown", "white"],
    "black": ["white", "gray", "beige","lightBlue", "blue", "red", "black"],
    "gray": ["white", "black", "blue", "pink", "yellow"],
    "brown": ["white", "beige", "blue", "green", "black"],
    "lightGray": ["white", "beige", "blue", "pink", "green"]
}

class Outfit:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def getTop(self):
        return self.top
    def getBottom(self):
        return self.bottom
    def getColor(self):
        return [self.top.getColor(), self.bottom.getColor()]
    def getStyle(self):
        return [self.top.getType(),self.bottom.getType()]
    def isGoodOutfit(self):
        bot = list(self.bottom.getColor())
        top = list(self.top.getColor())
        #bottomCol = [self.bottom.getColor()]
        for colorBottom in bot:
            for colorTop in top:
                print("colorrr: ", colorTop)
                if colorTop in colorsThatGoWith: 
                    print("colroTop: ", colorTop)
                    if colorBottom in colorsThatGoWith[colorTop]:
                        if self.bottom.getType() in types.get(self.top.getType()):  # Safe dictionary access
                            return True
        return False 

    def __repr__(self):
        return f"{self.top}, {self.bottom}"
    
    def __eq__(self, other):
        return (self.top.name == other.top.name) and (self.bottom.name == other.bottom.name)
    #def replaceTop(self, other):