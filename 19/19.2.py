import requests

response = requests.get("https://randomuser.me/api/")

user = response.json()["results"][0]
name = user["name"]["first"] + " " + user["name"]["last"]
country = user["location"]["country"]
phone = user["phone"]

print(f"Hi, I'm {name}, I'm from {country}, my phone number is {phone}")