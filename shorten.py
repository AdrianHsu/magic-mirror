#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import json
import requests
url = 'http://news.google.com.br/news?pz=1&cf=all&ned=tw&hl=zh&output=rss' 
# just some GNews feed - I'll use a specific search later

feed = feedparser.parse(url)
for post in feed.entries:
   print(post.links[0]['href'])
   print(post.title)
   break
   #print(post.keys())

def goo_shorten_url(url):
   post_url = 'https://www.googleapis.com/urlshortener/v1/url'
   payload = {'longUrl': url}
   headers = {'content-type': 'application/json'}
   r = requests.post(post_url, data=json.dumps(payload), headers=headers)
   print(r.text)
goo_shorten_url("http://stackoverflow.com/questions/17357351/how-to-use-google-shortener-api-with-python")
