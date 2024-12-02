from cmu_graphics import *
#from interface2 import *
from tp06 import loadImage
#from itemObject import Item
import os
from PIL import Image, ImageDraw,ImageFont
# from generator import Top, Bottom, Outfit
from outfitObjects import Item
from generator2 import *
import sys

def get_current_directory():
  """Returns the absolute path of the current working directory."""
  return os.getcwd()


def construct_file_path(directory, filename):
  """Constructs the full file path by joining the directory and filename.

  Args:
    directory: The directory where the file is located.
    filename: The name of the file.

  Returns:
    A string representing the full file path.
  """
  return os.path.join(directory, filename)
 
def onAppStart(app):
    current_dir = get_current_directory()
   # app.url = "C:\\Users\\irisy\\Downloads\\cropflower.png"
    app.b1 = construct_file_path(current_dir, 'item.png')
    app.b2 = construct_file_path(current_dir, 'outfit.png')
    app.b3 = construct_file_path(current_dir, 'closet.png')  
    app.width = 900
    app.height = 650
    app.itemMode = False
    app.addItemMode = False
    app.files = None
    app.scrollOffset = 0
    app.genMode = False
    app.warMode = False
    app.home = True
    
    #Colors
    app.bgCol = rgb(129,137,120)
    app.gray = rgb(165,160,156) 
    app.lightg = rgb(173,173,173)
    app.accent = rgb(126,147,146) 
    #mutedBeige = rgb(205, 210, 203)
    app.mutedBeige = rgb(222, 220, 211)

    app.numCols = 4
    app.itemSize = (app.width//app.numCols, 230) 
    app.itemsPerRow = app.numCols
    app.items = []
    app.noFiles = True
    app.buttonCol = rgb(109, 119, 99)
    #app.url = "C:\\Users\\irisy\\Downloads\\57E9D6B0-AF0F-4258-BE81-FF09865C1789.png"
    #pilImage1 = Image.open(app.url)
    #app.cmuImage1 = CMUImage(pilImage1)

    app.word = "Enter here:"
    app.type = False
    app.season = set()
    app.moveOn = False
    app.colors = set()
    app.done = False
    app.finDone = False
    app.typeC = ""
    app.fit = ""
    app.tops = []
    app.bottoms = []
    app.seen = []
    app.rename = False
    app.curr = ""

def drawButton(x, y, width, height, radius, fill='black', border=None, borderWidth=1):
    drawRect(x + radius, y, width - 2 * radius, height, fill=fill)
    drawRect(x, y + radius, width, height - 2 * radius, fill=fill)
    drawCircle(x + radius, y + radius, radius, fill=fill)
    drawCircle(x + width - radius, y + radius, radius, fill=fill) 
    drawCircle(x + radius, y + height - radius, radius, fill=fill)
    drawCircle(x + width - radius, y + height - radius, radius, fill=fill) 

def start_redrawAll(app):
    bgCol = rgb(129,137,120)
    buttonCol = rgb(109, 119, 99)
    drawRect(0,0,app.width,app.height, fill = bgCol)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    #drawImage(app.url, 620,300, align = "center", width = 400, height = 400)
    drawStar(480, 180, 20, 4, fill = "white", roundness = 50)
    drawStar(730, 410, 20, 4, fill = "white", roundness = 50)
    #draw.text((280,300),"Welcome to", fill = "white", font = font)
    drawLabel("Welcome to ", 280, 290, size = 50, fill = "white", align = "center", font ="Lora")
    drawLabel("Outfit Planner", 300, 350, size = 55, fill = "white", align = "center", font ="Lora")
    drawButton(287.5 - 90, 397 + 20, 205-30,65-10,20, fill = "white")
    drawButton(290 -90,400 + 20,200-30,60-10,20,fill = buttonCol)
    drawLabel("Start", 280, 445, size = 25, fill = "white", bold = True, font = "Lora", align = "center")

def start_onMousePress(app,mouseX,mouseY):
    if (mouseX >= 170 and mouseX <= 340) and (mouseY >= 416 and mouseY <= 462):
        #print("hi")
        setActiveScreen("main")

def main_redrawAll(app):
    drawRect(0,0,app.width,app.height, fill = app.bgCol)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    drawLabel("Select One: ", 300, 200, size = 50, fill = "white", font = "Lora", align = "center" )
    #add item
    drawImage(app.b1, 200, 400, align = "center", width = 250, height = 250)
    drawLabel("Add an item", 170, 540, align = "center", fill = "white", size = 25, font = "Lora")
    drawLine(90, 555, 250, 555, fill = "white")
    #create outfit
    drawImage(app.b2, 460, 400, align = "center", width = 250, height = 250)
    drawLabel("Create an Outfit", 450, 540, align = "center", fill = "white", size = 25, font = "Lora")
    drawLine(350, 555, 550, 555, fill = "white")
    #wardrobe
    drawImage(app.b3, 720, 400, align = "center", width = 250, height = 250)
    drawLabel("Wardrobe", 700, 540, align = "center", fill = "white", size = 25, font = "Lora")
    drawLine(640, 555, 760, 555, fill = "white")

def main_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 90 and mouseX <= 250) and (mouseY >= 530 and mouseY <= 555):
        setActiveScreen("item")
    if (mouseX >= 350 and mouseX <= 550) and (mouseY >= 530 and mouseY <= 555):
        #print("gren")
        setActiveScreen("gen")
    if (mouseX >= 640 and mouseX <= 760) and  (mouseY >= 530 and mouseY <= 555):
        #print("war")
        setActiveScreen("wardrobe")


