"""
// The MIT License (MIT)

// Copyright (c) YEAR NAME

//  Permission is hereby granted, free of charge, to any person obtaining a
//  copy of this software and associated documentation files (the "Software"),
//  to deal in the Software without restriction, including without limitation
//  the rights to use, copy, modify, merge, publish, distribute, sublicense,
//  and/or sell copies of the Software, and to permit persons to whom the
//  Software is furnished to do so, subject to the following conditions:
//
//  The above copyright notice and this permission notice shall be included in
//  all copies or substantial portions of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
//  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
//  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
//  DEALINGS IN THE SOFTWARE.
"""

# What the fuck to do?
# Let's make something to find apartments... Hmm 
import requests
from bs4 import BeautifulSoup

def fetch_apartments(location, min_price, max_price, bedrooms):
    url = f'https://{location}.craigslist.org/search/apa?min_price={min_price}&max_price={max_price}&bedrooms={bedrooms}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all('li', class_='result-row')

    apartments = []
    for listing in listings:
        title = listing.find('a', class_='result-title hdrlnk').text
        price = listing.find('span', class_='result-price').text
        neighborhood = listing.find('span', class_='result-hood')
        neighborhood = neighborhood.text.strip() if neighborhood else 'N/A'
        link = listing.find('a', class_='result-title hdrlnk')['href']

        apartments.append({
            'title': title,
            'price': price,
            'neighborhood': neighborhood,
            'link': link
        })

    return apartments

# Specify your search parameters
location = 'washingtondc'  # Craigslist subdomain, e.g., 'washingtondc', 'newyork', etc.
min_price = 1500
max_price = 2250
bedrooms = 2

# Fetch and display the apartments
apartments = fetch_apartments(location, min_price, max_price, bedrooms)
for apt in apartments:
    print(f"Title: {apt['title']}")
    print(f"Price: {apt['price']}")
    print(f"Neighborhood: {apt['neighborhood']}")
    print(f"Link: {apt['link']}")
    print('-' * 40)


