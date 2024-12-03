from random import randint, choice
from tp06 import loadImage
from objects2 import Item, Outfit
from cmu_graphics import *
import os


# types = {
#     "baggy": "tight",
#     "tight": "baggy",
#     "wellfit" : ["baggy", "tight"]
# }

# colorsThatGoWith = {
#     "red": ["black", "white", "blue", "beige", "gray"],
#     "orange": ["white", "brown", "beige","blue", "lightGray", "black"],
#     "yellow": ["gray", "white", "navy", "beige"],
#     "green": ["brown", "white", "black", "beige", "lightGray"],
#     "blue": ["white", "gray", "beige", "brown", "black"],
#     "lightBlue": ["white", "beige", "gray", "black", "pink"],
#     "purple": ["white", "black", "beige", "gray"],
#     "pink": ["white", "gray", "blue","navy", "lightBlue", "brown"],
#     "beige": ["brown", "white", "black", "pink"],
#     "white": ["black", "gray", "beige", "navy", "brown", "white"],
#     "black": ["white", "gray", "beige","lightBlue", "blue", "red", "black"],
#     "gray": ["white", "black", "blue", "pink", "yellow"],
#     "brown": ["white", "beige", "blue", "green", "black"],
#     "lightGray": ["white", "beige", "blue", "pink", "green"]
# }
def drawButton(x, y, width, height, radius, fill='black', border=None, borderWidth=1):
    drawRect(x + radius, y, width - 2 * radius, height, fill=fill)
    drawRect(x, y + radius, width, height - 2 * radius, fill=fill)
    drawCircle(x + radius, y + radius, radius, fill=fill)
    drawCircle(x + width - radius, y + radius, radius, fill=fill) 
    drawCircle(x + radius, y + height - radius, radius, fill=fill)
    drawCircle(x + width - radius, y + height - radius, radius, fill=fill) 

def seasons(topList, bottomList, season, topsSorted, botsSorted):
    for top in topList:
        print("get season: ", top.season)
        if season in top.season:
            topsSorted.append(top)
            print("sorted list for now: ", topsSorted)
    for bot in bottomList:
        if season in bot.season:
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
    if season in top.season:
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
    if season in bottom.season:
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
    print('Error, top is empty, please add tops.')
    #sys.exit(0)
  if not bottomList:
    print('Error, bottom is empty, please add bottoms')
    #sys.exit(0) 
  good_outfits = []
  for top in topList:
    for bottom in bottomList:
        outfit = Outfit(top, bottom)
        print('outfit = ', outfit)
        if outfit.isColorMatch() and outfit.isTypeMatch():
            good_outfits.append(outfit)

  return good_outfits


