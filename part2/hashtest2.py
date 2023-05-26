import os
import hashlib
import numpy as np
from PIL import Image
from numpy import asarray
from flask import Flask, request, jsonify,send_file
import io
app = Flask(__name__)

@app.route('/split-image', methods=['POST'])
def split_image():
    num_parts = 4
    image_file = request.files['image']
    img = Image.open(image_file)
    image_size_bytes = img.size[0] * img.size[1] * len(img.getbands())
    image_size_kb = image_size_bytes / 1024
    image_size_mb = image_size_kb / 1024
    numpydata = asarray(img)
    part_size = len(numpydata) // num_parts
    base_dir = "part2/array_parts"
    os.makedirs(base_dir, exist_ok=True)
    previous_hash = None
    parts_info = []

    for i in range(num_parts):
        start_index = i * part_size
        end_index = (i + 1) * part_size
        part = numpydata[start_index:end_index]
        part_bytes = part.tobytes()
        hash_object = hashlib.sha256()
        hash_object.update(part_bytes)
        current_hash = hash_object.hexdigest()
        folder_name = os.path.join(base_dir, current_hash)
        os.makedirs(folder_name, exist_ok=True)
        part_image = Image.fromarray(part)
        part_file_path = os.path.join(folder_name, f"{current_hash}.png")
        part_image.save(part_file_path)

        if previous_hash is not None:
            prev_hash_file_path = os.path.join(folder_name, "previous_hash.txt")
            with open(prev_hash_file_path, "w") as f:
                f.write(previous_hash)

        previous_hash = current_hash

        part_info = {
            'part': i + 1,
            'folder_name': folder_name,
            'hash': current_hash
        }
        parts_info.append(part_info)

    response = {
        'image_size_bytes': image_size_bytes,
        'image_size_kb': image_size_kb,
        'image_size_mb': image_size_mb,
        'num_parts': num_parts,
        'parts_info': parts_info
    }

    return jsonify(response)


@app.route('/reconstructimage', methods=['GET'])
def reconstruct_image():
    base_dir = "part2/array_parts"
    hash_folders = sorted([f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))])
    ordered_parts = []

    for hash_folder in hash_folders:
        current_hash = hash_folder
        file_path = os.path.join(base_dir, hash_folder, f"{current_hash}.jpg")
        part_image = Image.open(file_path)
        part = np.array(part_image)

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

    numpydata_ordered = np.concatenate(ordered_parts, axis=0)

    image = Image.fromarray(numpydata_ordered.astype(np.uint8))


    # Create an in-memory byte stream buffer
    image_buffer = io.BytesIO()
    # Save the image to the buffer in PNG format
    image.save(image_buffer, format='PNG')
    # Move the buffer's position to the beginning
    image_buffer.seek(0)

    # Save the image in the base directory
    save_path = os.path.join(base_dir, 'reconstructed_image.png')
    image.save(save_path)


    return send_file(image_buffer,
        mimetype='image/png',
        as_attachment=True,
        attachment_filename='reconstructed_image.png',
        add_etags=False)




if __name__ == '__main__':
    app.run()
