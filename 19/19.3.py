import requests
import json

start_issue = 15
end_number = 5

num_characters = end_number * 5

response = requests.get(f"https://rickandmortyapi.com/api/character/?page=1")
data = response.json()

characters = []
while len(characters) < num_characters:
    for character in data["results"]:
        if character["name"].startswith(f"#{start_issue}"):
            response = requests.get(character["origin"]["url"])
            planet_data = response.json()
            home_planet = planet_data["name"]

            episode_list = []
            for episode_url in character["episode"]:
                response = requests.get(episode_url)
                episode_data = response.json()
                episode_list.append(episode_data["name"])

            characters.append({
                "name": character["name"],
                "home_planet": home_planet,
                "episode_list": episode_list
            })

    if data["info"]["next"] is not None:
        response = requests.get(data["info"]["next"])
        data = response.json()
    else:
        break

with open("characters.json", "w") as f:
    json.dump(characters, f)
