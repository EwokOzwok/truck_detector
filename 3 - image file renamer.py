import os

# Define the directory containing the files
directory = r"C:/Users/intra/OneDrive/Desktop/AI Projects/truckdetector/truck_detector/data"

# List all files in the directory
files = os.listdir(directory)

# Sort the files by their current names
files.sort()

# Counter for new names
counter = 0

# Iterate through each file
for file_name in files:
    # Construct the new file name
    new_file_name = str(counter) + ".jpg"
    
    # Get the current file path
    current_path = os.path.join(directory, file_name)
    
    # Get the new file path
    new_path = os.path.join(directory, new_file_name)
    
    # Rename the file
    os.rename(current_path, new_path)
    
    # Increment counter
    counter += 1

print("All files renamed successfully!")
