# importing the required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# collecting the website data using main url.

page = requests.get('https://www.chapters.indigo.ca/en-ca/books/?link-usage=Header%3A%20https%3A%2F%2Fwww.chapters.indigo.ca%2Fen-ca%2Fbooks%2F%3Fmc%3DBook%26lu%3DMain&mc=Book&lu=Main')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
books=soup.find(id='ctl00_ctl00_MainContent_MainContent_dz3_ctl22_ctl08_GridLayoutContainer')
#print(books)

items = books.find_all(class_='product-list__results-container--grid-sort')

print(items)

print(items[0].find(class_='product-list__product-title-link--grid').get_text())
print(items[0].find(class_='product-list__author-link product-list__contributor').get_text())
print(items[0].find(class_='product-list__grid-price').get_text())
print(items[0].find(class_='product-list__grid-availability').get_text())


book_names = [item.find(class_='product-list__product-title-link--grid').get_text() for item in items]
author_names = [item.find(class_='product-list__author-link product-list__contributor').get_text() for item in items]
book_price = [item.find(class_='product-list__grid-price').get_text() for item in items]
Availability = [item.find(class_='product-list__grid-availability').get_text() for item in items]
print(book_names)
print(author_names)
print(book_price)
print(Availability)

#data storing using Pandas
BookCollection = pd.DataFrame(
    {
        'booknames': book_names,
        'Author': author_names,
        'Price': book_price,
        'Availability': Availability
    })
print(BookCollection)
BookCollection.to_csv('Books.csv')