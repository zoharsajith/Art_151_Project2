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

    results = 1
    page = requests.get(f"https://en.wikipedia.org/wiki/{search}")
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.text[1000:1500]




    return render_template("index.html", text = text)

@app.route('/nerves')

def BONE():
    return render_template("nerves.html")

@app.route('/skeleton')

def NERVES():
    return render_template("skeleton.html")

@app.route('/muscle')

def MUSCLES():
    return render_template("muscle.html")


