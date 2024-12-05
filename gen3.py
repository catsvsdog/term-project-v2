from random import randint, choice
from tp06 import loadImage
from objects2 import Item, Outfit
from cmu_graphics import *
import os
import copy
import math

def drawButton(x, y, width, height, radius, fill='black', border=None, borderWidth=1):
    drawRect(x + radius, y, width - 2 * radius, height, fill=fill)
    drawRect(x, y + radius, width, height - 2 * radius, fill=fill)
    drawCircle(x + radius, y + radius, radius, fill=fill)
    drawCircle(x + width - radius, y + radius, radius, fill=fill) 
    drawCircle(x + radius, y + height - radius, radius, fill=fill)
    drawCircle(x + width - radius, y + height - radius, radius, fill=fill) 


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
    if not topList:
        print('Error, top is empty, please add tops.')
    if not bottomList:
        print('Error, bottom is empty, please add bottoms')
    else:
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
    app.url = "C:\\Users\\irisy\\Desktop\\15-112\\termProject\\term-project-v2\\dislike.jpg"

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
    app.scrollOffset = 0
    app.saved_outfits = []
    app.userPrefMode = False
    app.targetSeason = ""
    app.userPrefColors = []
    app.bgCol = rgb(129,137,120)
    app.gray = rgb(100,100,100)
    app.lightg = rgb(173,173,173)
    app.accent = rgb(126,147,146) 
    #mutedBeige = rgb(205, 210, 203)
    app.mutedBeige = rgb(222, 220, 211)
    app.title = f"{current_date.strftime('%B %Y')}"

    # app.outfitsAvailable = app.saved_outfits
    # app.outfitsWorn = []
    # app.selectedOutfit = None
    # app.addToCalendar = False
    app.boardLeft = 50
    app.boardTop = 100
    #app.rows = 
    app.cellBorderWidth = 2
    app.selection = None
    app.boardWidth = 800
    app.boardHeight = 630

    app.calendarOutfits = {}  # Dictionary to store outfits per day
    app.outfitsAvailable = []
    app.outfitsWorn = []
    app.calendarMode = False
    app.selectedOutfit = None
    app.addToCalendar = False
    app.added = False
    app.day = ""
    app.needsWash = False



#source: chatgpt
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

#source: chatgpt
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

def recycleDisplayedOutfits(displayed, recycled):

    print("displayed before clear:", displayed)
    recycled.extend(copy.deepcopy(displayed)) 
    print("recycled:", recycled)
    displayed.clear() 


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

  length = min(outfits_size, 4)

  for i in range(length): # loop from 0 to 4
    outfit = pickAGoodOutfitRandomly(outfits)
    if not outfit:
        print('Warning: outfit is empty')
        return

    outfits.remove(outfit)
    displayed_outfits.append(outfit)

  return outfits, displayed_outfits

