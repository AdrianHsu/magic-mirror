# coding: utf-8

# In[1]:
import os
import sys
import PyQt5
import feedparser
import requests
import json
import subprocess
import time
# written by AdrianHsu

from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from pathlib import Path
from time import strftime, localtime
#for tts.py
#from bing_voice import *
#import pyaudio
#import wave


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        cb = QPushButton('Switch', self)
        cb.move(20, 20)
        cb.clicked.connect(self.add_entry)
        # self.showFullScreen()

        palette = self.palette()
        role = self.backgroundRole()
        palette.setColor(role, QColor('black'))
        self.setPalette(palette)
        
        page1_widget = Page1Widget(self)
        page1_widget.button.clicked.connect(self.gotopage2)
        self.central_widget.addWidget(page1_widget)

    def gotopage2(self):
        page2_widget = Page2Widget(self)
        page2_widget.button.clicked.connect(self.gotopage3)
        self.central_widget.addWidget(page2_widget)
        self.central_widget.setCurrentWidget(page2_widget)
        
    def gotopage1(self):
        page1_widget = Page1Widget(self)
        page1_widget.button.clicked.connect(self.gotopage2)
        self.central_widget.addWidget(page1_widget)
        self.central_widget.setCurrentWidget(page1_widget)
    def gotopage3(self):
        page3_widget = Page3Widget(self)
        page3_widget.button.clicked.connect(self.gotopage1)
        self.central_widget.addWidget(page3_widget)
        self.central_widget.setCurrentWidget(page3_widget)

    def add_entry(self):
        if self.windowState() & QtCore.Qt.WindowFullScreen:
            self.showNormal()
        else:
            self.showFullScreen()
    
class Page1Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Page1Widget, self).__init__(parent)
        layout = QGridLayout()
        self.button = QtWidgets.QPushButton('goto Page2')
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
        timer.start(10)
 
        self.lcd = QtWidgets.QLCDNumber(self)
#         self.resize(375,130)
        self.lcd.resize(375,100)
        self.lcd.setDigitCount(8)
        self.lcd.setStyleSheet("color: white")
#         self.lcd.setFont(QFont("Helvetica",80,QFont.Bold))  
#Added self.lcd.move and moved the clock 30px down to make space for buttons
#         self.lcd.move(0,30)
        self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
        self.lcd.setSegmentStyle(2)
        self.lcd.setFrameStyle(QFrame.NoFrame);

        day = QDate.currentDate().toString()
        print(day)
        self.label2 = QLabel(day)
        self.label2.setFont(QFont("Avenir Next",60,QFont.Normal))
        self.label2.setStyleSheet("color: white")

        layout.addWidget(self.label2)
        layout.addWidget(self.lcd)

        # class WebPage(QtWebEngineWidgets.QWebEnginePage):
        #     def javaScriptConsoleMessage(self, level, message, lineNumber, sourceId):
        #         #Send the log entry to Python's logging or do whatever you want
        #         logging.info("level: {}, source: {}, "+
        #                  "line: {}, message: {}".format(level,
        #                                                 sourceId,
        #                                                lineNumber,
        #                                                message))
        # self.webView = QtWebEngineWidgets.QWebEngineView(self)
        # path = "file:///Users/AdrianHsu/Google_Drive/NTUEE_105_1/eslab/magic-mirror/annyang/demo/index.html"
        # self.webView.load(QtCore.QUrl(path))
        # self.webView.setObjectName("webView")

        # layout.addWidget(self.webView)

        layoutInner = QGridLayout()
        taipei, weather, temperature, weather_image = self.retrieveWeather()
        self.label_location2 = QLabel(taipei)
        self.label_location2.setFont(QFont("Avenir Next",60,QFont.Normal))
        self.label_location2.setStyleSheet("color: white") 
        self.label_weather = QLabel(temperature +", "+ weather)
        self.label_weather.setFont(QFont("Avenir Next",60,QFont.Normal))
        self.label_weather.setStyleSheet("color: white")         
        pic = QLabel(self)
#         pic.setGeometry(10, 10, 64, 64)
        #use full ABSOLUTE path to the image, not relative
        tmp = QtGui.QPixmap("./assets/Rain.png")
#         tmp = QtGui.QPixmap("./weather_image/" + weather_image[-6:])
        tmp2 = tmp.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
        pic.setPixmap(tmp2)
        layoutInner.addWidget(pic)
        
        layoutInner.addWidget(self.label_location2)
        layoutInner.addWidget(self.label_weather)
        layout.addLayout(layoutInner, 0, 1)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
