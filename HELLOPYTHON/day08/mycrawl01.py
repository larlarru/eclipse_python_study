from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8081/WEB2/crw.jsp")
# html = urlopen("http://www.naver.com")
print(html)
bsObject = BeautifulSoup(html, "html.parser")

# 태그 포함 출력
print(bsObject.head.title)

# 태그 내의 text만 출력

print(bsObject.text)
print("\n\n")
# print(bsObject.table.find_all('td'))
print("\n\n")
# print(bsObject.head.find_all('meta'))
# print(bsObject)