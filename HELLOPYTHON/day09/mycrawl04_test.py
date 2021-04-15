import simplejson, requests
import sys

url = "https://dapi.kakao.com/v2/search/web"
apikey = "c34fc032d15b3a02e99d2ef75ada18f1"
subj = "대전맛집"

r = requests.get( url, 
                  params = {'query':subj}, 
                  headers = {'Authorization' : 'KakaoAK ' + apikey} )
#                   headers = {'Authorization' : 'KakaoAK' + apikey} )
js = simplejson.JSONEncoder().encode(r.json())

for i in r.json()["documents"] :
    print("\n")
    print(i["title"])
    print(i["url"])
    print(i["datetime"])
    print(i["contents"])