# 
def onAppStart(app):
    app.width = 900
    app.height = 650
    top1 = Item(None, "bf", None, 200, {"green"}, {"summer"}, "baggy", 'top', "processed\\IMG_1469.png")
    top2 = Item(None, "bm", None, 200, {"blue"}, {"summer"}, "tight", 'top', "processed\\IMG_1479.png")
    top3 = Item(None, "Pacsun", None, 200, {"red"}, {"summer", "spring"}, "tight", 'top', "processed\\IMG_1473.png")
    top4 = Item(None, "bm", None, 200,  {"white"}, {"summer", "spring"}, "tight", 'top', "processed\\IMG_1470.png")
    top5 = Item(None, "long", None, 200, {"green"},{"summer"},"well-fit", "top", "processed\\8IMG_2113.png")
    bot1 = Item(None, "chuu", None, 200, {"black"}, {"summer", "fall"}, "baggy", 'bottom', "processed\\IMG_1475.png")
    bot2 = Item(None, "jean", None, 200, {"lightBlue"}, {"summer"}, "well-fit", 'bottom', "processed\\IMG_1476.png")
    bot3 = Item(None, "vjean", None, 200, {"blue"}, {"summer"}, "baggy", "bottom", "processed\\6IMG_1477.png")

    print('top list = ', Item.instances['top'])
    print('bottom list = ', Item.instances['bottom'])
    app.my_good_outfits = generateAllGoodOutfits(Item.instances['top'], Item.instances['bottom'])

    print('good outfits: ', app.my_good_outfits)


    print('Testing display first 4 outfits')

    # displayed outfits contains a list of outfit being displayed
    app.displayed_outfits = []

    print('size of good outfits = ', len(app.my_good_outfits))


    # print('good outfits: ', my_good_outfits)

    # # now I have a list of color matched good outfits

    print('Testing display first 4 outfits')


    #app.my_good_outfits, app.displayed_outfits = get4Outfits(app.my_good_outfits, app.displayed_outfits)
    get4Outfits(app.my_good_outfits, app.displayed_outfits)
    print("displayed outfits: ", app.displayed_outfits)
    print('size of good outfits after displayed = ', len(app.my_good_outfits))
    app.recycled = []
    # app.finadd = Outfit(top1, bot2)
    # #app.finadd.append(Outfit(top2, bot2))
    app.numCols = 4
    app.itemSize = (app.width//app.numCols, 230) 
    app.itemsPerRow = app.numCols
    app.scrollOffset = 30
    app.saved_outfits = []
    app.userPrefMode = False
    app.userPrefColors = []
    app.bgCol = rgb(129,137,120)
    app.gray = rgb(165,160,156) 
    app.lightg = rgb(173,173,173)
    app.accent = rgb(126,147,146) 
    #mutedBeige = rgb(205, 210, 203)
    app.mutedBeige = rgb(222, 220, 211)


def generateSeasonData():
  seasons = {
    "spring": (
        ("Average Range", (45, 70)),
        ("Early Spring", (40, 60)),
        ("Late Spring", (55, 75))
    ),
    "summer": (
        ("Average Range", (70, 90)),
        ("Early Summer", (65, 85)),
        ("Peak Summer", (80, 100))
    ),
    "autumn": (
        ("Average Range", (50, 70)),
        ("Early Autumn", (60, 80)),
        ("Late Autumn", (40, 60))
    ),
    "winter": (
        ("Average Range", (20, 50)),
        ("Mild Winter Regions", (30, 60)),
        ("Harsh Winter Regions", (-10, 30))
    )
  }
  return seasons

def getSeasonFromTemp(temp):
    data = generateSeasonData()
    for season in data:  # Iterate through keys (seasons)
        ranges = data[season]  # Access the range tuples for each season
        for time, (low, high) in ranges:
            if low >= temp and temp <= high:
                return season   # Return the season when a match is found
    
    return "Invalid season"  # Return this if no range matches



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
    colors = outfit.getColor()
    for color in colors:
      print("color in outfits: ", color)
      if color in user_preferences:
    #if outfit.getColor() in user_preferences:
        print('Found user preferred color match')
        return outfit
    # if outfit.getStyle() in user_preferences:
    #     print('Found user preferred type match')
    #     return outfit

  print('Warning: no user preferred match, return None')
  return None

def get4UserPreferredOutfits(outfits, preferred_outfits, user_preferences):
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
 
    outfits.remove(outfit)
    # add displayed outfit into display outfit list
    preferred_outfits.append(outfit)

  return outfits, preferred_outfits

def pickAGoodOutfitRandomly(outfits):
  """Randomly pick 1 outfit from good outfit list.

  Args:
    outfits: list of good outfits
  
  Return:
    A Good outfit or nil if none outfits is empty
  """
  if not outfits:
    print('Warning, outfit is empty.')
    return None
  outfit = choice(outfits)
  return outfit
import copy
def recycleDisplayedOutfits(displayed, recycled):

    print("displayed before clear:", displayed)
    recycled.extend(copy.deepcopy(displayed))  # Add deep copies to recycled
    print("recycled:", recycled)
    displayed.clear()  # Clear the original list

    # while displayed != []:
    #     recycled.append(displayed.pop(0))  # Remove and append the first item each time

    # print("displayed: ", displayed)

#recycleDisplayedOutfits([3,2,1,5,4,3,2], [])
    

def get4Outfits(outfits, displayed_outfits):
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
  tempList = []

  loop_range = loop_range = min(outfits_size, 4)

  for i in range(loop_range): # loop from 0 to 4
    outfit = pickAGoodOutfitRandomly(outfits)
    if not outfit:
        print('Warning: outfit is empty')
        return

    outfits.remove(outfit)
    # add displayed outfit into display outfit list
    displayed_outfits.append(outfit)

  return outfits, displayed_outfits

def gen_redrawAll(app):
    drawLabel("Generate Outfit!", 30, 50, size = 30, fill = app.gray, font = "Lora", align = "left")
    drawLine(20, 70 , 270 , 70, fill = app.gray, lineWidth = 2)
    if app.displayed_outfits == []:
        print("naurr")
        clothing = app.recycled[-1]
        itemWidth = 180 + 45
        itemHeight = 200
        #print("item hieght: ", itemHeight)
        x = (0 * app.itemSize[0]) + itemWidth / 2
        y = 0 * itemHeight + 200 - app.scrollOffset
        print("serialnum: ", clothing.top.serialNum)
        # imageTop = clothing.top.serialNum
        # # if clothing.isTop == "bottom":
        # imageBot = clothing.bottom.serialNum
        drawImage(clothing.top.serialNum, x, y, align="center", width=clothing.getSize(), height=clothing.getSize())
        bottom = y + 200 + 20
        drawImage(clothing.bottom.serialNum, x, bottom, align="center", width=clothing.getSize(), height=clothing.getSize())
        drawButton(650, 503, 155, 50, 10, fill=app.lightg)
        drawButton(650, 500, 150, 50, 10, fill=app.bgCol)
        drawLabel("reset", 700, 525, size = 17, bold = True, fill = "white", font = "Lora")
        drawButton(x - 75, 523, 155, 50, 10, fill=app.lightg)
        drawButton(x - 75, 520, 150, 50, 10, fill=app.bgCol)
        clothing.pos = (x, 550)
        #print("clothing position: ", clothing.pos)
        drawLabel("add to outfits", x, 545, size=18, fill = "white" ,font="Lora", bold = True)
    else:
        for i, clothing in enumerate(app.displayed_outfits):
            row = i // app.numCols  
            col = i % app.numCols
            itemWidth = 180 + 45
            itemHeight = 200
            #print("item hieght: ", itemHeight)
            x = (col * app.itemSize[0]) + itemWidth / 2
            y = row * itemHeight + 200 - app.scrollOffset
            print("serialnum: ", clothing.top.serialNum)
            # imageTop = clothing.top.serialNum
            # # if clothing.isTop == "bottom":
            # imageBot = clothing.bottom.serialNum
            drawImage(clothing.top.serialNum, x, y, align="center", width=clothing.getSize(), height=clothing.getSize())
            bottom = y + clothing.getSize() + 20
            drawImage(clothing.bottom.serialNum, x, bottom, align="center", width=clothing.getSize(), height=clothing.getSize())
            
            # Draw the "add to outfits" button
            drawButton(x - 75, 523, 155, 50, 10, fill=app.lightg)
            drawButton(x - 75, 520, 150, 50, 10, fill=app.bgCol)
            clothing.pos = (x, 550)
            #print("clothing position: ", clothing.pos)
            drawLabel("add to outfits", x, 545, size=18, fill = "white" ,font="Lora", bold = True)
        #         # Remove the displayed outfit from the good outfits list and add it to the displayed outfits
        #         app.my_good_outfits.remove(outfit)
        #         app.displayed_outfits.append(outfit)

        #     # Print the final status of Item instances for debugging
        #     print(Item.instances)

    # Draw the "regenerate" button at the end
    drawButton(650, 603-20, 155, 50, 10, fill = app.lightg)
    drawButton(650, 600-20, 150, 50, 10 ,fill = app.bgCol)
    drawLabel("regenerate", 720, 605, size=17, fill = "white", bold = True, font="Lora")

    drawButton(620, 43-10, 155, 50, 10, fill = app.lightg)
    drawButton(620, 40-10, 150, 50, 10, fill = app.bgCol)
    drawLabel("My Outfits", 680, 54, size = 17, fill = "white", bold = True, font = "Lora")

def gen_onMousePress(app, mouseX, mouseY):
    buttonWidth, buttonHeight = 150, 50 
    
    for clothing in app.displayed_outfits:
        buttonX, buttonY = clothing.pos  # Center position of the button
        
        # Calculate button boundaries
        left = buttonX - buttonWidth / 2
        right = buttonX + buttonWidth / 2
        top = buttonY - buttonHeight / 2
        bottom = buttonY + buttonHeight / 2
        
        # Check if the mouse click is within this button
        if left <= mouseX <= right and top <= mouseY <= bottom:
            # Add the selected outfit to the desired collection or perform an action
            print(f"Outfit selected: Top={clothing.top.name}, Bottom={clothing.bottom.name}")
            
            # Example action: add to the user's saved outfits
            if clothing in app.saved_outfits:
               app.saved_outfits.remove(clothing)
            else:
                app.saved_outfits.append(clothing)
            print("saved: ", app.saved_outfits)
            
            # Optional: Remove the outfit from the displayed list if needed
            #app.displayed_outfits.remove(clothing)
            
            break  # Stop checking after finding the clicked button
    if  app.saved_outfits != []:
        app.userPrefMode = True
    if (mouseX >= 650 and mouseX <= 800) and (mouseY >= 500 and mouseY <= 550):
        print("Reset")
        app.my_good_outfits = generateAllGoodOutfits(Item.instances['top'], Item.instances['bottom'])

        print('good outfits: ', app.my_good_outfits)
        app.displayed_outfits = []

        print('size of good outfits = ', len(app.my_good_outfits))
        print('Testing display first 4 outfits')

        get4Outfits(app.my_good_outfits, app.displayed_outfits)
        print("displayed outfits: ", app.displayed_outfits)
        print('size of good outfits after displayed = ', len(app.my_good_outfits))
        app.recycled = []

    if (mouseX >= 675 and mouseX <= 825) and (mouseY >= 575 and mouseY <= 625):
        print("regenerated")
        print("displayed before removal: ", app.displayed_outfits)
        recycleDisplayedOutfits(app.displayed_outfits, app.recycled)
        print("recycled: ", app.recycled)
        print("check length: ", len(app.displayed_outfits))
        #get4Outfits(app.my_good_outfits, app.displayed_outfits)
        if app.userPrefMode:
            for outfit in app.saved_outfits:
               app.userPrefColors.append(outfit.getColor())
            print("color, " , app.userPrefColors)
            get4UserPreferredOutfits(app.displayed_outfits, app.saved_outfits, app.userPrefColors)
            for outfit in app.displayed_outfits:
                if outfit in app.recycled:
                    app.displayed_outfits.remove(outfit)
            print("to be displayed next: ", app.displayed_outfits)

        elif len(app.displayed_outfits) <= 1:
            print("Thats the best outfit! Press regenerate to restart!")
            # app.displayed_outfits = []
            get4Outfits(app.my_good_outfits, app.displayed_outfits)
        elif len(app.displayed_outfits) == []:
           app.displayed_outfits = app.recycled[-1]
        else:
           get4Outfits(app.my_good_outfits, app.displayed_outfits)
        print("good outfits: ", app.my_good_outfits)
    if (mouseX >= 620 and mouseX <= 775) and (mouseY >= 30 and mouseY <= 80):
       #if app.saved_outfits != []:
        print("changing screens")
        setActiveScreen("outfits")

    
       
       

def outfits_redrawAll(app):
    numCols = 4 
    itemWidth = (app.width) // numCols  
    itemHeight = 200 
    overlapOffset = 70 
    
    rectHeight = itemHeight + itemHeight - overlapOffset
    drawLabel("Back", 50+30,50,align = "center", fill = "black", font = "Lora", size = 20)
    # drawRect(0, 80, app.width//2, 50,fill = None, border='black')
    # drawRect(app.width//2, 80, app.width//2, 50, fill = None, border='black')
    drawLabel("Outfits", 450, 50, size = 30, fill = "black", font = "Lora")

    for i, clothing in enumerate(app.saved_outfits):
        row = i // numCols  # Row number (integer division)
        col = i % numCols   # Column number (remainder)
        x = col * (itemWidth) 
        y = 250 + row * (rectHeight + 20) 
        drawRect(x, y, itemWidth, rectHeight, fill=None, border="black", borderWidth=0.5, align='left')
        drawImage(clothing.top.serialNum, x, y - itemHeight / 2 + 20, align="left", width=itemWidth - 40, height=itemHeight)
        drawImage(clothing.bottom.serialNum, x, y + itemHeight / 2 - overlapOffset + 20, align="left", width=itemWidth - 40, height=itemHeight)

def outfits_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 40 and mouseY <= 100):
        setActiveScreen("gen")
        

# def main():
#     runAppWithScreens(initialScreen='gen')
# main()
#     #when regnerate:
