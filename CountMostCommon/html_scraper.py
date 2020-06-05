import urllib.parse
import urllib.error
import urllib.request
from lxml import html
import requests
from bs4 import BeautifulSoup
# from newspaper import Article

file1 = open("urls_to_read.txt")
websites = file1.readlines()
# print(websites)

def html_scraper(websites):
    for url in websites:
        page = requests.get(url, allow_redirects = True)
        soup = BeautifulSoup(page.content, "html.parser")
        paragraphs = soup.find('p')
        print(soup.prettify())


def save_webpage(websites): #test
    # save-webpage.py
    for url in websites:
        response = urllib.request.urlopen(url)
        webContent = response.read()
        f = open('cnn_article.html', 'wb')
        f.write(webContent)
        f.close

html_scraper(websites)
