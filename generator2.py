from random import randint, choice
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

    def display(self):
      """display top."""
      print(f"top name: {self.name}, color= {self.color}, season={self.season}, type={self.type}.") 


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

    def display(self):
      """display bottom."""
      print(f"Bottom name: {self.name}, color= {self.color}, season={self.season}, type={self.type}.") 

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
        self.userPrefColors = set()
    def getTop(self):
        return self.top
    def getBottom(self):
        return self.bottom
    def getColor(self):
      """Returns the color of the outfit.

        Prioritizes the top's color. If the top has no color, 
        returns the bottom's color.
      """
      top_color = self.top.getColor()
      bottom_color = self.bottom.getColor()
      if top_color:
        return top_color
      else:
        return bottom_color
    def getStyle(self):
      topType = self.top.getType()
      bottomType = self.bottom.getType()
      if topType:
        return topType
      else:
        return bottomType 
    def updatePref(self, other):
        self.userPrefColors.add(tuple(other))
    def isColorMatch(self):
        # try using top to match bottom first
        topColors = self.top.getColor()
        bottomColors = self.bottom.getColor()
        for topColor in topColors:
            if topColor in colorsThatGoWith:  # Check if the top color is in the dictionary
                matchedColors = set(colorsThatGoWith[topColor])  # Convert to set for easier comparison
                if matchedColors & bottomColors:  # Intersection: any common element
                    print('Eric: Found bottom that matches top')
                    return True

        # Now, check if any color from bottom matches any from top's compatible colors
        for bottomColor in bottomColors:
            if bottomColor in colorsThatGoWith:
                matchedColors = set(colorsThatGoWith[bottomColor])
                if matchedColors & topColors:  # Intersection check again
                    print('Eric: Found top that matches bottom')
                    return True
        # matched_color_list = colorsThatGoWith[topColor]
        # if bottomColor in matched_color_list:
        #     print('Eric: find bottom that matches top')
        #     return True
        # # now try using bottom to match top since we couldn't find
        # # matching bottom
        # matched_color_list = colorsThatGoWith[bottomColor]
        # if topColor in matched_color_list:
        #     print('Eric: find top that matches bottom')
        #     return True
        print('Info, No match find.')
        return False
    def isTypeMatch(self):
        if self.bottom.getType() in types.get(self.top.getType()):
            return True
        return False


    def display(self):
      """display the top and bottom"""
      self.top.display()
      self.bottom.display()

    def __repr__(self):
        return f"{self.top}, {self.bottom}"
    
    def __eq__(self, other):
        return (self.top.serialNum == other.top.serialNum) and (self.bottom.serialNum == other.bottom.serialNum)
    
    def __hash__(self):
        return hash(str(self))
    

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


def getSeasonTops(topList, season):
  """ return a list of season tops.

  Args:
    topList: List of Tops objects
    season: season string, for example: "summer"

  Returns:
    seasonTops: a list of tops that matches the season or nil
  """
  season_tops = []
  for top in topList:
    if season in top.getSeason():
        season_tops.append(top)
  return season_tops


def getSeasonBottoms(bottomList, season):
  """ return a list of season tops.

  Args:
    bottomList: List of Bottom objects
    season: season string, for example: "summer"

  Returns:
    season_bottoms: a list of tops that matches the season or nil
  """
  season_bottoms = []
  for bottom in bottomList:
    if season in bottom.getSeason():
        season_bottoms.append(bottom)
  return season_bottoms


def generateAllGoodOutfits(topList, bottomList):
  """Take all top and bottom and generate each combination of
   of outfits based on Good Outfit rules

  Args:
    topList: List of Top objects
    bottomList: List of Bottom objects

  Returns:
    a list of good outfit objects
  """
  if not topList:
    print('Eror, top is empty, please add tops.')
    sys.exit(0)
  if not bottomList:
    print('Error, bottom is empty, please add bottoms')
    sys.exit(0)
  good_outfits = []
  for top in topList:
    for bottom in bottomList:
        outfit = Outfit(top, bottom)
        print('outfit = ', outfit)
        if outfit.isColorMatch():# and outfit.isTypeMatch():
            good_outfits.append(outfit)

  return good_outfits


