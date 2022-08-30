from flask import Flask, render_template, request
import requests
import json
#https://github.com/D3vd/Meme_Api


app = Flask(__name__)

def render_meme():
    url = "https://meme-api.herokuapp.com/gimme"

    response = json.loads(requests.request('GET', url).text)
    meme_large = response['preview'][-2]
    subreddit = response['subreddit']
    return meme_large, subreddit



@app.route('/')
def main():
    meme, subreddit = render_meme()
    return render_template('index.html', subreddit=subreddit,meme=meme)


if __name__ == "__main__":
    app.run()