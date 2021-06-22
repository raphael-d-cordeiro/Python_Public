import requests
from requests import request
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
for ask in html.select('.question-summary'):
    title = ask.select_one('.question-hyperlink')
    date = ask.select_one('.relativetime')
    vote = ask.select_one('.vote-count-post')

    print(title.text)
    print(date.text, vote.text, sep='\t')