def gen_redrawAll(app):
    drawLabel("Generate Outfit!", 150, 50, size = 25, fill = app.gray, bold = True, font = "Lora", align = "left")
    drawLine(0, 90 ,app.width, 90, fill = app.gray, lineWidth = 2)
    drawLabel("Back", 50, 50,align = "center", fill = app.gray, font = "Lora", bold = True, size = 20)
    # if app.displayed_outfits == []:
    #     print("naurr")
    #     clothing = app.recycled[-1]
    #     itemWidth = 180 + 45
    #     itemHeight = 200
    #     #print("item hieght: ", itemHeight)
    #     x = (0 * app.itemSize[0]) + itemWidth / 2
    #     y = 0 * itemHeight + 200 - app.scrollOffset
    #     print("serialnum: ", clothing.top.serialNum)

    #     drawImage(clothing.top.serialNum, x, y + 40, align="center", width=170, height=170)
    #     bottom = y + 170 + 20
    #     drawImage(clothing.bottom.serialNum, x, bottom, align="center", width=170, height = 170)
    #     drawButton(650, 503, 155, 50, 10, fill=app.lightg)
    #     drawButton(650, 500, 150, 50, 10, fill=app.bgCol)
    #     drawLabel("reset", 700, 525, size = 17, bold = True, fill = "white", font = "Lora")
    #     drawButton(x - 75, 523, 155, 50, 10, fill=app.lightg)
    #     drawButton(x - 75, 520, 150, 50, 10, fill=app.bgCol)
    #     clothing.pos = (x, 550)
    #     #print("clothing position: ", clothing.pos)
    #     drawLabel("add to outfits", x, 545, size=18, fill = "white" ,font="Lora", bold = True)
    #     drawLabel("Generate Outfit!", 100, 50, size = 30, bold = True, fill = app.gray, font = "Lora", align = "left")
    
    # drawLine(100, 70 , 270 + 80 , 70, fill = app.gray, lineWidth = 2)
    # drawLabel("Generate with weather", 380, 50, size = 20, bold = True, fill = app.gray, font = "Lora", align = "left")
    if app.displayed_outfits == [] and app.recycled != []:
        clothing = app.recycled[-1]
        itemWidth = 180 + 45
        itemHeight = 200
        #print("item hieght: ", itemHeight)
        x = (0 * 200) + itemWidth / 2
       
        y = 0 * itemHeight + 200 - app.scrollOffset
        print("serialnum: ", clothing.top.serialNum)

        drawImage(clothing.top.serialNum, x, y + 30, align="center", width=200, height=200)
        bottom = y + 200 + 20
        drawImage(clothing.bottom.serialNum, x, bottom, align="center", width=200, height=200)
        drawButton(650, 503, 155, 50, 10, fill=app.lightg)
        drawButton(650, 500, 150, 50, 10, fill=app.bgCol)
        drawLabel("reset", 700, 525, size = 17, bold = True, fill = "white", font = "Lora")
        drawButton(x - 75, 523, 155, 50, 10, fill=app.lightg)
        drawButton(x - 75, 520, 150, 50, 10, fill=app.bgCol)
        drawLabel("Thats the best outfit!", 550, 400, fill = app.gray, size = 20,bold = True, font = "Lora", align = "left")
        drawLabel("Press reset to restart!", 550, 440, fill = app.gray, size = 20, bold = True, font = "Lora", align = "left")
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
            y = row * itemHeight + 200
            print("scroll offset: ", app.scrollOffset)
            drawImage(clothing.top.serialNum, x, y + 40, align="center", width=170, height=170)
            bottom = y + 170 + 20
            drawImage(clothing.bottom.serialNum, x, bottom, align="center", width=170, height=170)
            
            # Draw the "add to outfits" button
            drawButton(x - 75, 473, 155, 50, 10, fill=app.lightg)
            drawButton(x - 75, 470, 150, 50, 10, fill=app.bgCol)
            clothing.pos = (x, 550)
            #print("clothing position: ", clothing.pos)
            drawLabel("add to outfits", x, 495, size=18, fill = "white" ,font="Lora", bold = True)
            drawImage(app.url, x, 550, align = "center", width = 50, height = 40)
    drawButton(650, 603-20, 155, 50, 10, fill = app.lightg)
    drawButton(650, 600-20, 150, 50, 10 ,fill = app.bgCol)
    drawLabel("regenerate", 720, 605, size=17, fill = "white", bold = True, font="Lora")

    drawButton(200, 603-20, 155, 50, 10, fill = app.lightg)
    drawButton(200, 600-20, 150, 50, 10 ,fill = app.bgCol)
    drawLabel("generate with", 208, 597, size=17, fill = "white", align = "left", bold = True, font="Lora")
    drawLabel("weather", 212, 615, size = 17, fill = "white",  align = "left",  bold = True, font = "Lora" )
    # drawButton(650, 43-10, 155, 50, 10, fill = app.lightg)
    # drawButton(650, 40-10, 150, 50, 10, fill = app.bgCol)
    drawLabel("My Outfits", 715, 50, size = 20, fill = app.gray, bold = True, font = "Lora")
    #drawLine(650, 70 ,750, 70, fill = app.gray, lineWidth = 2)

