from PIL import Image
from numpy import asarray
import hashlib
# Load the image
img = Image.open('test1.png')

# Get the size of the image in bytes
image_size_bytes = img.size[0] * img.size[1] * len(img.getbands())

# Convert the size to kilobytes (KB) and megabytes (MB)
image_size_kb = image_size_bytes / 1024
image_size_mb = image_size_kb / 1024

# Convert the image to a NumPy array
numpydata = asarray(img)

# Get the size of the NumPy array in bytes
array_size_bytes = numpydata.nbytes

# Convert the size to kilobytes (KB) and megabytes (MB)
array_size_kb = array_size_bytes / 1024
array_size_mb = array_size_kb / 1024

# Print the size of the image and the array
print("Image size:", "{:.2f} KB ({:.2f} MB)".format(image_size_kb, image_size_mb))
print("Array size:", "{:.2f} KB ({:.2f} MB)".format(array_size_kb, array_size_mb))


# Print the NumPy array
print("NumPy array:\n", numpydata.shape)


data_bytes = numpydata.tobytes()

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the data bytes
hash_object.update(data_bytes)

# Get the hexadecimal representation of the hash
hash_value = hash_object.hexdigest()

# Print the cryptographic hash value
print("Cryptographic Hash (SHA-256):", hash_value)


# Calculate the size of the hash value in bytes
hash_size_bytes = len(hash_value)

# Convert the size to kilobytes (KB) and megabytes (MB)
hash_size_kb = hash_size_bytes / 1024
hash_size_mb = hash_size_kb / 1024

# Print the storage size of the hash value
print("Hash Storage Size: {:.2f} bytes".format(hash_size_bytes))
print("Hash Storage Size: {:.2f} KB".format(hash_size_kb))
print("Hash Storage Size: {:.2f} MB".format(hash_size_mb))