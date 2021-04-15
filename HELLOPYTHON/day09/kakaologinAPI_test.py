from flask import Flask, render_template, redirect, url_for, request
import requests
import json
app = Flask(__name__)
  
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/oauth')
def oauth():
    
    code = str(request.args.get('code'))
#     return str(code)


    url = "https://kauth.kakao.com/oauth/token"
    payload = "grant_type=authorization_code&client_id=b9cfa5b35e3ae75acd84aeb36feb4e2a&redirect_uri=https%3A%2F%2Flocalhost%3A8081%2Foauth&code=" + str(code)
    headers = {
        'Content-Type':'aaplication/x-www-form-urlencoded',
        'Cache-Control':'no-cache'
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    access_token = json.loads(((response.text).encode('utf-8')))['access_token']
#     return access_token

    url = "https://kapi.kakao.com/v1/user/sinup"
    
    headers.update({'Authorization':"Bearer " + str(access_token)})
    response = requests.request("POST", url, headers=headers)
    
#     return (response.text)

    url="https://kapi.kakao.com/v1/user/me"
    
    response = requests.request("POST", url, headers=headers)
    
    return (response.text)

if __name__ == '__name__':
    app.run(debug = True)