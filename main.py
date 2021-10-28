import requests

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""

url = url_host + endpoint + query

response = requests.get(url)
breeds = response.json()["message"]
poodle = breeds.get("poodle")

print(poodle)

all_breeds = breeds.keys()

for breed in all_breeds:
  print(breed)

poodle_subbreeds = breeds["poodle"]
input("\nPress enter to get all poodle subbreeds")
for sub in poodle_subbreeds:
  print(sub)