def gen_onMousePress(app, mouseX, mouseY):
    buttonWidth, buttonHeight = 150, 50 
    imWidth, imHeight = 50, 40
    if (mouseX >= 200 and mouseX <= 355) and (mouseY >= 583 and mouseY <= 630):
        while True:
            temp = app.getTextInput("Enter the temperature today (F): ")
            if getSeasonFromTemp(int(temp)) == "Invalid season":
                app.showMessage("Invalid Season, please try again")
            else:
                app.targetSeason = getSeasonFromTemp(int(temp))
                break
    if app.targetSeason != "":
        app.my_good_outfits = generateAllGoodOutfits(getSeasonTops(Item.instances['top'], app.targetSeason), getSeasonBottoms(Item.instances['bottom'], app.targetSeason))
        print("genn")
    if (mouseX >= 30 and mouseX <= 80) and (mouseY >= 40 and mouseY <= 65):
        print("ylo")
        setActiveScreen("main")
    for clothing in app.displayed_outfits:
        buttonX, buttonY = clothing.pos  # Center position of the button
        imageX, imageY = clothing.pos
        iLeft = imageX - imWidth / 2
        iRight = imageX + imWidth / 2
        iTop = imageY - imHeight / 2
        iBottom = imageY + imHeight/2
        print(iLeft,iRight,iTop,iBottom)

        # Calculate button boundaries
        left = buttonX - buttonWidth / 2
        right = buttonX + buttonWidth / 2
        top = buttonY - buttonHeight / 2
        bottom = buttonY + buttonHeight / 2
        print(left,right,top,bottom)
        
        if iLeft <= mouseX <= iRight and iTop <= mouseY <= iBottom:
            if clothing in app.saved_outfits:
                app.saved_outfits.remove(clothing)
            # app.recycled.remove(clothing)
            
            app.displayed_outfits.remove(clothing)

        # Check if the mouse click is within this button
        if left <= mouseX <= right and 470 <= mouseY <= 520:
            # Add the selected outfit to the desired collection or perform an action
            print(f"Outfit selected: Top={clothing.top.name}, Bottom={clothing.bottom.name}")
            print("clothing: ", clothing)
            # Example action: add to the user's saved outfits
            if clothing in app.saved_outfits:
               app.saved_outfits.remove(clothing)
            else:
                app.saved_outfits.append(clothing)
            print("saved: ", app.saved_outfits)
            
            
            break  # Stop checking after finding the clicked button
    if  app.saved_outfits != []:
        app.userPrefMode = True
    if (mouseX >= 650 and mouseX <= 800) and (mouseY >= 500 and mouseY <= 530):
        print("Reset")
        app.my_good_outfits.extend(app.recycled)
        app.recycled = []
        app.displayed_outfits = []
        
        for clothing in app.my_good_outfits:
           if clothing in app.saved_outfits:
              app.my_good_outfits.remove(clothing)
        get4Outfits(app.my_good_outfits, app.displayed_outfits)
        # print("displayed outfits: ", app.displayed_outfits)
        # print('size of good outfits after displayed = ', len(app.my_good_outfits))
        # app.recycled = []

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
               #app.userPrefStyle.append(outfit.getType())
            print("color, " , app.userPrefColors)
            #rint("")
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
    if (mouseX >= 650 and mouseX <= 800) and (mouseY >= 30 and mouseY <= 80):
       #if app.saved_outfits != []:
        print("changing screens")
        setActiveScreen("outfits")
   

def outfits_redrawAll(app):
    numCols = 4 
    itemWidth = (app.width) // numCols  
    itemHeight = 150 
    overlapOffset = 70 
    
    rectHeight = itemHeight + itemHeight - overlapOffset
    drawLabel("Back", 50+30,50,align = "center", fill = app.gray, font = "Lora", size = 20)
    drawLabel("Outfits", 450, 50, size = 30, fill = app.gray, font = "Lora", bold = True)
    drawLabel("Calendar", 700, 50, size = 25, align = "left", fill = app.gray, font = "Lora")
    drawLine(0, 90, 900, 90, fill = app.gray, lineWidth = 2)
    print("outfits: ", len(app.saved_outfits))
    print("is calendarMode: ", app.calendarMode)
    print("available outfits: ", app.outfitsAvailable)
    print("saved outfits: ", app.saved_outfits)
    if app.calendarMode:
       display = app.outfitsAvailable
    else:
       display = app.saved_outfits
    for i, clothing in enumerate(display):
        row = i // numCols  # Row number (integer division)
        col = i % numCols   # Column number (remainder)
        x = col * (itemWidth) 
        y = 250 + row * (rectHeight + 20) 
        drawRect(x, y, itemWidth, rectHeight, fill=None, border="black", borderWidth=0.5, align='left')
        drawImage(clothing.top.serialNum, x, y - itemHeight / 2 + 40, align="left", width=itemWidth - 40, height=itemHeight)
        drawImage(clothing.bottom.serialNum, x, y + itemHeight / 2 - overlapOffset + 20, align="left", width=itemWidth - 40, height=itemHeight)

