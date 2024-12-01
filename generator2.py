import random
from tp06 import loadImage
from itemObject import Item
from cmu_graphics import *
import os

class Top:
    def __init__(self, name, color, season, type, serialNum = 0):
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
        # if isinstance(self.color, set):
        #     result = ",".join(self.color)
        #     print("result: ", result)
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

class Bottom:
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
        # if isinstance(self.color, set):
        #     print("result: ", result)
        #     result = ",".join(self.color)
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
# top1 = Top("shirt", "red", {"summer", "spring"}, "wellfit")
# top2 = Top("tank", "beige", {"summer"}, "tight")
# top3 = Top("brandy", "white", {"spring", "fall", "summer"}, "tight")
# top4 = Top("uniqlo", "white", {"summer", "fall", "spring"}, "baggy")
# top5 = Top("johnb", "green", {"summer"}, "tight")



# bot1 = Bottom("pants", "green", {"spring", "fall"}, "baggy")
# bot2 = Bottom("shorts", "blue", {"summer"}, "wellfit")
# bot3 = Bottom("linenPants", "white", {"summer"}, 'baggy')
# bot4 = Bottom("jeans", "blue", {"summer"}, "baggy")
# bot5 = Bottom("bmJeans", "gray", {"summer"}, "wellfit")

#bott = [bot1, bot2, bot3, bot4, bot5]
#topp = [top1, top2, top3, top4,top5] #-already sorted by season

# op1 = Top("bf", "green", {"summer"}, "baggy")
# top2 = Top("bm", "blue", {"summer"}, "tight")
# bot1 = Bottom("chuu", "gray", {"summer", "fall"}, "baggy")
# bot2 = Bottom("jean", "lightBlue", {"summer"}, "tight")
# topp = [top1, top2]
# bott = [bot1, bot2]
# outfitss = []
# userPref = {'gray', 'blue', 'beige', 'brown', 'white'}
# print("top1: ", top1.getColor())

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
        self.userPrefColors = set()
    def getTop(self):
        return self.top
    def getBottom(self):
        return self.bottom
    def getColor(self):
        print("top color: ", self.top.getColor())
        print("bottom color: ", self.bottom.getColor())
        return self.top.getColor() | self.bottom.getColor()
    def getStyle(self):
        return self.top.getType() | self.bottom.getType()
    def updatePref(self, other):
        self.userPrefColors.add(tuple(other))
    def isGoodOutfit(self):
        # bot = list(self.bottom.getColor())
        # top = list(self.top.getColor())
        
        #bottomCol = [self.bottom.getColor()]

        for colorBottom in self.bottom.getColor():
            for colorTop in self.top.getColor():
                print("colorrr: ", colorTop)
                if self.userPrefColors == set():
                    if colorTop in colorsThatGoWith: 
                        print("colroTop: ", colorTop)
                        if colorBottom in colorsThatGoWith[colorTop]:
                            if self.bottom.getType() in types.get(self.top.getType()):  # Safe dictionary access
                                return True
                else:
                    if colorTop in colorsThatGoWith and colorTop in self.userPrefColors: 
                        print("colroTop: ", colorTop)
                        if colorBottom in colorsThatGoWith[colorTop] and colorBottom in self.userPrefColors:
                            if self.bottom.getType() in types.get(self.top.getType()):  # Safe dictionary access
                                return True
        return False 

    def __repr__(self):
        return f"{self.top}, {self.bottom}"
    
    def __eq__(self, other):
        return (self.top.serialNum == other.top.serialNum) and (self.bottom.serialNum == other.bottom.serialNum)
    
    def __hash__(self):
        return hash(str(self))
    
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
def seasons(topList, bottomList, season, topsSorted, botsSorted):
    for top in topList:
        print("get season: ", top.getSeason())
        if season in top.getSeason() :
            topsSorted.append(top)
            print("sorted list for now: ", topsSorted)
    for bot in bottomList:
        if season in bot.getSeason():
            botsSorted.append(bot)
    return topsSorted, botsSorted

#topsSorted, botsSorted = seasons(topp, bott, "summer",topsSorted, botsSorted)
#print(topsSorted)
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
                print("newOutfit: ", newOutfit)
                if newOutfit.isGoodOutfit():
                    print("good outfit!")
                    output.append(newOutfit)
    return output
print(generateAllPossibleOutfits(result, topsSorted, botsSorted))

#only generate 4:
def displayOutfits(result):
    final = []
    if not result:  # Check if the list is empty
        print("No outfits available to display.")
        return result 
    
    if len(result) > 4:
        while len(final) < 4:
            rand = random.randint(0, len(result) - 1)
            if result[rand] not in final:
                final.append(result[rand])
    else:
        final = result
    return final

print("final four: ", displayOutfits(result))
final = displayOutfits(result)

