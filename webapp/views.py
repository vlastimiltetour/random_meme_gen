from flask import Flask, Blueprint,render_template, request
import requests
import json
#https://github.com/D3vd/Meme_Api


views = Blueprint(__name__, "views")

def render_meme():
    url = "https://meme-api.herokuapp.com/gimme"

    response = json.loads(requests.request('GET', url).text)
    meme_large = response['preview'][-2]
    subreddit = response['subreddit']
    return meme_large, subreddit



@views.route('/')
def main():
    meme, subreddit = render_meme()
    return render_template('index.html', subreddit=subreddit,meme=meme)


