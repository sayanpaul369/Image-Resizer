import cv2
import tkinter as tk
from tkinter import filedialog
import os

# Open a file dialog to select the image file
source = filedialog.askopenfilename(title="Select an image file",
                                    filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")])

# Check if a file was selected
if source:
    filename,ext=os.path.splitext(os.path.basename(source)) #os.path.basename() -> split the filename from its path
                                                            #os.path.splitext() -> split the name and extension from the filename

    destination = f"{filename}_modified{ext}"
    scale_percent = int(input("Enter the scale percent you want to resize: \n"))

    # Read the selected image
    src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

    # Calculate new dimensions
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    # Resize the image
    output = cv2.resize(src, (new_width, new_height))

    # Compress the image by changing the quality (adjust as needed)
    # For JPEG format, use cv2.IMWRITE_JPEG_QUALITY, and for PNG, use cv2.IMWRITE_PNG_COMPRESSION
    compression_level = int(input("Enter the level(0-100) for compression: \n"))  # Adjust this value (0-100) for desired compression level
    if source.endswith(".jpeg") or source.endswith(".jpg"):
        cv2.imwrite(destination, output, [cv2.IMWRITE_JPEG_QUALITY, compression_level])
    elif source.endswith(".png"):
        cv2.imwrite(destination, output, [cv2.IMWRITE_PNG_COMPRESSION, compression_level])

    print(f"Image resized and compressed, saved as {destination}")
else:
    print("No file selected.")
