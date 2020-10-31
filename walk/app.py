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
    body = "body"
    nerves = "nerves"
    skeleton = "skeleton"
    muscles = "muscles"

    headers = {'User-Agent': 'Mozilla/5.0'}

    search  = body

    page = requests.get(f"https://en.wikipedia.org/wiki/{search}")
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.text[1000:1500]

    return render_template("index.html", text = text)

@app.route('/nerves')

def nerves():
    body = "body"
    nerves = "nerves"
    skeleton = "skeleton"
    muscles = "muscles"

    headers = {'User-Agent': 'Mozilla/5.0'}

    search  = nerves

    page = requests.get(f"https://en.wikipedia.org/wiki/{search}")
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.text[1000:1500]

    return render_template("nerves.html", text = text)

@app.route('/skeleton')

def skeleton():

    body = "body"
    nerves = "nerves"
    skeleton = "skeleton"
    muscles = "muscles"

    headers = {'User-Agent': 'Mozilla/5.0'}

    search  = skeleton

    page = requests.get(f"https://en.wikipedia.org/wiki/{search}")
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.text[1000:1500]
    return render_template("skeleton.html", text = text)

@app.route('/muscle')

def muscle():

    body = "body"
    nerves = "nerves"
    skeleton = "skeleton"
    muscles = "muscles"

    headers = {'User-Agent': 'Mozilla/5.0'}

    search  = muscles

    page = requests.get(f"https://en.wikipedia.org/wiki/{search}")
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.text[1000:1500]
    return render_template("muscle.html", text = text)


