import requests

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""

url = url_host + endpoint + query

response = requests.get(url)
print(response.json())