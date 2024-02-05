import cv2
import os

def extract_and_save_channels(image_path, output_folder):
    # Read the color image
    color_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Check if the image is empty
    if color_image is None:
        print(f"Error: Unable to load the image {image_path}.")
        return

    # Get the image file name (without extension)
    image_name = os.path.splitext(os.path.basename(image_path))[0]

    # Split the color image into three channels
    b, g, r = cv2.split(color_image)

    # Create the output folder (if it doesn't exist)
    os.makedirs(output_folder, exist_ok=True)

    # Save single-channel images for each of the three channels
    cv2.imwrite(os.path.join(output_folder, f"{image_name}_blue_channel.jpg"), cv2.merge([b, b*0, b*0]))
    cv2.imwrite(os.path.join(output_folder, f"{image_name}_green_channel.jpg"), cv2.merge([g*0, g, g*0]))
    cv2.imwrite(os.path.join(output_folder, f"{image_name}_red_channel.jpg"), cv2.merge([r*0, r*0, r]))

# Example usage
image_folder = '###'  # Replace with your image folder path
output_base_folder = '###'  # Replace with your output folder base name

# Iterate over all images in the image folder
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):
        image_path = os.path.join(image_folder, filename)
        output_folder = os.path.join(output_base_folder, os.path.splitext(filename)[0])
        extract_and_save_channels(image_path, output_folder)

print("Extraction and saving completed.")