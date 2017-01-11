#!/bin/bash
# parameter 1 : file name, contains flac encoded voice recording
 
echo Sending FLAC encoded Sound File to Google:
key='AIzaSyDdCfD8srYdwqeeaynleOKxW6ymfTgaaWI'
url='https://www.google.com/speech-api/v2/recognize?output=json&amp;amp;lang=en-us&amp;amp;key='$key
curl -i -X POST -H "Content-Type: audio/x-flac; rate=16000" --data-binary @$1 $url
echo '..all done'
