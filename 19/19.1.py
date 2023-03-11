import requests

url = "https://cataas.com/cat"
for i in range(2):
    name = "cat" + str(i) + ".jpeg"
    response = requests.get(url)
    with open(name, "wb") as f:
        f.write(response.content)

url = "https://cataas.com/cat?type=or"
for j in range(2):
    name = "cat" + str(j+5) + ".jpeg"
    response = requests.get(url)
    with open(name, "wb") as f:
        f.write(response.content)

url = "https://cataas.com/cat?filter=pixel"
for k in range(2):
    name = "cat" + str(k+10) + ".jpeg"
    response = requests.get(url)
    with open(name, "wb") as f:
        f.write(response.content)