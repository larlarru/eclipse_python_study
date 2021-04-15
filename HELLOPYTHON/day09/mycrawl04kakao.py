import requests
import json

url = "https://dapi.kakao.com/v2/search/cafe"
queryString = {"query":"대전맛집"}
header = {'authorization':'KakaoAK ea745165ce40f58aa41cb506784a72cf'}
r = requests.get(url, headers=header, params=queryString)

jsonobj = json.loads(r.text)
docus = jsonobj.get("documents")

for i in docus:
    print("cafename:",i.get("cafename") ,end=" ")
    print("contents:",i.get("contents") ,end=" ")
    print("datetime:",i.get("datetime") ,end=" ")
    
    print("thumbnail:",i.get("thumbnail") ,end=" ")
    print("title:",i.get("title") ,end=" ")
    print("url:",i.get("url") )

