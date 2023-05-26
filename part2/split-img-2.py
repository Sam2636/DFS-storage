import os
import hashlib
import numpy as np
import cv2

# Define the base directory containing the hash folders
base_dir = "part2/array_parts"

# Get a list of all hash folders
hash_folders = sorted([f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))])

# Initialize the ordered parts list
ordered_parts = []

# Iterate over the hash folders
for hash_folder in hash_folders:
    # Read the current hash from the folder name
    current_hash = hash_folder

    # Read the part data from the file
    file_path = os.path.join(base_dir, hash_folder, "part.npy")
    part = np.load(file_path)

    # Check if the folder has a previous hash
    prev_hash_file_path = os.path.join(base_dir, hash_folder, "previous_hash.txt")
    if not os.path.isfile(prev_hash_file_path):
        # If no previous hash, add it to the beginning of the ordered parts list
        ordered_parts.insert(0, part)
        continue

    # Read the previous hash from the file
    with open(prev_hash_file_path, "r") as f:
        previous_hash = f.read().strip()

    # Find the index where the current part should be inserted based on the previous hash
    insert_index = next((i for i, part in enumerate(ordered_parts) if hashlib.sha256(part.tobytes()).hexdigest() == previous_hash), None)

    # If the previous hash is not found, add it to the end of the ordered parts list
    if insert_index is None:
        ordered_parts.append(part)
    else:
        # Insert the current part after the part with the matching previous hash
        ordered_parts.insert(insert_index + 1, part)

# Concatenate the ordered parts into a single NumPy array
numpydata_ordered = np.concatenate(ordered_parts, axis=0)

print(numpydata_ordered.shape)
# Convert the NumPy array to an image using OpenCV
reconstructed_image = cv2.cvtColor(numpydata_ordered, cv2.COLOR_BGR2RGB)

# Save the image to a file
cv2.imwrite('output_image6.png', reconstructed_image)
