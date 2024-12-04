import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
import webcolors
import sys
import os

executable_path = os.path.dirname(sys.argv[0])
imagenet_classes_file_path = os.path.join(executable_path, 'imagenet_classes.txt')
# Load the pre-trained ResNet50 model
model = ResNet50(weights='imagenet')
# Load the class labels
with open(imagenet_classes_file_path, 'r') as f:
    class_labels = f.read().splitlines()

# Function to preprocess the image for ResNet50
def preprocess_image(image_path):
    """
    Preprocesses the image for the ResNet50 model.

    Args:
        image_path: Path to the image file.

    Returns:
        The preprocessed image as a NumPy array.
    """
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

# Function to get dominant color within bounding box
def get_dominant_color(image, bounding_box):
    """
    Calculates the dominant color within a bounding box in an image.

    Args:
        image: The image as a NumPy array.
        bounding_box: A tuple of bounding box dimensions (x, y, width, height).

    Returns:
        A tuple representing the dominant color in BGR format (blue, green, red).
    """
    x, y, w, h = bounding_box
    roi = image[y:y+h, x:x+w]
    
    # Calculate the mean color of the region of interest
    mean_color = cv2.mean(roi)[:3]  # Get BGR values
    
    return mean_color

def closest_colour(requested_colour):
    min_colours = {}
    for name in webcolors.names("css3"):
        r_c, g_c, b_c = webcolors.name_to_rgb(name)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

# Function to translate RGB to color name
def rgb_to_color_name(rgb):
    """
    Translates an RGB tuple to its closest matching color name.

    Args:
        rgb: An RGB tuple (red, green, blue) with values between 0 and 255.

    Returns:
        The name of the closest matching color.
    """
    try:
        # Find the closest matching color name
        color_name = webcolors.rgb_to_name(rgb)
    except ValueError:
        # If no exact match is found, get the closest name
        min_distance = float('inf')
        for key, value in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            distance = (r_c - rgb[0]) ** 2 + (g_c - rgb[1]) ** 2 + (b_c - rgb[2]) ** 2
            if distance < min_distance:
                min_distance = distance
                color_name = value
    return color_name

# Function to detect cloth, dimensions, and color
def detect_cloth_and_details(image_path):
    """
    Detects the type of cloth in the image using the ResNet50 model,
    returns the bounding box dimensions, and the dominant color name.

    Args:
        image_path: Path to the image file.

    Returns:
        A tuple containing:
            - The predicted cloth label.
            - A tuple of bounding box dimensions (x, y, width, height).
            - The name of the closest matching color.
    """
    img = cv2.imread(image_path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(rgb_img, (224, 224))
    
    # Preprocess the image for ResNet50
    input_tensor = preprocess_input(np.expand_dims(img_resized, axis=0))
    
    # Get predictions from ResNet50
    predictions = model.predict(input_tensor)
    decoded_predictions = tf.keras.applications.imagenet_utils.decode_predictions(predictions, top=5)[0]
    predicted_label = decoded_predictions[0][1] 

    # Use a simple object detection method (replace with a more robust method if needed)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Assuming the largest contour is the cloth
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        
        # Get dominant color in BGR
        dominant_color_bgr = get_dominant_color(img, (x, y, w, h))
        
        # Convert BGR to RGB
        dominant_color_rgb = tuple(int(i) for i in dominant_color_bgr[::-1])
        
        # Translate RGB to color name
        #color_name = rgb_to_color_name(dominant_color_rgb)
        color_name = closest_colour(dominant_color_rgb)

        dom_color = detect_object_color(img, COLOR_RANGES)
        print(f"color is {dom_color}")
        return predicted_label, (x, y, w, h), color_name
    else:
        return predicted_label, None, None


def getColorCounts(image, COLOR_RANGES):
  """
  Counts the occurrences of colors within specified ranges in an image efficiently.

  Args:
      image: The image to analyze (as a NumPy array).
      COLOR_RANGES: A dictionary mapping color names to (lower, upper) RGB tuples.

  Returns:
      A dictionary with color names as keys and their counts as values.
  """

  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  color_count = {color: 0 for color in COLOR_RANGES.keys()}

  for color, (lower, upper) in COLOR_RANGES.items():
    # Create masks for each color range
    mask = cv2.inRange(image_rgb, np.array(lower), np.array(upper))
    color_count[color] = cv2.countNonZero(mask)

  return color_count


def detect_object_color(image, COLOR_RANGES, threshold=0.1, white_threshold=200):
    """
    Detects the dominant color of an object in an image, assuming a white background.

    Args:
        image_path: Path to the image file.
        COLOR_RANGES: A dictionary mapping color names to (lower, upper) RGB tuples.
        threshold: The minimum proportion of pixels for a color to be considered dominant.
        white_threshold: Threshold to identify white pixels (0-255).

    Returns:
        The dominant color name or None if no dominant color is found.
    """

    #image = cv2.imread(image_path)
    
    # Create a mask to remove white background
    lower_white = np.array([white_threshold, white_threshold, white_threshold])
    upper_white = np.array([255, 255, 255])
    white_mask = cv2.inRange(image, lower_white, upper_white)
    
    # Invert the mask to keep non-white pixels
    object_mask = cv2.bitwise_not(white_mask)
    
    # Apply the mask to the image
    masked_image = cv2.bitwise_and(image, image, mask=object_mask)

    color_counts = getColorCounts(masked_image, COLOR_RANGES)

    # Calculate total pixel count of the object (non-white pixels)
    total_pixels = cv2.countNonZero(object_mask)

    dominant_color = None
    max_count = 0
    for color, count in color_counts.items():
        if total_pixels > 0:  # Avoid division by zero
            proportion = count / total_pixels
            if proportion > threshold and count > max_count:
                dominant_color = color
                max_count = count

    return dominant_color

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

current_dir = os.getcwd() # get the current directory
test_dir = os.path.join(current_dir, "test")
for filename in os.listdir(test_dir):
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
      filepath = os.path.join(test_dir, filename)
      print(f"processing file: {filepath}")
      predicted_cloth, dimensions, color_name = detect_cloth_and_details(filepath)
      print("Detected cloth:", predicted_cloth)
      if dimensions:
          print("Bounding box dimensions (x, y, width, height):", dimensions)
          print("Dominant color:", color_name)
      else:
          print("Could not detect object details.")