# #topsSorted, botsSorted = seasons(topp, bott, "summer",topsSorted, botsSorted)
# #print(topsSorted)
# def generateAllPossibleOutfits(output, topList, bottomList):
#     if topList == []:
#         print("error, please add tops")
#     elif bottomList == []:
#         print("please add bottoms")
#     else:
#         for top in topList:
#             for bot in bottomList:
#                 newOutfit = Outfit(top, bot)
#                 print("newOutfit: ", newOutfit)
#                 if newOutfit.isColorMatch():
#                     print("good outfit!")
#                     output.append(newOutfit)
#     return output

# #only generate 4:
# def displayOutfits(result):
#     final = []
#     if not result:  # Check if the list is empty
#         print("No outfits available to display.")
#         return result 
    
#     if len(result) > 4:
#         while len(final) < 4:
#             rand = random.randint(0, len(result) - 1)
#             if result[rand] not in final:
#                 final.append(result[rand])
#     else:
#         final = result
#     return final

#print("final four: ", displayOutfits(result))
#final = displayOutfits(result)

def onAppStart(app):
    app.width = 900
    app.height = 650
    # top1 = Top("shirt", {"red"}, {"summer", "spring"}, "wellfit","0IMG_1469")
    # top2 = Top("tank", {"beige"}, {"summer"}, "tight","5IMG_1479")
    # top3 = Top("brandy", {"white"}, {"spring", "fall", "summer"}, "tight")
    # top4 = Top("uniqlo", {"white"}, {"summer", "fall", "spring"}, "baggy")
    # top5 = Top("johnb", {"green"}, {"summer"}, "tight")

    # bot1 = Bottom("pants", {"green"}, {"spring", "fall"}, "baggy")
    # bot2 = Bottom("shorts",{"blue"}, {"summer"}, "wellfit")
    # bot3 = Bottom("linenPants", {"white"}, {"summer"}, 'baggy')
    # bot4 = Bottom("jeans", {"blue"}, {"summer"}, "baggy")
    # bot5 = Bottom("bmJeans", {"gray"}, {"summer"}, "wellfit")
    top1 = Top("bf", {"green"}, {"summer"}, "baggy", "0IMG_1469")
    top2 = Top("bm",{ "blue"}, {"summer"}, "tight", "5IMG_1479")
    top3 = Top("Pacsun", {"red"}, {"summer", "spring"}, "tight", "2IMG_1473")
    top4 = Top("bm", {"white"}, {"summer", "spring"}, "tight", "1IMG_1470")
    bot1 = Bottom("chuu", {"gray"}, {"summer", "fall"}, "baggy", "3IMG_1475")
    bot2 = Bottom("jean", {"lightBlue"}, {"summer"}, "well-fit", "4IMG_1476")
    app.tops = [top1, top2, top3, top4]
    app.bottoms = [bot1, bot2]

    # app.bottoms = [bot1, bot2, bot3, bot4, bot5]
    # app.tops = [top1, top2, top3, top4,top5]
    print('top list = ', app.tops)
    print('bottom list = ', app.bottoms)
    app.my_good_outfits = generateAllGoodOutfits(app.tops, app.bottoms)

    print('good outfits: ', app.my_good_outfits)

    # now I have a list of color matched good outfits

    print('Testing display first 4 outfits')

    # displayed outfits contains a list of outfit being displayed
    app.displayed_outfits = []

    print('size of good outfits = ', len(app.my_good_outfits))

    # run a while loop to print 4 randomy generated outfits until empty
    # while True:
    #     if not app.my_good_outfits:
    #         print('Info: good outfit is empty, exit test')
    #         return
    #     print("outfitssssss")
    #     app.my_good_outfits, displayed_outfits = display4Outfits(app.my_good_outfits, app.displayed_outfits)
        # print("displayed outtsz------: ", displayed_outfits)

        # print('good outfit len = ', len(app.my_good_outfits))
        # print('displayed = ', len(displayed_outfits))
        # print("----------------------------------------------------------")
        # print("final outfits: ", app.my_good_outfits)

    # app.finadd = Outfit(top1, bot2)
    # #app.finadd.append(Outfit(top2, bot2))
    app.numCols = 4
    app.itemSize = (app.width//app.numCols, 230) 
    app.itemsPerRow = app.numCols
    app.scrollOffset = 30
    # app.userPrefColors = {"colors": set()}
    app.xPos = []
    # app.final = []
    # app.likedOutfits = []
    # #app.userPref = {"color": set(), "type": set()}

    for item in loadImage("test"):
        filename = os.path.splitext(os.path.basename(item))[0]
        print("namsssss: ", filename)
        Item(item, filename, (0, 0), (200, 200), (0))

    # app.topsSorted = []
    # app.botsSorted = []
    # # print("season outfpit: ", seasons(app.tops, app.bottoms, "summer",topsSorted, botsSorted))
    # app.topsSorted, app.botsSorted = seasons(app.tops, app.bottoms, "summer",app.topsSorted, app.botsSorted)
    # #print("tops: ", topsSorted)
    # #print("bottoms: ", botsSorted)
    # result = []
    # (generateAllPossibleOutfits(result, app.topsSorted, app.botsSorted))
    # for i in app.tops:
    #     print("season: ", i.getSeason())
    # #print("final four: ", displayOutfits(result))
    # app.final = displayOutfits(result)
    # app.final.append(app.finadd)
    # print(len(app.final))
    
   
   # Item.instances = [<itemObject.Item object at 0x000001FFAF42A1D0>, <itemObject.Item object at 0x000001FFAF335350>, <itemObject.Item object at 0x000001FFB0252B50>, <itemObject.Item object at 0x000001FFAFE8AC50>]
def addUserPref(outfits, output):
    for clothing in outfits:
        print("abc:")
        print(clothing.getColor())
        output["colors"] = output.get("colors", set()) | clothing.getColor()
        clothing.updatePref(clothing.getColor())
    print(output)
    return output
    

def generate_season_data():
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
  return season_data


def pickOutfitOnUserPreference(outfits, user_preferences):
  """Pick outfit based on User Preference input.

  Args:
    outfits: list of good outfits
    user_prefereces: a list of user preferences such as color, type in string
  
  Return:
    A Good outfit or nil if outfits is empty or no match is found
  """
  if not outfits:
    print('Warning, outfits is empty!')
    return None
  for outfit in outfits: # iterate over each outfit and check color and type against it
    if outfit.getColor() in user_preferences:
        print('Found user preferred color match')
        return outfit
    if outfit.getStyle() in user_preferences:
        print('Found user preferred type match')
        return outfit

  print('Warning: no user preferred match, return None')
  return None


def pickAGoodOutfitRandomly(outfits):
  """Randomly pick 1 outfit from good outfit list.

  Args:
    outfits: list of good outfits
  
  Return:
    A Good outfit or nil if none outfits is empty
  """
  if not outfits:
    print('Warning, outfit is empty, return None object')
    return None
  outfit = choice(outfits)
  return outfit




def display4RandomOutfits(outfits, displayed_outfits):
  """ display 4 outfits at a time.
  if the number of outfits is less than 4, then
  display the rest of outfits

  Args:
    outfits: good outfits list

  return:
    updated outfits list after removing displayed object
    displayed_outfits list
  """
  # check the outfits list len
  outfits_size = len(outfits)

  loop_range = loop_range = min(outfits_size, 4)

  for i in range(loop_range): # loop from 0 to 4
    outfit = pickAGoodOutfitRandomly(outfits)
    if not outfit:
        print('Warning: outfits is empty now, return None.')
        return None, None

    # display 1 outfit
    outfit.display()
    # remove outfit from good outfit list
    outfits.remove(outfit)
    # add displayed outfit into display outfit list
    displayed_outfits.append(outfit)

  return outfits, displayed_outfits

def display4UserPreferredOutfits(outfits, preferred_outfits, user_preferences):
  """ display 4 outfits at a time.
  if the number of outfits is less than 4, then
  display the rest of outfits

  Args:
    outfits: good outfits list
    preferred_outfits: preferred_outfit lists

  return:
    updated outfits list after removing displayed object
    preferred_outfits list
  """
  # check the outfits list len
  outfits_size = len(outfits)

  loop_range = loop_range = min(outfits_size, 4)

  for i in range(loop_range): # loop from 0 to 4
    outfit = pickOutfitOnUserPreference(outfits, user_preferences)
    if not outfit:
        print('Warning: outfit is empty, nothing to display!')
        return None, None
    # display 1 outfit
    outfit.display()
    # remove outfit from good outfit list
    outfits.remove(outfit)
    # add displayed outfit into display outfit list
    preferred_outfits.append(outfit)

  return outfits, preferred_outfits

def test_generator():
  """ main testing code for generator"""

  print('Starting testing generator...')
  top1 = Top("shirt", "red", {"summer", "spring"}, "wellfit")
  top2 = Top("tank", "beige", {"summer"}, "tight")
  top3 = Top("brandy", "white", {"spring", "fall", "summer"}, "tight")
  top4 = Top("uniqlo", "white", {"summer", "fall", "spring"}, "baggy")
  top5 = Top("johnb", "green", {"summer"}, "tight")

  bot1 = Bottom("pants", "green", {"spring", "fall"}, "baggy")
  bot2 = Bottom("shorts", "blue", {"summer"}, "wellfit")
  bot3 = Bottom("linenPants", "white", {"summer"}, 'baggy')
  bot4 = Bottom("jeans", "blue", {"summer"}, "baggy")
  bot5 = Bottom("bmJeans", "gray", {"summer"}, "wellfit")

  bottoms = [bot1, bot2, bot3, bot4, bot5]
  tops = [top1, top2, top3, top4,top5]

  print('top list = ', tops)
  print('bottom list = ', bottoms)
  my_good_outfits = generateAllGoodOutfits(tops, bottoms)

  print('good outfits: ', my_good_outfits)

  # now I have a list of color matched good outfits

  print('Testing display first 4 outfits')

  # displayed outfits contains a list of outfit being displayed
  displayed_outfits = []

  print('size of good outfits = ', len(my_good_outfits))

  # run a while loop to print 4 randomy generated outfits until empty
  while True:
    if not my_good_outfits:
      print('Info: good outfit is empty, exit test')
      break

    my_good_outfits, displayed_outfits = display4RandomOutfits(my_good_outfits, displayed_outfits)

    if my_good_outfits is None or displayed_outfits is None:
        break
    print('good outfit len = ', len(my_good_outfits))
    print('displayed = ', len(displayed_outfits))
def redrawAll(app):
    app.xPos.clear()
    outfits_size = len(app.my_good_outfits)
    loop_range = min(outfits_size, 4)

    for i in range(loop_range):  # loop from 0 to 4
        outfit = pickAGoodOutfitRandomly(app.my_good_outfits)
        if not outfit:
            print('Warning: outfit is empty')
            return
        
        # Find the top and bottom items for the outfit
        topItem = None
        bottomItem = None
        for item in Item.instances:
            if item.name == outfit.top.serialNum:
                topItem = item
                print("yollo")
            if item.name == outfit.bottom.serialNum:
                bottomItem = item

        # Only display the outfit if both top and bottom items are found
        if topItem and bottomItem:
            row = i // app.numCols  
            col = i % app.numCols
            itemWidth = 180 + 45
            itemHeight = topItem.size[1] + 50
            x = (col * app.itemSize[0]) + itemWidth / 2
            y = row * itemHeight + 200 - app.scrollOffset

            # Draw the top and bottom items
            drawImage(topItem.image, x, y, align="center", width=topItem.size[0], height=topItem.size[1])
            bottom = y + topItem.size[1] + 20
            drawImage(bottomItem.image, x, bottom, align="center", width=bottomItem.size[0], height=bottomItem.size[1])
            app.xPos.append(x)
            # Draw the "add to outfits" button
            drawRect(x, 550, 150, 50, fill=None, border="black", align="center")
            drawLabel("add to outfits", x, 550, size=17, font="Lora")

            # Remove the displayed outfit from the good outfits list and add it to the displayed outfits
            app.my_good_outfits.remove(outfit)
            app.displayed_outfits.append(outfit)

        # Print the final status of Item instances for debugging
        print(Item.instances)

    # Draw the "regenerate" button at the end
    drawRect(750, 600, 150, 50, fill=None, border="black", align="center")
    drawLabel("regenerate", 750, 600, size=17, font="Lora")

# def onMousePress(app, mouseX, mouseY):
#     print("x position: ", app.xPos)
#     for i in range(len(app.xPos)):
#         print("i: ", i)
#         print("final: ", app.final)
#         j = app.xPos[i]
#         if (mouseX >= j - 75 and mouseX <= j + 75) and (mouseY >= 525 and mouseY <= 575):
#             if app.final[i] not in app.likedOutfits:
#                 app.likedOutfits.append(app.final[i])
#     print(app.likedOutfits)
#     addUserPref(app.likedOutfits, app.userPrefColors)
    #regenrate button
    # if (mouseX >= 675 and mouseX <= 825) and (mouseY >= 575 and mouseY <= 625):
    #     print("regenerated")
    #     (generateAllPossibleOutfits(result, app.topsSorted, app.botsSorted))
    #     app.final = displayOutfits(result)

def main():
    runApp()
main()
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
#print(generateAllPossibleOutfits(result, topsSorted, botsSorted))


# def test_generator():
#     print('Starting testing generator...')
# #   top1 = Top("shirt", {"red"}, {"summer", "spring"}, "wellfit")
# #   top2 = Top("tank", {"beige"}, {"summer"}, "tight")
# #   top3 = Top("brandy", {"white"}, {"spring", "fall", "summer"}, "tight")
# #   top4 = Top("uniqlo", {"white"}, {"summer", "fall", "spring"}, "baggy")
# #   top5 = Top("johnb", {"green"}, {"summer"}, "tight")

# #   bot1 = Bottom("pants", {"green"}, {"spring", "fall"}, "baggy")
# #   bot2 = Bottom("shorts",{"blue"}, {"summer"}, "wellfit")
# #   bot3 = Bottom("linenPants", {"white"}, {"summer"}, 'baggy')
# #   bot4 = Bottom("jeans", {"blue"}, {"summer"}, "baggy")
# #   bot5 = Bottom("bmJeans", {"gray"}, {"summer"}, "wellfit")
#     top1 = Top("bf", {"green"}, {"summer"}, "baggy", "0IMG_1469")
#     top2 = Top("bm",{ "blue"}, {"summer"}, "tight", "5IMG_1479")
#     top3 = Top("Pacsun", {"red"}, {"summer", "spring"}, "tight", "2IMG_1473")
#     top4 = Top("bm", {"white"}, {"summer", "spring"}, "tight", "1IMG_1470")
#     bot1 = Bottom("chuu", {"gray"}, {"summer", "fall"}, "baggy", "3IMG_1475")
#     bot2 = Bottom("jean", {"lightBlue"}, {"summer"}, "well-fit", "4IMG_1476")
#     tops = [top1, top2, top3, top4]
#     bottoms = [bot1, bot2]

#     # bottoms = [bot1, bot2, bot3, bot4, bot5]
#     # tops = [top1, top2, top3, top4,top5]

#     print('top list = ', tops)
#     print('bottom list = ', bottoms)
#     my_good_outfits = generateAllGoodOutfits(tops, bottoms)

#     print('good outfits: ', my_good_outfits)

#     # now I have a list of color matched good outfits

#     print('Testing display first 4 outfits')

#     # displayed outfits contains a list of outfit being displayed
#     displayed_outfits = []

#     print('size of good outfits = ', len(my_good_outfits))

#     # run a while loop to print 4 randomy generated outfits until empty
#     while True:
#         if not my_good_outfits:
#             print('Info: good outfit is empty, exit test')
#             return
#         print("outfitssssss")
#         my_good_outfits, displayed_outfits = display4Outfits(my_good_outfits, displayed_outfits)
#         print("displayed outtsz------: ", displayed_outfits)

#         print('good outfit len = ', len(my_good_outfits))
#         print('displayed = ', len(displayed_outfits))
#         print("----------------------------------------------------------")
#         print("final outfits: ", my_good_outfits)

  # dummy user preferences data for testing, in the real code, this data
  # is constructed dynamically by reading the user selected outfit and analyze it
  # test case #1
  #user_preferences = ["red", "green", "baggy", "wellfit"]
  # test case #2, match 1 color
  user_preferences = ["red"]
  # test case #3, match 1 type
  #user_preferences = ["baggy"]

  print('Testing user preference display...')
  # At this moment, all the outfits are in the displayed_outfits list because they are all displayed
  # we will use this list for testings
  preferred_outfits = []
  while True:
    if not displayed_outfits:
      print('Info: displayed outfits list is empty')
      break

    print('display outfit len = ', len(displayed_outfits))
    print('preferred list = ', len(preferred_outfits))

    displayed_outfits, preferred_outfits = display4UserPreferredOutfits(displayed_outfits, preferred_outfits, user_preferences)
    if displayed_outfits is None and preferred_outfits is None:
        break

