# import requests
# from bs4 import BeautifulSoup
# def crawler(): 
#     
#     url = 'https://www.google.com'
#     html = requests.get(url)
#     print(html.text)
# crawler()

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject)