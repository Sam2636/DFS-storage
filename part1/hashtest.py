import os
import hashlib
import numpy as np
from PIL import Image
from numpy import asarray
# Assuming you already have a NumPy array named 'numpydata'
# Define the number of parts to split the array into

img = Image.open('test1.png')

# Get the size of the image in bytes
image_size_bytes = img.size[0] * img.size[1] * len(img.getbands())

# Convert the size to kilobytes (KB) and megabytes (MB)
image_size_kb = image_size_bytes / 1024
image_size_mb = image_size_kb / 1024

# Convert the image to a NumPy array
numpydata = asarray(img)
num_parts = 4

# Calculate the size of each part
part_size = len(numpydata) // num_parts

# Create a base directory to store the folders
base_dir = "array_parts"
os.makedirs(base_dir, exist_ok=True)

# Initialize the previous hash variable
previous_hash = None

# Split the array into parts and store in separate folders
for i in range(num_parts):
    # Get the current part
    start_index = i * part_size
    end_index = (i + 1) * part_size
    part = numpydata[start_index:end_index]

    # Convert the part to bytes
    part_bytes = part.tobytes()

    # Calculate the SHA-256 hash of the part
    hash_object = hashlib.sha256()
    hash_object.update(part_bytes)
    current_hash = hash_object.hexdigest()

    # Create a folder with the hash as its name
    folder_name = os.path.join(base_dir, current_hash)
    os.makedirs(folder_name, exist_ok=True)

    # Write the part data to a file within the folder
    file_path = os.path.join(folder_name, "part.npy")
    np.save(file_path, part)

    # Save the previous hash in a file within the folder
    if previous_hash is not None:
        prev_hash_file_path = os.path.join(folder_name, "previous_hash.txt")
        with open(prev_hash_file_path, "w") as f:
            f.write(previous_hash)

    # Set the current hash as the previous hash for the next iteration
    previous_hash = current_hash

    # Print information
    print("Part", i+1, "has been saved in", folder_name)
    print("SHA-256 Hash:", current_hash)
    print()
