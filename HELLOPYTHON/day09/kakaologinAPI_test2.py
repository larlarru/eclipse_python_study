
from selenium import webdriver
import time
 
browser = webdriver.Chrome()

browser.get("https://kauth.kakao.com/oauth/authorize?client_id=b9cfa5b35e3ae75acd84aeb36feb4e2a&redirect_uri=https://localhost:8081/oauth&response_type=code")
# browser.get("http://localhost:8081/WEB2/index.html")
