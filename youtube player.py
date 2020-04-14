# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:36:20 2019

@author: rohan
"""
import urllib.request
import urllib.parse
import re
import vlc
import pafy
query_string = urllib.parse.urlencode({"search_query" : input()})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url = "http://www.youtube.com/watch?v=" + search_results[0]
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
media.play()
c = input()
if c=='q':
    media.stop()