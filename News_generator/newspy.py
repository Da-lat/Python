import requests
from sys import argv
from tkinter import *

root = Tk()
root.title("Top News today")
root.geometry("500x350")

title = Label(root, text="Top news stories", font=("Helvetica", 40), bg="#984ea3", fg="aquamarine")
title.pack(pady=20, ipadx=10, ipady=10)

API_KEY = 'c97f53b4282741fc96b019c2c8a31f6f'

URL = ('https://newsapi.org/v2/top-headlines?')

def get_artciles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_artciles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')
    return results

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=query_parameters)

    sources = response.json()['sources']

    for source in sources:
        print(source['name'])
        print(source['url'])


if __name__ == "__main__":
    print(f"Getting news for {argv[1]}...\n")
    news = get_artciles_by_category(argv[1])


    news_list = Listbox(root, font=("Helvetica", 15), highlightcolor="blue", cursor="dot")
    news_list.pack(fill=BOTH, expand=1)

    for article in news: 
        news_list.insert(END, article)
        news_list.insert(END, "\n")
    # news_label = Label(root, text=f"{news_list}", font=("Helvetica", 10))
    # news_label.pack(pady=20)


    print(f"Successfully retrieved top {argv[1]} headlines")
    # get_artciles_by_query("Liz Truss"))
    #print_sources_by_category("technology")

root.mainloop()