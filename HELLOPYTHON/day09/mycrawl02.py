from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8081/WEB2/crw.jsp")
bs = BeautifulSoup(html, "html.parser")

tds = bs.find_all("td");
for i in tds :
    print(i.text)

