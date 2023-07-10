import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-07-08&to=2023-07-08&sortBy=popularity&apiKey=4797c4ed6c2348d89979a8f33f72cddc"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------------------")