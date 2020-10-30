#import flask object 
from flask import Flask, render_template 

app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
import re
import time

@app.route('/')

def index():
    #set up list
    nerves = "nerves"
    skeleton = "skeleton"
    muscles = "muscles"

    headers = {'User-Agent': 'Mozilla/5.0'}

    number = 0

    for i in range(0, 40):
        if i < 40:
            #move through list
            search = nerves
            article = []
            results = 100 # valid options 10, 20, 30, 40, 50, and 100
            page = requests.get(f"https://www.google.com/search?q={search}&num={results}&pws=0",headers = headers)
            soup = BeautifulSoup(page.content, "html.parser")
            links = soup.findAll("a")
            for link in links :
                link_href = link.get('href')
                if "url?q=" in link_href and not "webcache" in link_href:
                    article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

            page = requests.get(f'{article[number]}', headers = headers)
            soup = BeautifulSoup(page.text, 'html.parser')
            text = soup.find('p').getText()


        return render_template("index.html", text = text)
        time.sleep(0.1)
        i = i + 1

@app.route('/nerves')

def BONE():
    return render_template("nerves.html")

@app.route('/skeleton')

def NERVES():
    return render_template("skeleton.html")

@app.route('/muscle')

def MUSCLES():
    return render_template("muscle.html")


