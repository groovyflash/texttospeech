from bs4 import BeautifulSoup as bs
import epub
import requests
import os
#The next set of functions is scraping the wwebsite for books that will be downloaded
#you must run this in python 3.6 start this file in a conda environment with that level please
#on this computer the environment is named textminer


DOMAIN = 'https://www.feedbooks.com'
#URL = 'http://www.feedbooks.com/books/top?lang=en&page=2'
FILETYPE = '.epub'
directory = "/home/ttscomp/Desktop/TTS/"
books = []
 
def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

def get_html(URL):
    for link in get_soup(URL).find_all('a'):
        file_link = link.get('href')
        if FILETYPE in file_link:
            print(file_link)
            r=requests.get(file_link, allow_redirects=True)
            open("hello.epub", 'wb').write(r.content)
            with epub.open_epub("hello.epub") as book:
                title = book.opf.metadata.titles[0][0]
            os.rename("hello.epub", title + ".epub")
            books.append([title + ".epub"])


out = input()
get_html(out)
