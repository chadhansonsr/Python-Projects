import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "video/2")
print(response.json())

response = requests.put(BASE + "video/2", {"name":"how to put", "views":99, "likes":101})
print(response.json())

response = requests.get(BASE + "video/2")
print(response.json())

response = requests.patch(BASE + "video/2", {"name":"how to putt", "views":9999, "likes":10101})
print(response.json())

response = requests.delete(BASE + "video/2")
print(response.json())

response = requests.get(BASE + "video/2")
print(response.json())