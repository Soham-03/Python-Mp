from bs4 import BeautifulSoup
import requests
import csv
import json
import lxml

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=bicep+curls+muscle&btnG='

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'lxml')
for item in soup.select('[data-lid]'):
    print(item)
    print("--------------------------------------------")