# Expanded window height by 30px
#         self.setGeometry(300,300,375,130)

    def Time(self):
        self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
    def retrieveWeather(self):
        url = "http://www.cwb.gov.tw/V7/observe/24real/Data/46692.htm"
        page = urlopen(url)

        soup = BeautifulSoup(page, "lxml")

        #print(soup.prettify())
        #print(soup.tr.prettify())
        latest_observe = soup.find_all('tr')[1]
        print("觀測時間：2016/%s" %latest_observe.th.contents[0])
        print("溫度：%sºC" %latest_observe.td.contents[0])

        url_image = "http://www.cwb.gov.tw/V7/life/Life_N.htm"
        page_image = urlopen(url_image)
        soup_image = BeautifulSoup(page_image, "lxml")
        #print(soup_image.prettify())
        taipei_weather = soup_image.find_all('tr')[2]
        taipei = taipei_weather.th.contents[0]
        weather_text = taipei_weather.td.contents[0]['title']
        weather_image = "http://www.cwb.gov.tw"+taipei_weather.td.contents[0]['src']

        image_path = Path("weather_image/"+weather_image[-6:])
        if not image_path.is_file():
            print(weather_image)
            urlretrieve(weather_image, "weather_image/"+weather_image[-6:])
        weather_ptr = 0
        temperature_ptr_begin = weather_text.find('<BR>')+5
        temperature_ptr_end = weather_text.find('<BR>',temperature_ptr_begin)
        weather = weather_text[:temperature_ptr_begin-6]
        temperature = weather_text[temperature_ptr_begin:temperature_ptr_end]
        print(taipei)
        print(weather)
        print(temperature)
        print(weather_image[-6:])
        print(strftime("%Y %b %d %H:%M:%S", localtime()))
        print(strftime("%A"))
        return taipei, weather, temperature, weather_image
        # urlretrieve()
        
class Page2Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Page2Widget, self).__init__(parent)
        layout = QHBoxLayout()
        self.label = QLabel('in page2')
        layout.addWidget(self.label)
        self.button = QtWidgets.QPushButton('goto Page3')
        layout.addWidget(self.button)
        
        url = 'http://news.google.com.br/news?pz=1&cf=all&ned=tw&hl=zh&output=rss'
        feed = feedparser.parse(url)
        str = ""
        for post in feed.entries:
            str = str + "\n" + post.title
        self.label_news = QLabel(str)
        self.label_news.setFont(QFont("Avenir Next",14, QFont.Normal))
        self.label_news.setStyleSheet("color: white")
        layout.addWidget(self.label_news)

        self.setLayout(layout)
        
        
        
class Page3Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Page3Widget, self).__init__(parent)
        layout = QGridLayout()
        self.label = QLabel('in page3')
        layout.addWidget(self.label)
        self.button = QtWidgets.QPushButton('goto Page1')
        layout.addWidget(self.button)
        #self.record_button = QtWidgets.QPushButton('start record')
        #self.record_button.clicked.connect(self.record_start)
        #layout.addWidget(self.record_button)

        self.label2 = QLabel("Hello 秉鈞, How are you today?")
        self.label2.setFont(QFont("Avenir Next",60,QFont.Normal))
        self.label2.setStyleSheet("color: white")

        layout.addWidget(self.label2)
        self.setLayout(layout)

#    def record_start(self):
#        cmd = "arecord -r 16000 -f S16_LE tmp.wav"
#        proc = subprocess.Popen(cmd, shell=True)
#        time.sleep(7)
#        print("test")
#        os.system("pkill -9 arecord")
#        proc.terminate()
#        print("record done!")
#        self.label2.setText("speech recognition")
#        os.system("python3 bing_voice.py tmp.wav > result.txt")
#        filename = "result.txt"
#        with open(filename) as f:
#            data = f.readlines()
#        result = data[0] #what's the weather like
#        self.label2.setText(result)
#        print("set text done:" + result)
#        result.replace(' ', ',')
        #speak_out(result)
        #if "hello" in result:
        #   speak_out("hello")
        #elif "name" in result:
        #    speak_out("your,name,is,adrian")
        #elif "weather" in result:
        #    speak_out("I,dont,know")

#    def speak_out(self, mystr):
#        BING_KEY = '15e52d8feeff44baac29e191e3d8c432'
#        CHUNK_SIZE = 2048
#
#        # if len(sys.argv) < 2:
#        #     print('Usage: python %s text_to_convert' % sys.argv[0])
#        #     sys.exit(-1)
#        bing = BingVoice(BING_KEY)
#        data = bing.synthesize(mystr)
#
#        pa = pyaudio.PyAudio()
#        stream = pa.open(format=pyaudio.paInt16,
#                         channels=1,
#                         rate=16000,
#                         output=True,
#                         # output_device_index=1,
#                         frames_per_buffer=CHUNK_SIZE)
#
#        stream.write(data)
#        stream.close()
#
#        # if len(sys.argv) >= 3:
#        wf = wave.open(mystr, 'wb')
#        wf.setframerate(16000)
#        wf.setnchannels(1)
#        wf.setsampwidth(2)
#
#        wf.writeframes(data)
#        wf.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("Magic Mirror")
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())


# In[ ]:




# In[ ]:



