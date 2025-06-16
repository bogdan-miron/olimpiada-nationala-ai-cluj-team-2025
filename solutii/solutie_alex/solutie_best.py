import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

from PIL import Image
import numpy as np

def image_to_pixel_features(image_path):

    # Load the image
    image = Image.open(image_path).convert("RGB")
    width, height = image.size
    pixels = np.array(image)

    # Prepare the data
    samples = []

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            samples.append([x, y, r, g, b])

    # Convert to NumPy array if needed
    samples = np.array(samples)
    return samples, width, height

def binary_closing(image_path, threshold=50, show_plots=False):
    """
    Applies grayscale conversion and binary thresholding to an image.

    Args:
        image_path (str): Path to the input image.
        threshold (int): Threshold for binarizing grayscale image.
        show_plots (bool): If True, show matplotlib plots.

    Returns:
        np.ndarray: Binary mask (0/1 values)
    """
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not load image at path: {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binary threshold
    _, binary = cv2.threshold(gray, threshold, 1, cv2.THRESH_BINARY)

    if show_plots:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        axes[0].imshow(gray, cmap='gray')
        axes[0].set_title("Grayscale Image")
        axes[0].axis("off")

        axes[1].imshow(binary, cmap='gray')
        axes[1].set_title("Binary Image (Thresholded)")
        axes[1].axis("off")

        plt.tight_layout()
        plt.show()


    return binary


from os import listdir
from os.path import isfile, join
DATASET_PATH = 'C:/Mano/profession/ai_cluj/olimpiada-nationala-ai-cluj/images_subtask3/'
SAVE_PATH = 'C:/Mano/profession/ai_cluj/olimpiada-nationala-ai-cluj/solutii/solutie_alex/predictions3/'
onlyfiles = [f for f in listdir(DATASET_PATH) if isfile(join(DATASET_PATH, f))]
import cv2

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # You can tweak kernel size

for of in onlyfiles:
    # pixels, width, height = image_to_pixel_features(DATASET_PATH + of)
    '''
    result = kmeans_image_segmentation(
        pixels, height, width, k_range=(2, 2), show_plots=False
    )
    
    image = result["clustered_images"][0].astype(np.uint8)

    # Apply morphological opening
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # Save result
    mask_img = Image.fromarray(opened_image)
    mask_img.save(SAVE_PATH + of)
    '''
    image = binary_closing(DATASET_PATH + of, show_plots=False)

    # Apply morphological opening
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # If `image` contains only 0 and 1:
    image_255 = (image * 255).astype(np.uint8)

    mask_img = Image.fromarray(image_255)
    mask_img.save(SAVE_PATH + of)


import os
import cv2
import csv
import numpy as np

def rle_encode_col_major(mask):
    # Flatten the 2D array in column-major order
    pixels = mask.flatten(order='F')
    rle = []
    i = 0
    while i < len(pixels):
        if pixels[i] == 1:
            start = i
            length = 0
            while i < len(pixels) and pixels[i] == 1:
                length += 1
                i += 1
            rle.extend([start, length])
        else:
            i += 1
    return ' '.join(map(str, rle)) if len(rle) > 0 else ' '.join(map(str, [1, 1]))

def process_images(base_dir, output_csv):
    results = []

    for subtaskID in range(3, 5):
        folder_path = os.path.join(base_dir, 'predictions' + str(subtaskID))
        if not os.path.isdir(folder_path):
            continue

        for filename in sorted(os.listdir(folder_path)):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                image_path = os.path.join(folder_path, filename)
                img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

                # Threshold to binary (you can adjust the threshold if needed)
                _, binary_mask = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)

                rle = rle_encode_col_major(binary_mask)

                # Extract numeric datapointID from filename (assumes digits are in the name)
                datapointID = filename # ''.join(filter(str.isdigit, filename))

                if subtaskID == 3:
                    results.append([1, datapointID, "[28,12]"])
                    results.append([2, datapointID, "[28,12]"])
                # results.append([3, datapointID, "[28,12]"])
                results.append([subtaskID, datapointID, rle])

    # Write to CSV
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['subtaskID', 'datapointID', 'answer'])
        writer.writerows(results)

# Example usage
base_dir = 'C:/Mano/profession/ai_cluj/olimpiada-nationala-ai-cluj/solutii/solutie_alex/'
output_csv = 'rle_output2.csv'
process_images(base_dir, output_csv)

import re
import pandas as pd
df = pd.read_csv('rle_output2.csv')

df['answer'] = df['answer'].apply(
    lambda x: '[' + ','.join(map(str, re.findall(r'\d+', str(x)))) + ']'
)

# Save CSV with minimal quoting
df.to_csv("rle_output2_fixed.csv", index=False, quoting=csv.QUOTE_MINIMAL)