#Item screen
def item_onScreenActivate(app):
    pass
def item_redrawAll(app):
    drawRect(0,0,app.width, app.height, fill = app.bgCol)
    drawLabel("Add an item", 450, 90, align = "center", size = 30, font = "Lora", bold = True, fill = "white")
    drawLine(150, 140, 750, 140, fill="white", lineWidth=2)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    #drawLabel("", 200, 150, align  = "center")
    drawRect(300,180, 300, 350, fill = None, border = "white", borderWidth = 3)
    drawButton(347.5,298,205,65,20,fill = "white")
    drawButton(350,300,200,60,20,fill = app.buttonCol )
    drawLabel("Upload files", 450, 330, align = "center", font = "Lora", fill = "white", size = 25)

    #back button
    drawLabel("Back", 50+30,50+30,align = "center", fill = "white", font = "Lora", size = 20)
    #drawRect(40+40,40+40,60,30, align = "center", fill = "blue")

def item_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 347.5 and mouseX <= 347.5 + 205) and (mouseY >= 298 and mouseY <= 298 + 65):
        # file_path = app.getTextInput("Enter the path of the file to read: ")
        # app.files = 'Unknown' if file_path == '' else file_path
        #print("app.files: ", app.files)
        app.x = 100
        app.y = 100
        i = 0
        while app.files == None:
            file_path = app.getTextInput("Enter the path of the file to read: ")
            if file_path and os.path.exists(file_path):
                app.files = file_path
            else:
                app.showMessage("Invalid path! Please enter a valid directory.")
                app.files == None
        try:
            for item in loadImage(app.files):
                filename = os.path.splitext(os.path.basename(item))[0]
                print("namsssss: ", filename)
                Item(item, filename, (0, 0), (200, 200), (0))
                i += 1
            # Item.instances[0]
            app.noFiles = False
            setActiveScreen("main")
        except FileNotFoundError as e:
            app.showMessage(f"Error loading folder: {e}")

        #setActiveScreen("addItem")
    elif (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
        setActiveScreen("main")

#Wardrobe Screen
def wardrobe_onScreenActivate(app):
    #print("app.fileszzz: ", app.files)
    i = 0

def wardrobe_redrawAll(app):

    # print(app.noFiles)
    if app.noFiles:
        drawRect(0,0,app.width, app.height, fill = app.bgCol)
        drawLine(150, 140, 750, 140, fill="white", lineWidth=2)
        drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
        drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
        drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
        drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
        drawLabel("No clothes right now, click to upload!", 450, 120, size = 20, fill = "white", font = "Lora", bold= True)
        drawButton(450 - 30, 300,50, 50, 5, fill = app.lightg)
        drawLine(450 - 30, 325, 500-30, 325, fill = "white")
        drawLine(475 - 30, 300, 475-30, 350, fill = "white")
        drawLabel("Back", 50+30,50,align = "center", fill = "white", font = "Lora", size = 20)
    else:
        if app.files == None:
            pass
        else:
            for i, item in enumerate(Item.instances):
                # print("item name: ", item)
                row = i // app.numCols
                col = i % app.numCols
                itemWidth = 180 + 45
                itemHeight = item.size[1] + 50
                x = col * (app.itemSize[0])
                y = row * (itemHeight) + 130 - app.scrollOffset
                #x, y = item.pos
                #y += 100 
                drawRect(x, y, itemWidth, itemHeight, fill=None, border="black", borderWidth=0.5)
                drawImage(item.image, x + item.size[0] / 2 + 20, y + item.size[1] / 2, 
                        align="center", width=item.size[0], height=item.size[1])
                # drawLabel(item.name, x + 80, y + 250, align="center")

                # Store the bounds for click detection
                item.update_bounds(x, y, itemWidth, itemHeight) # Update bounds for the individual item
                # app.items.append(Item(item, "Brandy", (x,y),(180,230)))

        drawRect(0, 0, app.width, 130, fill='white')

        drawLabel("Wardrobe", 450, 50, size = 30, fill = "black", font = "Lora")
        drawLabel("Back", 50+30,50,align = "center", fill = "black", font = "Lora", size = 20)
        drawRect(0, 80, app.width//2, 50,fill = None, border='black')
        drawRect(app.width//2, 80, app.width//2, 50, fill = None, border='black')
        drawLabel('Items', app.width//4, 105, align='center', font = "Lora", size = 18, borderWidth = 0.5)
        drawLabel('Outfits', app.width//4*3, 105, align='center', font = "Lora", size = 18, borderWidth = 0.5)

        # for item in app.items:
        #     x, y = item.pos
        #     y += 100  # Adjust for header height
        #     y -= app.scrollOffset

        #     itemWidth = 180 + 45
        #     itemHeight = item.size[1] + 270  # Account for the text area



        # for item in app.items:
        #     x, y = item.pos
        #     y += 100
        #     y -= app.scrollOffset
        #     itemWidth = 180 + 45
        #     itemHeight = item.size[1] + 270
        #     if y + itemHeight > 100 and y < app.height:   # Only draw items within the visible area
        #           # Account for the text area below
        #         # drawRect(x, y, itemWidth, itemHeight, fill=None, border="black", borderWidth=0.5)
        #         # drawImage(item.image, x + item.size[0] / 2 + 20, y + item.size[1] / 2, align="center", width=item.size[0], height=item.size[1])
        #         # drawLabel(item.name, x + 80, y + 250, align="center")
        #         # Store bounds for click detection
        #         drawRect(x, y, 180 + 45, item.size[1], fill=None, border="black", borderWidth = 0.5)
        #         drawRect(x, y+230, 180 + 45, 40, fill = None, border = "black", borderWidth = 0.5)
        #         #drawImage(item.image, *item.pos, align='center', width = item.size[0], height=item.size[1])
        #         drawImage(item.image, x + item.size[0] / 2 + 20, y + item.size[1] / 2, align="center",width=item.size[0], height=item.size[1])
        #         drawLabel(item.name, x+80, y+, align = "center")
     
        #         item.bounds = (x, y, x + itemWidth, y + itemHeight)
def wardrobe_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 40 and mouseY <= 100):
        setActiveScreen("main")
    elif (mouseX >= 325 and mouseX <= 450) and (mouseY >= 300 and mouseY <= 350):
        if app.noFiles:
            setActiveScreen("item")
    elif (mouseX >= 0 and mouseX <= app.width//2) and (mouseY >= 80 and mouseY <= 130):
        setActiveScreen("wardrobe")
    elif (mouseX >= app.width//2 and mouseX <= app.width *2) and (mouseY >= 80 and mouseY <= 130):
        setActiveScreen("outfit") #testing
    else:
        # Iterate through each item to check if the click is within its bounds
        for item in Item.instances:
            if item.bounds is not None:  # Check if bounds are set
                x1, y1, x2, y2 = item.bounds  # Get the bounds of the item
                if x1 <= mouseX <= x2 and y1 <= mouseY <= y2:  # Check if mouse is inside the bounds
                    app.selectedItem = item  # Update the selected item
                    app.num = item.name
                    print("item name: ", item.name)
                    if item.name not in app.seen:
                        app.seen.append(item.name)
                        setActiveScreen("nameItem")
                    else:
                        app.rename = True
                        # app.curr = item
                        # setActiveScreen("temp")
                        print(app.selectedItem)
                        if app.tops != []:
                            print("tops:", app.tops)
                            for i in app.tops:
                                print(i, app.selectedItem.name, i.serialNum)
                                if app.selectedItem.name == i.serialNum:
                                    print("check")
                                    app.curr = i
                                    app.season = app.curr.season
                                    app.color = app.curr.color
                                    app.fit = app.curr.type
                                    setActiveScreen("temp")
                        if app.bottoms != []:
                            print("bottoms:", app.bottoms)
                            for i in app.bottoms:
                                print(i, app.selectedItem.name, i.serialNum)
                                if app.selectedItem.name == i.serialNum:
                                    print("check")
                                    app.curr = i
                                    app.season = app.curr.season
                                    app.color = app.curr.color
                                    app.fit = app.curr.type
                                    setActiveScreen("temp")
                        print("already seen")
                    print("seen: ", app.seen)
                        # setActiveScreen("displayInfo")
                    #print(f"Clicked on {item.name}")
                    
                    #setActiveScreen("nameItem")  # Example action
   
def wardrobe_onKeyPress(app, key):
    scrollStep = 20  # Increase speed for smoother scrolling
    maxScroll = max(0, len(Item.instances) * 300 - (app.height - 150))  # Account for header

    if key == "down":
        app.scrollOffset = min(app.scrollOffset + scrollStep, maxScroll)
        # print(app.scrollOffset)
    elif key == "up":
        app.scrollOffset = max(app.scrollOffset - scrollStep, 0)
        # print(app.scrollOffset)

def temp_redrawAll(app):
    buttonCol = rgb(109, 119, 99)
    #top1 = Top("shirt", "red", {"summer", "spring"}, "wellfit")
    drawRect(0,0,app.width,app.height, fill = app.bgCol)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    drawButton(200, 100, 500, 350, 20, fill = "white")
    drawButton(205, 105, 390 + 100, 290 + 50, 20, fill = app.bgCol)
    drawLabel("Click on what you wish to modify", 430, 150, size = 25, fill = "white", font= "Lora", bold = True)
    #drawButton(240, 250, 400, 50, 10, fill = buttonCol)
    col = {"green", "white"}
    print("app.curr: ", app.curr)

    drawLabel(f"Name: {app.curr.name}", 230, 200, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
    drawLabel(f"Color: {app.curr.getColor()}", 230, 250, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
    drawLabel(f"Season: {app.curr.getSeason()}", 230, 300, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
    drawLabel(f"Style: {app.curr.type}", 230, 350, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
    # if isinstance(app.curr, Top):
    #     drawLabel(f"Type: {app.curr.isTop}", 230, 400, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
    # elif isinstance(app.curr, Bottom):
    #     drawLabel(f"Type: {app.curr.isBottom}", 230, 400, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
    drawLabel("Back", 50+30,50+30,align = "center", fill = "white", font = "Lora", size = 20)
    drawButton(497, 497.5, 205,65-10,10, fill = "white")
    drawButton(500,500,200,60-10,10,fill = buttonCol)
    drawLabel("Done", 570, 525, fill = "white", size = 25, font = "Lora", align = "center")

def temp_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 230 and mouseX <= 420) and (mouseY >= 190 and mouseY <= 210):
        setActiveScreen("nameItem")
        app.rename = True
    if (mouseX >= 230 and mouseX <= 400) and (mouseY >= 245 and mouseY <= 260):
        setActiveScreen("colors")
    if (mouseX >= 230 and mouseX <= 450) and (mouseY >= 295 and mouseY <= 310):
        setActiveScreen("season")
    if (mouseX >= 230 and mouseX <= 300) and (mouseY >= 345 and mouseY <= 360):
        setActiveScreen("fit")
    # if (mouseX >= 230 and mouseX <= 400) and (mouseY >= 395 and mouseY <= 410):
    #     setActiveScreen("fit")
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
        setActiveScreen("wardrobe")
    if (mouseX >= 497 and mouseX <= 700) and (mouseY >= 500 and mouseY <= 550):
        app.rename = False
        setActiveScreen("wardrobe")

# def wardrobe_onMousePress(app, mouseX, mouseY):

#     if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
#         setActiveScreen("main")
#     elif (mouseX >= 325 and mouseX <= 450) and (mouseY >= 300 and mouseY <= 350):
#         setActiveScreen("item")
#     else:
#         for item in app.items:
#             x1, y1, x2, y2 = item.pos  # Use the pre-calculated bounds
#             if x1 <= mouseX <= x2 and y1 <= mouseY <= y2:
#                 # Update or perform an action for the clicked item
#                 app.selectedItem = item
#                 setActiveScreen("nameItem")

    # item.bounds = (x, y, x + itemWidth, y + itemHeight)
    # if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
    #     setActiveScreen("main")
    # elif (mouseX >= 325 and mouseX <= 450) and (mouseY >= 300 and mouseY <= 350):
    #     setActiveScreen("item")
    # else:
    #     for item in app.items:
    #         x1, y1, x2, y2 = item.bounds
    #         if x1 <= mouseX <= x2 and y1 <= mouseY <= y2:
    #             # Update or perform an action for the clicked item
    #             app.selectedItem = item
    #             setActiveScreen("nameItem")
    #             #print(f"Clicked on {item.name}")
    #             #setActiveScreen("itemDetails")  # Example action

 
def nameItem_redrawAll(app):
    buttonCol = rgb(109, 119, 99)
    drawRect(0,0,app.width,app.height, fill = app.bgCol)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    drawButton(200, 100, 500, 350, 20, fill = "white")
    drawButton(205, 105, 390 + 100, 290 + 50, 20, fill = app.bgCol)
    drawLabel("What brand is your item?", 430, 180, size = 30, fill = "white", font= "Lora", bold = True)
    drawButton(240, 250, 400, 50, 10, fill = buttonCol)
    #drawLabel("Enter Here: ", 250, 275, fill = "white", size = 25, font = "Lora", align = "left", bold = True)
    drawLabel(f"{app.word}", 250, 275, fill = "white", size = 25, font = "Lora", align = "left", bold = True)
    drawStar(170, 180, 20, 4, fill = "white", roundness = 50)
    drawStar(730, 410, 20, 4, fill = "white", roundness = 50)
    drawButton(287.5 +40, 337+10, 205,65-10,10, fill = "white")
    drawButton(290+40,340+10,200,60-10,10,fill = buttonCol)
    drawLabel("Next", 380, 375, fill = "white", size = 25, font = "Lora", align = "center")
    drawLabel("Back", 50+30,50+30,align = "center", fill = "white", font = "Lora", size = 20)

def nameItem_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 240 and mouseX <= 640) and (mouseY >= 250 and mouseY <= 300):
        app.type = True
        app.word = ""
    if (mouseX >= 328 and mouseX <= 530) and (mouseY >= 350 and mouseY <= 400):
        if app.word != "Enter here:":
            if app.rename:
                app.curr.changeName(app.word)
                setActiveScreen("temp")
            else:
                setActiveScreen("season")
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
        if app.rename:
            print("new: ", app.word)
            setActiveScreen("temp")
        else:
            if (app.tops == [] and app.bottoms == []):
                app.seen.remove(app.num)
            setActiveScreen("wardrobe")
        
def nameItem_onKeyPress(app, key):
    if app.type:
        if len(key) == 1 and key.isalpha():
            app.word += key
        if key == "backspace":
            app.word = app.word[:-1]

def season_redrawAll(app):
    buttonCol = rgb(109, 119, 99)
    drawRect(0,0,app.width,app.height, fill = app.bgCol)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    drawButton(200, 100, 500, 350, 20, fill = "white")
    drawButton(205, 105, 390 + 100, 290 + 50, 20, fill = app.bgCol)
    drawLabel("What season is your item?", 430, 180-30, size = 30, fill = "white", font= "Lora", bold = True)
    drawLabel("(can select multiple)", 430, 220-30, size = 25, fill = "white", font = "Lora", bold=True)
    #drawButton(240, 250, 400, 50, 10, fill = buttonCol)
    drawButton(210 + 50, 337 - 40, 150, 65 - 10, 10, fill="white")
    if "Spring" in app.season:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(212 + 50, 340 - 40, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Spring", 210 + 50 + 75, 337 - 40 + 27, fill="white", font="Lora", size=20)  # Adjusted label position

    # Summer Button
    if "Summer" in app.season:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 50, 337 - 110, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 50, 340 - 110, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Summer", 210 + 50 + 75, 337 - 110 + 27, fill="white", font="Lora", size=20)  # Adjusted label position

    if "Autumn" in app.season:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 250, 337 - 40, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 250, 340 - 40, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Autumn", 210 + 250 + 75, 337 - 40 + 27, fill="white", font="Lora", size=20)  # Adjusted label position

    if "Winter" in app.season:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 250, 337 - 110, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 250, 340 - 110, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Winter", 210 + 250 + 75, 337 - 110 + 27, fill="white", font="Lora", size=20)  # Adjusted label position

    drawStar(170, 180, 20, 4, fill = "white", roundness = 50)
    drawStar(730, 410, 20, 4, fill = "white", roundness = 50)
    drawButton(287.5 +40, 337+30, 205,65-10,10, fill = "white")
    nextCol = rgb(109, 119, 99)
    drawButton(290+40,340+30,200,60-10,10,fill = nextCol)
    drawLabel("Next", 380, 375+20, fill = "white", size = 25, font = "Lora", align = "center")
    drawLabel("Back", 50+30,50+30,align = "center", fill = "white", font = "Lora", size = 20)
    
def season_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 260 and mouseX <= 410) and (mouseY >= 230 and mouseY <= 280):
        if "Summer" in app.season:
            app.season.remove("Summer")
        else:
            app.season.add("Summer")
    if (mouseX >= 260 and mouseX <= 410) and (mouseY >= 300 and mouseY <= 350):
        if "Spring" in app.season:
            app.season.remove("Spring")
        else:
            app.season.add("Spring")
    if (mouseX >= 460 and mouseX <= 610) and (mouseY >= 230 and mouseY <= 280):
        if "Winter" in app.season:
            app.season.remove("Winter")
        else:
            app.season.add("Winter")
    if (mouseX >= 460 and mouseX <= 610) and (mouseY >= 300 and mouseY <= 350):
        if "Autumn" in app.season:
            app.season.remove("Autumn")
        else:
            app.season.add("Autumn")
    if app.season != set(): app.moveOn = True
    if (mouseX >= 328 and mouseX <= 530) and (mouseY >= 370 and mouseY <= 420):
        if app.moveOn:
            if app.rename:
                app.curr.changeSeason(app.season)
                setActiveScreen("temp")
            else:
                print(app.season)
                setActiveScreen("colors")
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
        if app.rename:
            setActiveScreen("temp")
        else:
           setActiveScreen("nameItem")

def colors_redrawAll(app):
    buttonCol = rgb(109, 119, 99)
    bgCol = rgb(129, 137, 120)  # Sage green
    drawRect(0,0,app.width,app.height, fill = app.bgCol)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    drawButton(200, 100, 500, 350, 20, fill = "white")
    drawButton(205, 105, 390 + 100, 290 + 50, 20, fill = app.bgCol)

    drawLabel("What color is your item?", 430, 180-30, size = 30, fill = "white", font= "Lora", bold = True)
    drawLabel("(can select multiple)", 430, 220-30, size = 25, fill = "white", font = "Lora", bold=True)
    lightBlue = rgb(102, 163, 212)
    gray = rgb(92,92,92)
    beige = rgb(207,195,175)
    lightGray = rgb(194,194,194)
    brown = rgb(74,46,10)
    orange = rgb(215,121,40)
    pink = rgb(215,121,158)
    colors = ["black", brown, "blue",lightBlue, "purple", pink, orange]
    col = ["green", "yellow", "red", gray, beige, "white", lightGray]
    selectedCol = rgb(109, 119, 99)
    j = 0
    for i in range(200, 680, 70):
        # if colors[j] in app.colors:
        #     drawButton(18 + i, 247, 45, 45, 10, fill = selectedCol)
        #     drawButton(20 + i, 250, 40, 40, 10, fill = colors[j])
        # else:
        drawButton(20 + i, 250, 40, 40, 10, fill = colors[j])
        j += 1
    j = 0
    for i in range(200, 680, 70):
        # if col[j] in app.colors:
        #     #drawButton(18 + i, 297, 45, 45, 10, fill = selectedCol)
        #     drawButton(20 + i, 300, 40, 40, 10, fill = col[j])
        # else:
        drawButton(20 + i, 300, 40, 40, 10, fill = col[j])
        j +=1 
    drawStar(170, 180, 20, 4, fill = "white", roundness = 50)
    drawStar(730, 410, 20, 4, fill = "white", roundness = 50)
    drawButton(287.5 +40, 337+30, 205,65-10,10, fill = "white")
    drawButton(290+40,340+30,200,60-10,10,fill = buttonCol)
    drawLabel("Next", 380, 375+20, fill = "white", size = 25, font = "Lora", align = "center")
    drawLabel("Back", 50+30,50+30,align = "center", fill = "white", font = "Lora", size = 20)

def colors_onMousePress(app, mouseX, mouseY):
    if (mouseY >= 250 and mouseY <= 290):
        if (mouseX >= 220 and mouseX <= 260):
            if "black" in app.colors:
                app.colors.remove("black")
            else:
                app.colors.add("black")
        if (mouseX >= 290 and mouseX <= 330):
            if "brown" in app.colors:
                app.colors.remove("brown")
            else:
                app.colors.add("brown")
        if (mouseX >= 360 and mouseX <= 400):
            if "blue" in app.colors:
                app.colors.remove("blue")
            else:
                app.colors.add("blue")
        if (mouseX >= 430 and mouseX <= 470):
            if "lightBlue" in app.colors:
                app.colors.remove("lightBlue")
            else:
                app.colors.add("lightBlue")
        if (mouseX >= 500 and mouseX <= 540):
            if "purple" in app.colors:
                app.colors.remove("purple")
            else:
                app.colors.add("purple")
        if (mouseX >= 570 and mouseX <= 610):
            if "pink" in app.colors:
                app.colors.remove("pink")
            else:
                app.colors.add("pink")
        if (mouseX >= 640 and mouseX <= 680):
            if "orange" in app.colors:
                app.colors.remove("orange")
            else:
                app.colors.add("orange")

    if (mouseY >= 300 and mouseY <= 340):
        if (mouseX >= 220 and mouseX <= 260):
            if "green" in app.colors:
                app.colors.remove("green")
            else:
                app.colors.add("green")
        if (mouseX >= 290 and mouseX <= 330):
            if "yellow" in app.colors:
                app.colors.remove("yellow")
            else:
                app.colors.add("yellow")
        if (mouseX >= 360 and mouseX <= 400):
            if "red" in app.colors:
                app.colors.remove("red")
            else:
                app.colors.add("red")
        if (mouseX >= 430 and mouseX <= 470):
            if "gray" in app.colors:
                app.colors.remove("gray")
            else:
                app.colors.add("gray")
        if (mouseX >= 500 and mouseX <= 540):
            if "beige" in app.colors:
                app.colors.remove("beige")
            else:
                app.colors.add("beige")
        if (mouseX >= 570 and mouseX <= 610):
            if "white" in app.colors:
                app.colors.remove("white")
            else:
                app.colors.add("white")
        if (mouseX >= 640 and mouseX <= 680):
            if "lightGray" in app.colors:
                app.colors.remove("lightGray")
            else:
                app.colors.add("lightGray")
    print(app.colors)
    if app.colors != set():
        app.done = True
    if (mouseX >= 328 and mouseX <= 530) and (mouseY >= 370 and mouseY <= 420):
        if app.done:
            if app.rename:
                app.curr.changeColor(app.colors)
                setActiveScreen("temp")
            else:
                print(app.colors)
                setActiveScreen("type")
    elif (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
        if app.rename:
            setActiveScreen("temp")
        else:
            setActiveScreen("season")

def type_redrawAll(app):
    buttonCol = rgb(109, 119, 99)
    drawRect(0,0,app.width,app.height, fill = app.bgCol)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    drawButton(200, 100, 500, 350, 20, fill = "white")
    drawButton(205, 105, 390 + 100, 290 + 50, 20, fill = app.bgCol)
    drawLabel("Is your item a top or bottom?", 430, 180-30, size = 30, fill = "white", font= "Lora", bold = True)
    
    if "Top" in app.typeC:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 50, 250, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 50, 253, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Top", 210 + 50 + 75, 250 + 27, fill="white", font="Lora", size=20)  # Adjusted label position

    if "Bottom" in app.typeC:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 250, 250, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 250, 253, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Bottom", 210 + 250 + 75, 250 + 27, fill="white", font="Lora", size=20)  # Adjusted label position
    buttonCol = rgb(109, 119, 99)
    drawStar(170, 180, 20, 4, fill = "white", roundness = 50)
    drawStar(730, 410, 20, 4, fill = "white", roundness = 50)
    drawButton(287.5 +40, 337+30, 205,65-10,10, fill = "white")
    drawButton(290+40,340+30,200,60-10,10,fill = buttonCol)
    drawLabel("Next", 380, 375+20, fill = "white", size = 25, font = "Lora", align = "center")
    drawLabel("Back", 50+30,50+30,align = "center", fill = "white", font = "Lora", size = 20)

def type_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 260 and mouseX <= 410) and (mouseY >= 250 and mouseY <= 300):
        app.typeC = ("Top")
        app.finDone = True
    if (mouseX >= 460 and mouseX <= 610) and (mouseY >= 250 and mouseY <= 300):
        app.typeC = ("Bottom")
        app.finDone = True
    if (mouseX >= 328 and mouseX <= 530) and (mouseY >= 370 and mouseY <= 420):
        if app.finDone:
            print(app.typeC)
            print("done")
            # if app.rename:
            #     # app.curr.changeType = app.typeC
            #     setActiveScreen("temp")
            # else:
            setActiveScreen("fit")
            # if app.typeC == "Top":
            #     tops.append(Top(app.word, app.colors, app.season))

    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
        if app.rename:
            setActiveScreen("temp")
        else:
            setActiveScreen("colors")

def fit_redrawAll(app):
    buttonCol = rgb(109, 119, 99)
    drawRect(0,0,app.width,app.height, fill = app.bgCol)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    drawButton(200, 100, 500, 350, 20, fill = "white")
    drawButton(205, 105, 390 + 100, 290 + 50, 20, fill = app.bgCol)
    drawLabel("Select the fit", 430, 180-30, size = 30, fill = "white", font= "Lora", bold = True)
    
    if "baggy" in app.fit:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 50, 250-50, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 50, 253-50, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Baggy", 210 + 50 + 75, 250 + 27-50, fill="white", font="Lora", size=20)  # Adjusted label position

    if "tight" in app.fit:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 250, 250-50, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 250, 253-50, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Tight", 210 + 250 + 75, 250 + 27-50, fill="white", font="Lora", size=20)  # Adjusted label position
    
    if "well-fit" in app.fit:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 150, 250 + 70-50, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 150, 253 + 70-50, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Well-fit", 210 + 150 + 75, 250 + 27 + 70-50, fill="white", font="Lora", size=20)  # Adjusted label position
    buttonCol = rgb(109, 119, 99)

    drawStar(170, 180, 20, 4, fill = "white", roundness = 50)
    drawStar(730, 410, 20, 4, fill = "white", roundness = 50)
    drawButton(287.5 +40, 337+30, 205,65-10,10, fill = "white")
    drawButton(290+40,340+30,200,60-10,10,fill = buttonCol)
    drawLabel("Next", 380, 375+20, fill = "white", size = 25, font = "Lora", align = "center")
    drawLabel("Back", 50+30,50+30,align = "center", fill = "white", font = "Lora", size = 20)
    
def fit_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 260 and mouseX <= 410) and (mouseY >= 200 and mouseY <= 255):
        app.fit = "baggy"
    if (mouseX >= 460 and mouseX <= 610) and (mouseY >= 200 and mouseY <= 255):
        app.fit = "tight"
    if (mouseX >= 360 and mouseX <= 510) and (mouseY >= 270 and mouseY <= 325):
        app.fit = "well-fit"
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 50 and mouseY <= 100):
        if app.rename:
            setActiveScreen("temp")
        else:
            setActiveScreen("type")
    print(app.fit)
    if app.fit != "":
        if (mouseX >= 328 and mouseX <= 530) and (mouseY >= 370 and mouseY <= 420):

            if app.rename:
                app.curr.changeType(app.fit)
                setActiveScreen("temp")
            else:
                setActiveScreen("wardrobe")
            
                if app.typeC == "Top":
                    app.tops.append(Top(app.word, app.colors, app.season, app.fit, app.num))

                elif app.typeC == "Bottom":
                    app.bottoms.append(Bottom(app.word, app.colors, app.season, app.fit, app.num))
                if app.tops != [] or app.bottoms != []:
                    app.word = ""
                    app.colors = set()
                    app.season = set()
                    app.typeC = ""
                    app.fit = ""
                    app.num = 0
            print(app.tops, app.bottoms)
            

def gen_redrawAll(app):
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
    drawRect(0, 0, app.width, app.height, fill = app.bgCol)
    drawLine(150, 140, 750, 140, fill="white", lineWidth=2)
    drawLine(0, 50, 900, 50, fill = "white", lineWidth = 4)
    drawLine(0, 600, 900, 600, fill = "white",lineWidth = 4)
    drawLine(50, 0, 50, 650, fill = "white", lineWidth = 4)
    drawLine(850, 0, 850, 650, fill = "white", lineWidth = 4)
    drawLabel("Back", 50+30,50+30,align = "center", fill = "white", font = "Lora", size = 20)
    drawLabel("Outfits", 450, 100, size = 30, fill = "white", font = "Lora")
    
    if app.files != None:
        topsSorted = []
        botsSorted = []
        # print("season outfpit: ", seasons(app.tops, app.bottoms, "summer",topsSorted, botsSorted))
        topsSorted, botsSorted = seasons(app.tops, app.bottoms, "Summer",topsSorted, botsSorted)
        
        # for top in app.tops:
        #     print("get season: ", top.getSeason())
        #     if "summer" in top.getSeason() :
        #         topsSorted.append(top)
        #     print("sorted list for now: ", topsSorted)
        # for bot in app.bottoms:
        #     if "summer" in bot.getSeason():
        #         botsSorted.append(bot)
        print("tops: ", topsSorted)
        print("bottoms: ", botsSorted)
        result = []
        (generateAllPossibleOutfits(result, topsSorted, botsSorted))
        for i in app.tops:
            print("season: ", i.getSeason())
        print("final four: ", displayOutfits(result))
        final = displayOutfits(result)
        print("item instances: ", Item.instances)
        for item in (Item.instances):
            for clothing in final:
                if item.serialNum == clothing.serialNum:
                    x = 250
                    y = 100
                    drawImage(item.image, x + item.size[0] / 2 + 20, y + item.size[1] / 2, align="center", width=item.size[0], height=item.size[1])
        

def gen_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
        setActiveScreen("main")

def outfit_redrawAll(app):
    x = 250
    y = 100
    for item in (Item.instances):
        drawImage(item.image, x + item.size[0] / 2 + 20, y + item.size[1] / 2, align="center", width=item.size[0], height=item.size[1])
        

def main():
  """ main entrypoint of the program."""
  test_generator()
  sys.exit(0)
  runAppWithScreens(initialScreen='item')


if __name__ == "__main__":
    main()


#itemmode -> add item:

# def addItem_redrawAll(app):
#     file_path = input("Enter the path of the file to read: ")
#     print("temp")

# def addItem_onMousePress(app, mouseX, mouseY):
#     #if (mouseX >= 350 and mouseX <= 550) and (mouseY >= 300 and mouseY <= 360):
#     print("hiii")
#     file_path = app.getTextInput("Enter the path of the file to read: ")
#     app.file = 'Unknown' if file_path == '' else file_path
#         # message = f'This is a modal poup!  Your name is: {app.name}'
#         # app.showMessage(message)

        
# def onMousePress(app, mouseX, mouseY):
#     if (mouseX >= 97.5 and mouseX <= 303) and (mouseY >= 298 + 150 and mouseY <= 360+150):
#         app.itemMode = True
#     elif (mouseX >= 347.5 and mouseX <= 347.5 + 205) and (mouseY >= 450 and mouseY <= 510):
#         app.genMode = True
#     elif (mouseX >= 597.5 and mouseX <= 597.5 + 205) and (mouseY >= 298 + 150 and mouseY <= 360 + 150):
#         app.warMode = True

#     #item page
#     if app.itemMode:
#         if (mouseX >= 347.5 and mouseX <= 347.5 + 205) and (mouseY >= 298 and mouseY <= 298 + 65):
#             app.addItemMode = True
#         elif (mouseX >= 40 and mouseX <= 100) and (mouseY >= 40 and mouseY <= 70):
#             app.itemMode = False
