# This is a simple web-scraper to retrieve profile pictures from github

import requests
from bs4 import BeautifulSoup as bs

gh_user = input('Input the user to search: ')
url = 'https://github.com/' + gh_user

# send a request to the url / get answer in html form
req = requests.get(url)
soup = bs(req.content, 'html.parser')

prof_image = soup.find('img', {'alt': 'Avatar'})['src']
print(prof_image)

