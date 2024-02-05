import cv2
import os

def apply_pseudocolor(image_path, output_folder, colormap_index):
    # Read the grayscale image
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is empty
    if gray_image is None:
        print(f"Error: Unable to load the image {image_path}.")
        return

    # Get the image file name (without extension)
    image_name = os.path.splitext(os.path.basename(image_path))[0]

    # Apply pseudocolor mapping
    pseudocolor_image = cv2.applyColorMap(gray_image, colormap_index)

    # Create the output folder (if it doesn't exist)
    os.makedirs(output_folder, exist_ok=True)

    # Save the pseudocolor image
    cv2.imwrite(os.path.join(output_folder, f"{image_name}_pseudocolor_{colormap_index}.jpg"), pseudocolor_image)

# Example usage
image_folder = 'github_load/Abnormal/Pulverized_coal_lower'  # Replace with your image folder path
output_base_folder = 'afterTreat/colormap/Abnormal/Pulverized_coal_lower'  # Replace with your output folder base name

# Iterate over all images in the image folder
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):
        image_path = os.path.join(image_folder, filename)
        output_folder = os.path.join(output_base_folder, os.path.splitext(filename)[0])

        # Iterate over pseudocolor mapping indices
        for colormap_index in range(0, 22):
            apply_pseudocolor(image_path, output_folder, colormap_index)

print("Pseudocolor transformation completed.")