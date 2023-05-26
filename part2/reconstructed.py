import os
import hashlib
import numpy as np
from PIL import Image
from numpy import asarray
from flask import Flask, request, jsonify,send_file
import io


def reconstruct_image():
    base_dir = "part2/array_parts"
    hash_folders = sorted([f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))])
    ordered_parts = []

    for hash_folder in hash_folders:
        # print(hash_folder)
        current_hash = hash_folder
        file_path = os.path.join(base_dir, hash_folder, f"{current_hash}.png")
        # print(file_path)
        part_image = Image.open(file_path)
        
        part = np.array(part_image)
        # print(part)

        prev_hash_file_path = os.path.join(base_dir, hash_folder, "previous_hash.txt")
        if not os.path.isfile(prev_hash_file_path):
            ordered_parts.insert(0, part)
            continue

        with open(prev_hash_file_path, "r") as f:
            previous_hash = f.read().strip()

        insert_index = next((i for i, part in enumerate(ordered_parts) if hashlib.sha256(part.tobytes()).hexdigest() == previous_hash), None)

        if insert_index is None:
            ordered_parts.append(part)
        else:
            ordered_parts.insert(insert_index + 1, part)
    print(ordered_parts)        

    numpydata_ordered = np.concatenate(ordered_parts, axis=0)

    image = Image.fromarray(numpydata_ordered.astype(np.uint8))


    # Create an in-memory byte stream buffer
    image_buffer = io.BytesIO()
    # Save the image to the buffer in PNG format
    image.save(image_buffer, format='PNG')
    # Move the buffer's position to the beginning
    image_buffer.seek(0)

    # # Save the image in the base directory
    save_path = os.path.join(base_dir, 'reconstructed_image1.png')
    image.save(save_path)


    # return send_file(image_buffer,
    #     mimetype='image/png',
    #     as_attachment=True,
    #     attachment_filename='reconstructed_image.png',
    #     add_etags=False)

    print(numpydata_ordered.shape)


reconstruct_image()