def outfits_onMousePress(app, mouseX, mouseY):
    numCols = 4
    itemWidth = app.width // numCols  
    itemHeight = 150
    overlapOffset = 70
    rectHeight = itemHeight + itemHeight - overlapOffset
    startY = 250  # Starting Y-position for the outfits grid
    
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 40 and mouseY <= 100):
        # app.selectedOutfit = app.saved_outfits
        # app.outfitsAvailable = app.saved_outfits
        app.calendarMode = False
        setActiveScreen("gen")
    if (mouseX >= 700 and mouseX <= 800) and (mouseY >= 40 and mouseY <= 100):
        app.outfitsAvailable = app.saved_outfits.copy()
        print("outfit to calendar")
        app.calendarMode = True
        setActiveScreen("calendar") #testing
    print("add? ", app.addToCalendar)
    print("outfits available: ", app.outfitsAvailable)
    if app.addToCalendar and app.outfitsAvailable != []:
        for i, clothing in enumerate(app.outfitsAvailable):
            row = i // numCols
            col = i % numCols
            x = col * itemWidth
            y = 250 + row * (rectHeight + 20) - 115
            print(x,y)
            # Check if the mouse click is within this outfit's rectangle
            if (x <= mouseX <= x + 225) and (y <= mouseY <= y + 230):
                print(f"Outfit {i + 1} clicked!") 
                print("selected outfit: ", app.selectedOutfit)
                app.selectedOutfit = clothing
                app.outfitsAvailable.remove(clothing)
                if app.outfitsAvailable == []:
                    app.needsWash = True
                app.outfitsWorn.append(clothing)
                app.added = True
                app.calendarOutfits[app.day] = app.selectedOutfit
                app.selectedOutfit = None
                setActiveScreen("calendar")  
    # if app.outfitsAvailable == []:
    #     app.needsWash = True



import datetime

# Get the current month and year
current_date = datetime.date.today()
month = current_date.month
year = current_date.year

# Create a function to get the first day of the month and total days - chatgpt
def get_calendar_data(year, month):
    first_day = datetime.date(year, month, 1)
    start_day = first_day.weekday()  # Monday = 0, Sunday = 6
    total_days = (datetime.date(year, month + 1, 1) - first_day).days if month != 12 else 31
    return start_day, total_days



