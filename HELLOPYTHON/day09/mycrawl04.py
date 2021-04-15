import simplejson,requests
import sys
url = "https://dapi.kakao.com/v2/search/web"
# apikey = "c34fc032d15b3a02e99d2ef75ada18f1"
# subj = "아이유"
# r = requests.get( url, 
#                   params = {'query':subj}, 
#                   headers={'Authorization' : 'KakaoAK ' + apikey } )
# js = simplejson.JSONEncoder().encode(r.json())
# for i in r.json()["documents"] :
#     print (i["title"])
#     print (i["url"])
#     print (i["datetime"])
#     print (i["contents"])

queryString = {"query":"대전맛집"}
header = {"authorization":"KakaoAK c34fc032d15b3a02e99d2ef75ada18f1"}
r = requests.get(url, headers=header, params=queryString)
print()