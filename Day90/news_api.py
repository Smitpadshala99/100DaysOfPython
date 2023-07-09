#  Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application ?

import requests

API_KEY = 'https://newsapi.org/ '
BASE_URL = 'https://newsapi.org/v2/top-headlines'

def fetch_news(topic):
    params = {
        'apiKey': API_KEY,
        'country': 'india',
        'category': topic.lower()
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['status'] == 'ok':
        articles = data['articles']
        print(f"Top news related to {topic}:")
        for i, article in enumerate(articles, start=1):
            print(f"\n{i}. {article['title']}")
            print(article['description'])
            print(f"Read more: {article['url']}")
    else:
        print("Failed to fetch news.")

def main():
    print("Welcome to Daily News!")

    while True:
        print("\nSelect a type of news:")
        print("1. Technology")
        print("2. Business")
        print("3. Entertainment")
        print("4. Health")
        print("5. Science")
        print("6. Sports")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            fetch_news('technology')
        elif choice == '2':
            fetch_news('business')
        elif choice == '3':
            fetch_news('entertainment')
        elif choice == '4':
            fetch_news('health')
        elif choice == '5':
            fetch_news('science')
        elif choice == '6':
            fetch_news('sports')
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