def onAppStart(app):
    app.width = 900
    app.height = 650
    top1 = Top("bf", {"green"}, {"summer"}, "baggy", "0IMG_1469")
    top2 = Top("bm",{ "blue"}, {"summer"}, "tight", "5IMG_1479")
    top3 = Top("Pacsun", {"red"}, {"summer", "spring"}, "tight", "2IMG_1473")
    top4 = Top("bm", {"white"}, {"summer", "spring"}, "tight", "1IMG_1470")
    bot1 = Bottom("chuu", {"gray"}, {"summer", "fall"}, "baggy", "3IMG_1475")
    bot2 = Bottom("jean", {"lightBlue"}, {"summer"}, "well-fit", "4IMG_1476")
    app.tops = [top1, top2, top3, top4]
    app.bottoms = [bot1, bot2]
    app.finadd = Outfit(top1, bot2)
    #app.finadd.append(Outfit(top2, bot2))
    app.numCols = 4
    app.itemSize = (app.width//app.numCols, 230) 
    app.itemsPerRow = app.numCols
    app.scrollOffset = 30
    app.userPrefColors = {"colors": set()}
    app.xPos = []
    app.final = []
    app.likedOutfits = []
    #app.userPref = {"color": set(), "type": set()}

    for item in loadImage("test"):
        filename = os.path.splitext(os.path.basename(item))[0]
        print("namsssss: ", filename)
        Item(item, filename, (0, 0), (200, 200), (0))

    app.topsSorted = []
    app.botsSorted = []
    # print("season outfpit: ", seasons(app.tops, app.bottoms, "summer",topsSorted, botsSorted))
    app.topsSorted, app.botsSorted = seasons(app.tops, app.bottoms, "summer",app.topsSorted, app.botsSorted)
    #print("tops: ", topsSorted)
    #print("bottoms: ", botsSorted)
    result = []
    (generateAllPossibleOutfits(result, app.topsSorted, app.botsSorted))
    for i in app.tops:
        print("season: ", i.getSeason())
    #print("final four: ", displayOutfits(result))
    app.final = displayOutfits(result)
    app.final.append(app.finadd)
    print(len(app.final))
        
    # Item.instances = [<itemObject.Item object at 0x000001FFAF42A1D0>, <itemObject.Item object at 0x000001FFAF335350>, <itemObject.Item object at 0x000001FFB0252B50>, <itemObject.Item object at 0x000001FFAFE8AC50>]

def redrawAll(app):
    app.xPos.clear()
    #print(final)
    #print(Item.instances)
    for i, clothing in enumerate(app.final):
        print("clothing", clothing)
        topItem = None
        bottomItem = None
        for item in Item.instances:
            # print("one", item.name, clothing.top.serialNum)
            # print("two ", item.name, clothing.bottom.serialNum)
            if item.name == clothing.top.serialNum:
                topItem = item
            if item.name == clothing.bottom.serialNum:
                bottomItem = item

        if topItem != None and bottomItem != None:
            row = i // app.numCols  
            col = i % app.numCols
            itemWidth = 180 + 45
            itemHeight = topItem.size[1] + 50
            x = (col * app.itemSize[0]) + itemWidth / 2
            y = row * (itemHeight) + 200 - app.scrollOffset
            drawImage(topItem.image, x, y, align="center", width=topItem.size[0], height=topItem.size[1])
            bottom = y + topItem.size[1] + 20
            drawImage(bottomItem.image, x, bottom, align="center", width=bottomItem.size[0], height=bottomItem.size[1])
            app.xPos.append(x)
            print("X: ", x)
            drawRect(x, 550, 150, 50, fill = None, border = "black", align = "center")
            drawLabel("add to outfits", x, 550, size = 17, font = "Lora")
    drawRect(750, 600, 150, 50, fill = None, border = "black", align = "center")
    drawLabel("regenerate", 750, 600, size = 17, font = "Lora")

def onMousePress(app, mouseX, mouseY):
    print("x position: ", app.xPos)
    for i in range(len(app.xPos)):
        print("i: ", i)
        print("final: ", app.final)
        j = app.xPos[i]
        if (mouseX >= j - 75 and mouseX <= j + 75) and (mouseY >= 525 and mouseY <= 575):
            if app.final[i] not in app.likedOutfits:
                app.likedOutfits.append(app.final[i])
    print(app.likedOutfits)
    addUserPref(app.likedOutfits, app.userPrefColors)
    #regenrate button
    if (mouseX >= 675 and mouseX <= 825) and (mouseY >= 575 and mouseY <= 625):
        print("regenerated")
        (generateAllPossibleOutfits(result, app.topsSorted, app.botsSorted))
        app.final = displayOutfits(result)

    #when regnerate:

# def regenUser(output, topList, bottomList, userPref):
#     if topList == []:
#         print("error, please add tops")
#     elif bottomList == []:
#         print("please add bottoms")
#     else:
#         for top in topList:
#             for bot in bottomList:
#                 newOutfit = Outfit(top, bot)
#                 print("newOutfit: ", newOutfit)
#                 if newOutfit.isGoodOutfit():
#                     print("good outfit!")
#                     output.append(newOutfit)
#     return output
print(generateAllPossibleOutfits(result, topsSorted, botsSorted))

def addUserPref(outfits, output):
    for clothing in outfits:
        print("abc:")
        print(clothing.getColor())
        output["colors"] = output.get("colors", set()) | clothing.getColor()
        clothing.updatePref(clothing.getColor())
    print(output)
    return output
    

def main():
    runApp()
main()