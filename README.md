#Magic Mirror

arecord -r 16000 -f S6_LE tmp.wav  
wf = wave.open("tmp.wav")  
wf.getframerate() is 16000 (sample rate: 16000)  
wf.getnchannels() is 1 (channel)  
wf.getsampwidth() is 2 (byte depth)  

#generate the WAV file content  
with io.BytesIO() as wav_file:  
wav_writer = wave.open(wav_file, "wb")  
wav_writer.setframerate(16000)  
wav_data = wav_file.getvalue()  
finally... wav_writer.close()  

#Subprocess control

[http://xmodulo.com/how-to-capture-microphone-input-to-wav-format-file.html](http://xmodulo.com/how-to-capture-microphone-input-to-wav-format-file.html)  

sudo apt-get install mediainfo  
proc = subprocess.Popen(cmd, shell=True)  
in parent:  
os.system("pkill -9 arecord")  
proc.terminate()  

# BLE Programming
from lab 7

(target) sudo apt-get update
(target) sudo apt-get dost-upgrade
(target) sudo apt-get install bluez blueman libbluetooth-dev
(target) sudo reboot
(target) sudo systemctl status bluetooth
(target) sudo vi /etc/systemd/system/dbus-org.bluez.service
改這行：ExecStart=/usr/lib/bluetooth/bluetoothd --compat
(target) sudo systemctl daemon-reload
(target) sudo systemctl restart bluetooth
(target) sudo hciconfig hci0 up

PART 1

(target) sudo bluetoothctl
[Bluetooth]# agent on
[Bluetooth]# default-agent
scan on -> 找到後 -> trust -> pair

PART 2

(target) run python & c program

for this demo

sudo apt-get update && sudo apt-get upgrade
sudo rpi-update
sudo aptitude install libglib2.0-dev libdbus-1-dev libudev-dev libicaldev libreadline6-dev

following here: http://joshondesign.com/2013/10/23/noderpi
curl -sL https://deb.nodesource.com/setup | sudo bash -
sudo apt-get install nodejs

Activate bluetooth adapter:

hciconfig
sudo hciconfig hci0 up

Download the nodejs code and run it:

sudo node eddystone-beacon.js
