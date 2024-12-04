from rembg import remove
from PIL import Image
#from cmu_graphics import CMUImage
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def loadImage(inputPath):
    folder_path = inputPath
    #folder_path = "clothes"
    result = []
    i = 0
    for item in os.listdir(folder_path):
        #
        img_path = os.path.join(folder_path, item)
        input_image = Image.open(img_path)
        #print("name: ", img_path)
        print("loadimage item: ", item)
        output_image = remove(input_image)
        #output_folder = f"C:\\Users\\irisy\\Desktop\\15-112\\termProject\\Term-Project\\removedbgClothing\\{i}"
        output_folder =  f"C:\\Users\\irisy\\Desktop\\15-112\\termProject\\Term-Project\\removedbgClothing\\{i}"
        ##print('heloooooooooo', item)
        output_path = output_folder+item[:-4] +".png"
        output_image.save(output_path)
        result.append(output_path)
        print("result: ", result)
        i += 1
      
    return result


# from sklearn.cluster import KMeans

# Define a list of colors with their RGB values
COLOR_RANGES = {
    "Red": ((100, 0, 0), (255, 80, 80)),
    "Orange": ((200, 100, 0), (255, 200, 50)),
    "Yellow": ((200, 200, 0), (255, 255, 100)),
    "Green": ((40, 90, 40), (130, 220, 130)), # Narrower range, includes grayish greens
    "darkBlue": ((0, 0, 50), (65, 90, 100)),          # Avoids lighter tones to maintain dark appearance
    "lightBlue": ((140, 180, 200), (180, 240, 255)),  # Darker blues included
    "Purple": ((100, 0, 100), (180, 60, 180)),  # More distinct from pink
    "Pink": ((230, 180, 200), (255, 220, 240)),  # Narrower pink range
    "Beige": ((210, 210, 180), (255, 245, 220)),
    "White": ((170, 170, 170), (255, 255, 255)),  # Higher lower-bound
    "Black": ((45, 45, 45), (60, 60, 60)),  # Expanded to include darker grays
    "Gray": ((60, 60, 60), (150, 150, 150)),  # Adjusted for separation
    "Brown": ((110, 50, 30), (170, 100, 80)),  # Narrower brown range
    "LightGray": ((160, 160, 160), (189, 189, 189))  # For subtle grays
}


colorCount = {
    "Red": 0,
    "Orange": 0,
    "Yellow":0,
    "Green": 0,
    "darkBlue": 0,
    "lightBlue": 0,
    "Purple":0,
    "Pink": 0,
    "Beige": 0,
    "White": 0,
    "Black": 0,
    "Gray":  0,
    "Brown": 0,
    "LightGray": 0
}

def getColorCounts(folder):
    image_rgb= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height, width, _ = image_rgb.shape
    local_color_count = {color: 0 for color in COLOR_RANGES.keys()}
    # Loop through each pixel in the image
    for y in range(0, height, 100):
        for x in range(0, width, 100):
            r, g, b = image_rgb[y, x]
            for color, (lower, upper) in COLOR_RANGES.items():
                # Check if the pixel's color is within the range
                if lower[0] <= r <= upper[0] and lower[1] <= g <= upper[1] and lower[2] <= b <= upper[2]:
                    local_color_count[color] += 1
                    break  # Stop checking other colors once a match is found
    return local_color_count

# Load the image
#image_path = "C:\\Users\\irisy\\Desktop\\15-112\\termProject\\Term-Project\\removedbgClothing"
#  # Replace with the path to your image
# image = cv2.imread(image_path)

# # Get color counts

final = dict()
# Find the most common color
# for item in os.listdir("removedbgClothing"):
#     # Convert the image to RGB format
#     #image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image_path = os.path.join("removedbgClothing", item)
#     print(item)
#     # Load the image
#     image = cv2.imread(image_path)
#     if image is None:
#         print(f"Error loading image: {image_path}")
#         continue 
#     result = getColorCounts(image)

#     most_common_color = max(result, key=result.get)
#     #print(result)
#     #print(result.get)
#     final[item] = most_common_color
# print(final)


#print(f"The most common color is {most_common_color} with {most_common_count} pixels.")


# # Load the image
#image = cv2.imread("C:/Users/irisy/Desktop/15-112/termProject/Term-Project/removedbgClothing/h.pngbm.png")

#getColor(image)
#blue_mask = cv2.inRange(hsv(100,100,100),(140,255,255))
# Get the dominant color
# dominant_color = get_dominant_color(image)
# print(f"Dominant Color (RGB): {dominant_color}")

# # Find the closest color using recursive Euclidean distance
# closest_color = find_closest_color_recursive(dominant_color, COLOR_NAMES)
# print(f"Closest Color: {closest_color}")

# def getColor(image):
#     image_rgb= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     #height, width, _ = image_rgb.shape
