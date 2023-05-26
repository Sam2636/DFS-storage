import numpy as np
from PIL import Image

# Load the image
image = Image.open("part2/test1.png")

# Convert the image to a NumPy array
image_array = np.array(image)

# Split the image array along the channel axis
channels = np.split(image_array, image_array.shape[2], axis=2)
print(channels)
# Convert each channel array back to an image
reconstructed_images = []
for channel in channels:
    reconstructed_image = Image.fromarray(np.squeeze(channel))
    reconstructed_images.append(reconstructed_image)
print(reconstructed_images)
# Display the reconstructed images
for i, image in enumerate(reconstructed_images):
    image.show()
