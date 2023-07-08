import requests

# get request
# response = requests.get("https://www.google.com")
# print(response.text)


# post request
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "userId": 1,
#     "id": 1,
#     "title": "Hello, world!",
# }

# headers = {
#     "Content-Type": "application/json"
# }

# response = requests.post(url, headers=headers, json=data)
# print(response.text)

# bs4 MODULE
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)