from cmu_graphics import *
#from interface2 import *
from tp06 import loadImage
#from itemObject import Item
import os
from PIL import Image, ImageDraw,ImageFont
# from generator import Top, Bottom, Outfit
from objects2 import Top, Bottom, Item

def onAppStart(app):
   # app.url = "\Users\\irisy\\Downloads\\cropflower.png"
    app.b1 = "C:/Users/irisy/Desktop/15-112/termProject/term-project-v2/item.png"
    app.b2 = "C:\\Users\\irisy\\Desktop\\15-112\\termProject\\term-project-v2\\outfit.png"
    app.b3 = "C:\\Users\\irisy\\Desktop\\15-112\\termProject\\term-project-v2\\closet.png"
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
    app.url = "C:\\Users\\irisy\\Downloads\\57E9D6B0-AF0F-4258-BE81-FF09865C1789.png"
    # pilImage1 = Image.open(app.url)
    # app.cmuImage1 = CMUImage(pilImage1)

    app.word = "Enter here:"
    app.type = False
    app.targetSeason = ""
    # app.season = set()
    app.moveOn = False
    # app.curr.color = set()
    app.done = False
    app.finDone = False
    app.typeC = ""
    # app.fit = ""
    app.tops = []
    app.bottoms = []
    app.seen = []
    app.rename = False
    app.curr = ""
    app.displayed_outfits = []
    app.recycled = []

    app.numCols = 4
    app.itemSize = (app.width//app.numCols, 230) 
    app.itemsPerRow = app.numCols
    app.offset = 30
    app.saved_outfits = []
    app.userPrefMode = False
    app.userPrefColors = []
    app.my_good_outfits = []

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
    drawImage(app.url, 620,300, align = "center", width = 400, height = 400)
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
            print(os.path)
            if file_path and os.path.exists(file_path):
                app.files = file_path
                print(app.files)
            else:
                app.showMessage("Invalid path! Please enter a valid directory.")
                app.files == None
        try:
            # !!! change path
            loadImage(app.files)
            for item in ['C:\\Users\\irisy\\Desktop\\15-112\\termProject\\term-project-v2\\processed\\'+item for item in os.listdir('processed')]:
                filename = os.path.splitext(os.path.basename(item))[0]
                print("namsssss: ", filename)
                Item(item, filename, (0, 0), (200, 200), set(), set(), '', None, f"processed\\{filename}.png")
                # i += 1
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
            for i, item in enumerate([item for sublist in Item.instances.values() for item in sublist]):
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

def wardrobe_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 40 and mouseY <= 100):
        setActiveScreen("main")
    elif (mouseX >= 325 and mouseX <= 450) and (mouseY >= 300 and mouseY <= 350):
        if app.noFiles:
            setActiveScreen("item")
    elif (mouseX >= 0 and mouseX <= app.width//2) and (mouseY >= 80 and mouseY <= 130):
        setActiveScreen("wardrobe")
    elif (mouseX >= app.width//2 and mouseX <= app.width *2) and (mouseY >= 80 and mouseY <= 130):
        setActiveScreen("gen") #testing
    else:
        # Iterate through each item to check if the click is within its bounds
        for item in [item for sublist in Item.instances.values() for item in sublist]:
            if item.bounds is not None:  # Check if bounds are set
                x1, y1, x2, y2 = item.bounds  # Get the bounds of the item
                if x1 <= mouseX <= x2 and y1 <= mouseY <= y2:  # Check if mouse is inside the bounds
                    app.curr = item
                    # app.num = item.name
                    print("item name: ", item.name)
                    if app.curr.name not in app.seen:
                        app.rename = False
                        app.typeC = ''
                        app.word = "Enter here:"
                        app.seen.append(app.curr.name)
                        setActiveScreen("nameItem") 
                    else:
                        print('founedoineif na')
                        app.rename = True
                        setActiveScreen("temp")

                        print("already seen")
                    print("seen: ", app.seen)

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
    drawLabel(f"Color: {app.curr.color}", 230, 250, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
    drawLabel(f"Season: {app.curr.season}", 230, 300, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
    drawLabel(f"Fit: {app.curr.type}", 230, 350, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
    # if isinstance(app.curr, Top):
    drawLabel(f"Type: {app.curr.isTop}", 230, 400, size = 20, fill = "white", font = "Lora", align = "left",bold = True)
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
    # if (mouseX >= 230 and mouseX <= 300) and (mouseY >= 345 and mouseY <= 360):
    #     setActiveScreen("fit")
    if (mouseX >= 230 and mouseX <= 400) and (mouseY >= 395 and mouseY <= 410):
        setActiveScreen("type")
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
        setActiveScreen("wardrobe")
    if (mouseX >= 497 and mouseX <= 700) and (mouseY >= 500 and mouseY <= 550):
        app.rename = False
        setActiveScreen("wardrobe")

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
            app.curr.name = app.word
            app.seen[-1] = app.curr.name
            if app.rename:
                setActiveScreen("temp")
            else:
                setActiveScreen("season")
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 60 and mouseY <= 110):
        if app.rename:
            print("new: ", app.word)
            setActiveScreen("temp")
        else:
            # if (app.tops == [] and app.bottoms == []):
            #     app.seen.remove(app.num)
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
    if "Spring" in app.curr.season:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(212 + 50, 340 - 40, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Spring", 210 + 50 + 75, 337 - 40 + 27, fill="white", font="Lora", size=20)  # Adjusted label position

    # Summer Button
    if "Summer" in app.curr.season:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 50, 337 - 110, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 50, 340 - 110, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Summer", 210 + 50 + 75, 337 - 110 + 27, fill="white", font="Lora", size=20)  # Adjusted label position

    if "Autumn" in app.curr.season:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 250, 337 - 40, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 250, 340 - 40, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Autumn", 210 + 250 + 75, 337 - 40 + 27, fill="white", font="Lora", size=20)  # Adjusted label position

    if "Winter" in app.curr.season:
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
        if "Summer" in app.curr.season:
            app.curr.season.remove("Summer")
        else:
            app.curr.season.add("Summer")
    if (mouseX >= 260 and mouseX <= 410) and (mouseY >= 300 and mouseY <= 350):
        if "Spring" in app.curr.season:
            app.curr.season.remove("Spring")
        else:
            app.curr.season.add("Spring")
    if (mouseX >= 460 and mouseX <= 610) and (mouseY >= 230 and mouseY <= 280):
        if "Winter" in app.curr.season:
            app.curr.season.remove("Winter")
        else:
            app.curr.season.add("Winter")
    if (mouseX >= 460 and mouseX <= 610) and (mouseY >= 300 and mouseY <= 350):
        if "Autumn" in app.curr.season:
            app.curr.season.remove("Autumn")
        else:
            app.curr.season.add("Autumn")
    if app.curr.season != set(): app.moveOn = True
    if (mouseX >= 328 and mouseX <= 530) and (mouseY >= 370 and mouseY <= 420):
        if app.moveOn:
            if app.rename:
                setActiveScreen("temp")
            else:
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
        # if colors[j] in app.curr.color:
        #     drawButton(18 + i, 247, 45, 45, 10, fill = selectedCol)
        #     drawButton(20 + i, 250, 40, 40, 10, fill = colors[j])
        # else:
        drawButton(20 + i, 250, 40, 40, 10, fill = colors[j])
        j += 1
    j = 0
    for i in range(200, 680, 70):
        # if col[j] in app.curr.color:
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
            if "black" in app.curr.color:
                app.curr.color.remove("black")
            else:
                app.curr.color.add("black")
        if (mouseX >= 290 and mouseX <= 330):
            if "brown" in app.curr.color:
                app.curr.color.remove("brown")
            else:
                app.curr.color.add("brown")
        if (mouseX >= 360 and mouseX <= 400):
            if "blue" in app.curr.color:
                app.curr.color.remove("blue")
            else:
                app.curr.color.add("blue")
        if (mouseX >= 430 and mouseX <= 470):
            if "lightBlue" in app.curr.color:
                app.curr.color.remove("lightBlue")
            else:
                app.curr.color.add("lightBlue")
        if (mouseX >= 500 and mouseX <= 540):
            if "purple" in app.curr.color:
                app.curr.color.remove("purple")
            else:
                app.curr.color.add("purple")
        if (mouseX >= 570 and mouseX <= 610):
            if "pink" in app.curr.color:
                app.curr.color.remove("pink")
            else:
                app.curr.color.add("pink")
        if (mouseX >= 640 and mouseX <= 680):
            if "orange" in app.curr.color:
                app.curr.color.remove("orange")
            else:
                app.curr.color.add("orange")

    if (mouseY >= 300 and mouseY <= 340):
        if (mouseX >= 220 and mouseX <= 260):
            if "green" in app.curr.color:
                app.curr.color.remove("green")
            else:
                app.curr.color.add("green")
        if (mouseX >= 290 and mouseX <= 330):
            if "yellow" in app.curr.color:
                app.curr.color.remove("yellow")
            else:
                app.curr.color.add("yellow")
        if (mouseX >= 360 and mouseX <= 400):
            if "red" in app.curr.color:
                app.curr.color.remove("red")
            else:
                app.curr.color.add("red")
        if (mouseX >= 430 and mouseX <= 470):
            if "gray" in app.curr.color:
                app.curr.color.remove("gray")
            else:
                app.curr.color.add("gray")
        if (mouseX >= 500 and mouseX <= 540):
            if "beige" in app.curr.color:
                app.curr.color.remove("beige")
            else:
                app.curr.color.add("beige")
        if (mouseX >= 570 and mouseX <= 610):
            if "white" in app.curr.color:
                app.curr.color.remove("white")
            else:
                app.curr.color.add("white")
        if (mouseX >= 640 and mouseX <= 680):
            if "lightGray" in app.curr.color:
                app.curr.color.remove("lightGray")
            else:
                app.curr.color.add("lightGray")
    print(app.curr.color)
    if app.curr.color != set():
        app.done = True
    else:
        app.done = False
    if (mouseX >= 328 and mouseX <= 530) and (mouseY >= 370 and mouseY <= 420):
        if app.done:
            if app.rename:
                setActiveScreen("temp")
            else:
                print(app.curr.color)
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
    
    if "top" in app.typeC:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 50, 250, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 50, 253, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Top", 210 + 50 + 75, 250 + 27, fill="white", font="Lora", size=20)  # Adjusted label position

    if "bottom" in app.typeC:
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
        app.typeC = ("top")
        #app.finDone = True
    if (mouseX >= 460 and mouseX <= 610) and (mouseY >= 250 and mouseY <= 300):
        app.typeC = ("bottom")
        #app.finDone = True
    if app.typeC != "":
        app.finDone = True
    if (mouseX >= 328 and mouseX <= 530) and (mouseY >= 370 and mouseY <= 420):
        if app.finDone:
            print(app.typeC)
            print("done")
            print(app.curr.isTop)
            print(Item.instances[app.curr.isTop])
            [print(item) for item in Item.instances[app.curr.isTop]]
            print(app.curr)
            print(app.curr in Item.instances[app.curr.isTop])
            Item.instances[app.curr.isTop].remove(app.curr)
            Item.instances[app.typeC].add(app.curr)
            app.curr.isTop = app.typeC
            if app.rename:
                setActiveScreen("temp")
            else:
                setActiveScreen("fit")
            # if app.typeC == "Top":
            #     tops.append(Top(app.word, app.curr.color, app.season))

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
    
    if "baggy" in app.curr.type:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 50, 250-50, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 50, 253-50, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Baggy", 210 + 50 + 75, 250 + 27-50, fill="white", font="Lora", size=20)  # Adjusted label position

    if "tight" in app.curr.type:
        buttonCol = rgb(173,173,173)
    else:
        buttonCol = rgb(109, 119, 99)
    drawButton(210 + 250, 250-50, 150, 65 - 10, 10, fill="white")
    drawButton(212 + 250, 253-50, 147, 60 - 10, 10, fill=buttonCol)
    drawLabel("Tight", 210 + 250 + 75, 250 + 27-50, fill="white", font="Lora", size=20)  # Adjusted label position
    
    if "well-fit" in app.curr.type:
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
        app.curr.type = "baggy"
    if (mouseX >= 460 and mouseX <= 610) and (mouseY >= 200 and mouseY <= 255):
        app.curr.type = "tight"
    if (mouseX >= 360 and mouseX <= 510) and (mouseY >= 270 and mouseY <= 325):
        app.curr.type = "well-fit"
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 50 and mouseY <= 100):
        if app.rename:
            setActiveScreen("temp")
        else:
            setActiveScreen("type")
    print(app.curr.type)
    if app.curr.type != "":
        if (mouseX >= 328 and mouseX <= 530) and (mouseY >= 370 and mouseY <= 420):
            if app.rename:
                setActiveScreen("temp")
            else:
                app.rename = True
                setActiveScreen("wardrobe")
            

            



# !!! GENERATOR
from gen3 import pickOutfitOnUserPreference, generateAllGoodOutfits, get4UserPreferredOutfits, pickAGoodOutfitRandomly, recycleDisplayedOutfits, get4Outfits, getSeasonTops, getSeasonBottoms, getSeasonFromTemp
def gen_onScreenActivate(app):
    app.width = 900
    app.height = 650
    # top1 = Item(None, "bf", None, 200, {"green"}, {"summer"}, "baggy", 'top', "processed\\IMG_1469.png")
    # top2 = Item(None, "bm", None, 200, {"blue"}, {"summer"}, "tight", 'top', "processed\\IMG_1479.png")
    # top3 = Item(None, "Pacsun", None, 200, {"red"}, {"summer", "spring"}, "tight", 'top', "processed\\IMG_1473.png")
    # top4 = Item(None, "bm", None, 200,  {"white"}, {"summer", "spring"}, "tight", 'top', "processed\\IMG_1470.png")
    # top5 = Item(None, "long", None, 200, {"green"},{"summer"},"well-fit", "top", "processed\\8IMG_2113.png")
    # bot1 = Item(None, "chuu", None, 200, {"gray"}, {"summer", "fall"}, "baggy", 'bottom', "processed\\IMG_1475.png")
    # bot2 = Item(None, "jean", None, 200, {"lightBlue"}, {"summer"}, "well-fit", 'bottom', "processed\\IMG_1476.png")
    # bot3 = Item(None, "vjean", None, 200, {"blue"}, {"summer"}, "baggy", "bottom", "processed\\6IMG_1477.png")
    # tops = [top1, top2, top3, top4, top5]
    # bottoms = [bot1, bot2, bot3]


    print('top list = ', Item.instances['top'])
    print('bottom list = ', Item.instances['bottom'])
    app.my_good_outfits = generateAllGoodOutfits(Item.instances['top'], Item.instances['bottom'])

    print('good outfits: ', app.my_good_outfits)
    #outfits_size = len(app.my_good_outfits)
    #loop_range = min(outfits_size, 4)
    # now I have a list of color matched good outfits

    print('Testing display first 4 outfits')

    # displayed outfits contains a list of outfit being displayed
    

    print('size of good outfits = ', len(app.my_good_outfits))

    print('Testing display first 4 outfits')


    #app.my_good_outfits, app.displayed_outfits = get4Outfits(app.my_good_outfits, app.displayed_outfits)
    get4Outfits(app.my_good_outfits, app.displayed_outfits)
    print("displayed outfits: ", app.displayed_outfits)
    print('size of good outfits after displayed = ', len(app.my_good_outfits))
    


def gen_redrawAll(app):
    drawLabel("Generate Outfit!", 100, 50, size = 30, bold = True, fill = app.gray, font = "Lora", align = "left")
    drawLabel("Back", 50, 50,align = "center", fill = app.gray, font = "Lora", size = 20)
    drawLine(100, 70 , 270 + 80 , 70, fill = app.gray, lineWidth = 2)
    drawLabel("Generate with weather", 380, 50, size = 20, bold = True, fill = app.gray, font = "Lora", align = "left")
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
        drawLabel("Thats the best outfit! Press regenerate to restart!", 550, 400, fill = app.gray, size = 25, font = "Lora", align = "left")
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
            y = row * itemHeight + 200 - app.offset

            # imageTop = clothing.top.serialNum
            # # if clothing.isTop == "bottom":
            # imageBot = clothing.bottom.serialNum
            print("serial num: ", clothing.top.serialNum)
            drawImage(clothing.top.serialNum, x, y + 30, align="center", width=200, height=200)
            bottom = y + 200 + 20
            drawImage(clothing.bottom.serialNum, x, bottom, align="center", width=200, height=200)
    
            drawButton(x - 75, 523, 155, 50, 10, fill=app.lightg)
            drawButton(x - 75, 520, 150, 50, 10, fill=app.bgCol)
            clothing.pos = (x, 550)
            #print("clothing position: ", clothing.pos)
            drawLabel("add to outfits", x, 545, size=18, fill = "white" ,font="Lora", bold = True)

    # Draw the "regenerate" button at the end
    drawButton(650, 603-20, 155, 50, 10, fill = app.lightg)
    drawButton(650, 600-20, 150, 50, 10 ,fill = app.bgCol)
    drawLabel("regenerate", 720, 605, size=17, fill = "white", bold = True, font="Lora")

    drawButton(650, 43-10, 155, 50, 10, fill = app.lightg)
    drawButton(650, 40-10, 150, 50, 10, fill = app.bgCol)
    drawLabel("My Outfits", 715, 54, size = 17, fill = "white", bold = True, font = "Lora")

def gen_onMousePress(app, mouseX, mouseY):
    buttonWidth, buttonHeight = 150, 50 
    if (mouseX >= 380 and mouseX <= 620) and (mouseY >= 40 and mouseY <= 60):
        while True:
            temp = app.getTextInput("Enter the temperature today (F): ")
            if getSeasonFromTemp(int(temp)) == "Invalid season":
                app.showMessage("Invalid Season, please try again")
            else:
                app.targetSeason = getSeasonFromTemp(int(temp))
                break
        if app.targetSeason != "":
            app.my_good_outfits = generateAllGoodOutfits(getSeasonTops(Item.instances['top'], app.targetSeason), getSeasonBottoms(Item.instances['bottom'], app.targetSeason))
        
    if (mouseX >= 30 and mouseX <= 80) and (mouseY >= 40 and mouseY <= 65):
        print("ylo")
        setActiveScreen("main")
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
    itemHeight = 180 
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
        drawImage(clothing.top.serialNum, x, y - itemHeight / 2 + 40, align="left", width=200 - 40, height=200)
        drawImage(clothing.bottom.serialNum, x, y + itemHeight / 2 - overlapOffset + 20, align="left", width=200 - 40, height=200)

def outfits_onMousePress(app, mouseX, mouseY):
    if (mouseX >= 50 and mouseX <= 110) and (mouseY >= 40 and mouseY <= 100):
        setActiveScreen("gen")
        
def main():
    runAppWithScreens(initialScreen='start')
main()


