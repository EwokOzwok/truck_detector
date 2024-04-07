import os
os.getcwd()

# Specify the directory containing the JPEG files
directory = 'C:\\Users\\intra\\OneDrive\\Desktop\\truckdetector\\data\\'

# Iterate through the range of numbers from 0 to 2292
for i in range(2293):
    # Generate the old and new filenames
    old_filename = os.path.join(directory, f"frame{i}.jpg")
    new_filename = os.path.join(directory, f"{i}.jpg")
    
    # Check if the old filename exists
    if os.path.exists(old_filename):
        # Rename the file
        os.rename(old_filename, new_filename)
        print(f"Renamed {old_filename} to {new_filename}")
    else:
        print(f"File {old_filename} not found.")
