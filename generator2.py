import random
class Top:
    def __init__(self, name, color, season, type):
        self.name = name
        self.color = color
        self.season = season
        self.type = type

    def getType(self):
        return self.type
    def getSeason(self):
        return self.season
    
    def getColor(self):
        return self.color
    
    def __eq__(self, other):
        if (self.name == other.name) and (self.color == other.color) and (self.season == other.season) and (self.type == other.type):
            return True
        else:
            return False

    def __repr__(self):
        return f"Top: {self.name}"#, color: {self.color}, season: {self.season}"

top1 = Top("shirt", "red", {"summer", "spring"}, "wellfit")
top2 = Top("tank", "beige", {"summer"}, "tight")
top3 = Top("brandy", "white", {"spring", "fall", "summer"}, "tight")
top4 = Top("uniqlo", "white", {"summer", "fall", "spring"}, "baggy")
top5 = Top("johnb", "green", {"summer"}, "tight")


class Bottom:
    def __init__(self, name, color, season, type):
        self.name = name
        self.color = color
        self.season = season
        self.type = type
    def getType(self):
        return self.type
    
    def getSeason(self):
        return self.season
    
    def getColor(self):
        return self.color
    def __repr__(self): 
        return f"Bottom: {self.name}"#, color: {self.color}, season: {self.season}"
    def __eq__(self, other):
        if (self.name == other.name) and (self.color == other.color) and (self.season == other.season) and (self.type == other.type):
            return True
        else:
            return False


bot1 = Bottom("pants", "green", {"spring", "fall"}, "baggy")
bot2 = Bottom("shorts", "blue", {"summer"}, "wellfit")
bot3 = Bottom("linenPants", "white", {"summer"}, 'baggy')
bot4 = Bottom("jeans", "blue", {"summer"}, "baggy")
bot5 = Bottom("bmJeans", "gray", {"summer"}, "wellfit")

bott = [bot1, bot2, bot3, bot4, bot5]
topp = [top1, top2, top3, top4,top5] #-already sorted by season
outfitss = []
userPref = {'gray', 'blue', 'beige', 'brown', 'white'}

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
    "purple": ["white", "black", "beige", "gray"],
    "pink": ["white", "gray", "beige", "blue","navy", "brown"],
    "beige": ["brown", "white", "black", "pink"],
    "white": ["black", "gray", "beige", "navy", "brown", "white"],
    "black": ["white", "gray", "beige", "blue", "red", "black"],
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
        if self.bottom.getColor() in colorsThatGoWith[self.top.getColor()]:
            if self.bottom.getType() in types[self.top.getType()]:
                return True
        else:
            return False

    def __repr__(self):
        return f"{self.top}, {self.bottom}"
    
    def __eq__(self, other):
        return (self.top.name == other.top.name) and (self.bottom.name == other.bottom.name)
    
season_data = {
    "Spring": (
        ("Average Range", (45, 70)),
        ("Early Spring", (40, 60)),
        ("Late Spring", (55, 75))
    ),
    "Summer": (
        ("Average Range", (70, 90)),
        ("Early Summer", (65, 85)),
        ("Peak Summer", (80, 100))
    ),
    "Autumn": (
        ("Average Range", (50, 70)),
        ("Early Autumn", (60, 80)),
        ("Late Autumn", (40, 60))
    ),
    "Winter": (
        ("Average Range", (20, 50)),
        ("Mild Winter Regions", (30, 60)),
        ("Harsh Winter Regions", (-10, 30))
    )
}

topsSorted = []
botsSorted = []
#sort by season:
def seasons(topList, bottomList, season):
    for top in topList:
        #print(top.getSeason)
        if season in top.getSeason() :
            topsSorted.append(top)
            #print(topsSorted)
    for bot in bottomList:
        if season in bot.getSeason():
            botsSorted.append(bot)
seasons(topp, bott, "summer")
print(topsSorted)
result = []
def generateAllPossibleOutfits(output, topList, bottomList):
    if topList == []:
        print("error, please add tops")
    elif bottomList == []:
        print("please add bottoms")
    else:
        for top in topList:
            for bot in bottomList:
                newOutfit = Outfit(top, bot)
                if newOutfit.isGoodOutfit():
                    output.append(newOutfit)
    return output
print(generateAllPossibleOutfits(result, topsSorted, botsSorted))

#only generate 4:

def displayOutfits(result):
    final = []
    if len(result) > 4:
        while len(final) < 4:
            rand = random.randint(0, len(result) -1)
            if result[rand] not in final:
                final.append(result[rand])
    else:
        final = result
    return final

print("final four: ", displayOutfits(result))
