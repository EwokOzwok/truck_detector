from PIL import Image
import os
os.getcwd()
# Path to the folder containing your images
folder_path = r"C:/Users/intra/OneDrive/Desktop/AI Projects/truckdetector/truck_detector/data"

# Output folder where cropped images will be saved
output_folder = r"C:/Users/intra/OneDrive/Desktop/AI Projects/truckdetector/truck_detector/croppeddata"

# Ensure the output folder exists, create it if not
os.makedirs(output_folder, exist_ok=True)

# Iterate through each image in the folder
for filename in os.listdir(folder_path):
    # Open the image
    image_path = os.path.join(folder_path, filename)
    with Image.open(image_path) as img:
        # Get dimensions of the image
        width, height = img.size

        # Crop and keep only the top half
        top_half_img = img.crop((0, 0, width, height // 2))

        # Save the cropped image
        output_path = os.path.join(output_folder, filename)
        top_half_img.save(output_path)

print("Cropping complete.")
