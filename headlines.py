#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:28:56 2019

@author: l
"""

import feedparser
from flask import Flask
from flask import render_template
from flask import request
import json
import urllib2
import urllib

app = Flask(__name__)
RSS_FEEDS = {'anxiety':'https://www.psychiatryadvisor.com/home/topics/anxiety/feed',
             'mood':'https://www.psychiatryadvisor.com/home/topics/mood-disorders/feed',
                 'depression':'https://www.nature.com/subjects/depression.rss',
                 'dwarves':'http://www.bay12games.com/dwarves/dev_now.rss',
                 'obitOne':'https://www.nytimes.com/services/xml/rss/nyt/Obituaries.xml',
                 'emergencies':'https://afro.who.int/rss/emergencies.xml',
                 'death':'http://rawdataserver.com/CDB/rss'
                 }



@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "anxiety"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    weather = get_weather("Philadelphia,US")
    return render_template("home.html",articles=feed['entries'], weather = weather)

def get_weather():
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=04b64c4599b0c05101d8c22b14bb2379"
    query = urllib.quote(query)
    url = api_url.format(query)
    data = urllib2.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description":parsed["weather"][0]["description"],"temperature":parsed["main"]["temp"],"city":parsed["name"]
                  }
    return weather

if __name__ == '__main__':
  app.run(port=5000, debug=True)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  