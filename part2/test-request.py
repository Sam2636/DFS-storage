import requests

url = 'http://localhost:5000/split-image'
image_file = open('test1.png', 'rb')

response = requests.post(url, files={'image': image_file})

data = response.json()
print(data)