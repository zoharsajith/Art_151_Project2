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
    body = "human body"
    nerves = "nerves"
    skeleton = "skeleton"
    muscles = "muscles"

    headers = {'User-Agent': 'Mozilla/5.0'}

    search  = body

    page = requests.get(f"https://en.wikipedia.org/wiki/{search}")
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.text[303:1500]

    return render_template("index.html", text = text)

@app.route('/nerves')

def nerves():
    body = "human body"
    nerves = "nerves"
    skeleton = "skeleton"
    muscles = "muscles"

    headers = {'User-Agent': 'Mozilla/5.0'}

    search  = nerves

    page = requests.get(f"https://en.wikipedia.org/wiki/{search}")
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.text[300:1500]

    return render_template("nerves.html", text = text)

@app.route('/skeleton')

def skeleton():

    body = "human body"
    nerves = "nerves"
    skeleton = "skeleton"
    muscles = "muscles"

    headers = {'User-Agent': 'Mozilla/5.0'}

    search  = skeleton

    page = requests.get(f"https://en.wikipedia.org/wiki/{search}")
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.text[400:1200]
    return render_template("skeleton.html", text = text)

@app.route('/muscles')

def muscle():

    body = "human body"
    nerves = "nerves"
    skeleton = "skeleton"
    muscles = "muscles"

    headers = {'User-Agent': 'Mozilla/5.0'}

    search  = muscles

    page = requests.get(f"https://en.wikipedia.org/wiki/{search}", headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.text[400:1900]
    return render_template("muscles.html", text = text)


