#!/usr/bin/

import sys
import subprocess
import time
import random
import datetime
import sys
import time
from pprint import pprint
from difflib import SequenceMatcher
from wit import Wit

def query():
	
	client_wit = Wit(API KEY HERE)

	try:
		while True:
			subprocess.call(['rec test.wav rate 32k silence 1 0.1 3% 1 1.0 3%'], shell=True)
			resp = None
			with open('test.wav', 'rb') as f:
			  resp = client_wit.speech(f, None, {'Content-Type': 'audio/wav'})
			inputWords = str(resp['_text'])
			print inputWords
			if "five" in inputWords:
				subprocess.call(['qemu-system-i386 -full-screen -localtime -cpu 486 -m 32 -boot d -hda win95.qcow'], shell=True)
			if "eight" in inputWords:
				subprocess.call(['qemu-system-i386 -full-screen -localtime -cpu 486 -m 128 -boot d -hda win98.img'], shell=True)
			if "x" in inputWords:
				subprocess.call(['qemu-system-x68_64 -full-screen -m 256 -hda winXP.img'], shell=True)
			if inputWords == "reboot":
				subprocess.call(['sudo reboot'], shell=True)
			if inputWords == "shut down":
				subprocess.call(['sudo shutdown -h now'], shell=True)
	except: 
	  pass
	  
while True:
		query()