def calendar_redrawAll(app):
    start_day, total_days = get_calendar_data(year, month)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    cell_width, cell_height = 100, 110  # Adjusted cell size
    calendar_top = 110
    start_x = 60  # Starting X position of the calendar
    
    day_counter = 1
    
    for row in range(6):  # Max 6 weeks in a month
        for col in range(7):
            x = start_x + col * cell_width
            y = calendar_top +( row * cell_height )-app.scrollOffset
            if (row == 0 and col >= start_day) or (row > 0 and day_counter <= total_days):
                drawRect(x, y, cell_width, cell_height, fill=None, border=app.lightg)
                drawLabel(str(day_counter), x + cell_width // 2 - 30, y + cell_height // 2 - 30, size=14, font = "Lora", fill = app.gray)
                if day_counter in app.calendarOutfits:
                    clothing = app.calendarOutfits[day_counter]  # Assuming the outfit has an image attribute
                    #print("outfit image: ", outfit_image)
                    #drawImage(outfit_image, x + 20, y + 30, width=60, height=60) 
                    drawImage(clothing.top.serialNum, x + 20, y + 50, align="left", width=80, height=80)
                    drawImage(clothing.bottom.serialNum, x + 20, y + 70, align="left", width= 80, height= 80)
                day_counter += 1
    drawRect(0,0, app.width, 110, fill = "white")
    drawLabel(app.title, app.width // 2, 50, size=20, font = "Lora", fill = app.gray)
    if app.needsWash:
        color = rgb(80, 85, 90)
    else:
        color = app.lightg
    drawLabel("Wash", 700, 50, size = 20, align = "left", fill = color, font = "Lora")
    drawLabel("Back", 50+30,50,align = "center", fill = app.gray, font = "Lora", size = 20)
    for i, day in enumerate(days):
        drawLabel(day, start_x + i * cell_width + cell_width // 2, calendar_top - 10, size=13, font = "Lora", fill = app.gray, bold=True)



def calendar_onMousePress(app, mouseX, mouseY):
    # if app.outfitsAvailable == []:
    #     app.needsWash = True
    if (mouseX >= 700 and mouseX <= 800) and (mouseY >= 40 and mouseY <= 100):
        if app.needsWash:
            app.outfitsAvailable = app.outfitsWorn.copy()  # Restore outfits
            app.outfitsWorn = []  # Clear the worn outfits list
            print("Outfits washed and available again.")
            app.needsWash = False
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 40 and mouseY <= 100) :
       app.calendarMode = False #and not app.needsWash:
       print("hereeeeee-----------------------")
       setActiveScreen("outfits")
    col = 7
    row = 6
    start_day, total_days = get_calendar_data(year, month)
    cell_width, cell_height = 100, 110
    calendar_top = 110
    start_x = 60
    x = start_x + 7 * cell_width
    y = calendar_top + 6 * cell_height
    
    col = (mouseX - start_x) // cell_width
    row = (mouseY - calendar_top) // cell_height

    if 0 <= col < 7 and row >= 0:
        day_number = row * 7 + col + 1 - start_day
        if 1 <= day_number <= total_days:
            print("selected day: ", day_number)
            print(app.selectedOutfit)
            app.day = day_number
            if app.selectedOutfit == None:
                if day_number in app.calendarOutfits and app.calendarOutfits[day_number] is not None:
                    print("displayyyy")
                    setActiveScreen("display")
                else:
                    app.addToCalendar = True
                    # app.day = day_number
                    app.calendarMode = True
                    setActiveScreen("outfits")
            # else:
            #     # try:
            #     #     if app.calendarOutfits[app.day] in app.outfitsWorn:
            #     #         print("displayyyy")
            #     #         setActiveScreen("display")
            #     #     # elif app.outfitsAvailable == []:
            #     #     #     setActiveScreen("display")
            #     # except:
            #         if app.outfitsAvailable == []:
            #             setActiveScreen("display")
            #         # setActiveScreen("outfits")
            #     # if app.outfitsAvailable == []:
            #     #     setActiveScreen("display"
            
            print("available is empty?: ", app.outfitsAvailable)
            # if app.selectedOutfit is not None:
def calendar_onKeyPress(app, key):
    scrollStep = 20 
    maxScroll = max(0, 6 * 300 - (app.height - 110))
    if key == "down":
        app.scrollOffset = min(app.scrollOffset + scrollStep, maxScroll)
    elif key == "up":
        app.scrollOffset = max(app.scrollOffset - scrollStep, 0)

def display_redrawAll(app):
    clothing = app.calendarOutfits[app.day]
    
    drawImage(clothing.top.serialNum, app.width//2,app.height//2 - 100, align="center", width=200, height=200)
    drawImage(clothing.bottom.serialNum,app.width//2,app.height//2 + 100, align="center", width= 200, height= 200)
    drawLabel("Back", 50+30,50,align = "center", fill = app.gray, font = "Lora", size = 20)

def display_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 40 and mouseY <= 100):
       setActiveScreen("calendar")


# def main():
#     runAppWithScreens(initialScreen='gen')
# main()
#     #when regnerate:
