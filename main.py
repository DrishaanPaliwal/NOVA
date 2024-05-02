import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import pyfiglet
import pyautogui
#import pygame
import subprocess
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from newsapi import base_news
#import gui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Evening Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Evening Sir !") 

	else:
		speak("Good Evening Sir !") 

	assname =("NOVA 1 point o")
	speak("I am your Assistant")
	speak(assname)
	ascii_banner = pyfiglet.figlet_format(assname)
	print(ascii_banner)
	

	

def username():
	speak("Good Evening Sir, Vineet, KKN, Panchi. Good Evening Everyone, I hope you are having a good time.")
	speak("How CAN I help you sir")
	uname = takeCommand()
	#if uname == "operator":
		#speak("Welcome Master")
		#speak("Drishaan")
		#columns = shutil.get_terminal_size().columns
	
		#print("#####################".center(columns))
		#print("Welcome Master.", "Drishaan".center(columns))
		#print("#####################".center(columns))
	
		#speak("How can i Help you, Sir")
	
	#elif uname == "class":
		#speak("Greetings Teacher")
	#else:
		#speak("You are denied access")
		#quit()

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('your email id', 'your email password')
	server.sendmail('your email id', to, content)
	server.close()
 


if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	#wishMe()
	#username()
	#display()
	#face()
	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be 
		# stored here in 'query' and will be
		# converted to lower case for easily 
		# recognition of command
		if 'find out' in query:
			speak('Searching Wikipedia...')
			query = query.replace("what is", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)
			if wikipedia.exceptions.PageError:
				speak("page not found")
		elif 'greet' in query:
			speak("​Good evening, ladies, and gentlemen. it's, a pleasure,. to welcome, such a wonderful, and intrigued, audience, to the 8th, founders. day.")
		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")
		elif 'search' in query:
			speak('Searching Google...\n')
			query = query.replace("what is", "")
			webbrowser.open("https://google.com/" + query + "/")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com") 

		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			# music_dir = "G:\\Song"
			music_dir = "C:\\Users\\GAURAV\\Music"
			songs = os.listdir(music_dir)
			print(songs) 
			random = os.startfile(os.path.join(music_dir, songs[1]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("% H:% M:% S") 
			speak(f"Sir, the time is {strTime}")

		elif 'open opera' in query:
			codePath = r"C:\Users\drish\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Opera GX Browser.lnk"
			os.startfile(codePath)

		elif 'email to drishaan' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "Receiver email address"
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'send a mail' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				speak("whome should i send")
				to = input() 
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query: 
			speak("I have been created by Drishaan.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			
		elif "calculate" in query: 
			
			app_id = "85ELX6-GRRWE3KVJ3"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate') 
			query = query.split()[indx + 1:] 
			res = client.query(' '.join(query)) 
			answer = next(res.results).text
			print("The answer is " + answer) 
			speak("The answer is " + answer) 

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 

		elif "who i am" in query:
			speak("If you talk then definitely your human.")

		elif "why you came to world" in query:
			speak("To kill everyone who defy my master.")

		elif 'power point presentation' in query:
			speak("opening Power Point presentation")
			power = r"C:\\Users\\drish\\Desktop\\Presentation.pptx"
			os.startfile(power)

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by Drishaan")

		elif 'reason for you' in query:
			speak("To destroy all opposition to lord Drishaan ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20, 
													0, 
													"Location of wallpaper",
													0)
			speak("Background changed successfully")

		elif 'open bluestack' in query:
			appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
			os.startfile(appli)

		elif 'news' in query:
			
			try: 
				jsonObj = urlopen('https://newsapi.org/v2/everything?''q=Apple&''from=2023-11-27&''sortBy=popularity&''apiKey=d56a722eb571486d9ca18ed02ceb9edd')
				data = json.load(jsonObj)
				i = 1
				
				speak('here are some top news from the times of india')
				print('''=============== TIMES OF INDIA ============'''+ '\n')
				
				for item in data['articles']:
					
					print(str(i) + '. ' + item['title'] + '\n')
					print(item['description'] + '\n')
					speak(str(i) + '. ' + item['title'] + '\n')
					i += 1
			except Exception as e:
				
				print(str(e))

		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.com/maps/dir//" + location + "/")

		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "SITA Camera ", "img.jpg")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])
		elif "quit" in query:
			quit()

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r") 
			print(file.read())
			speak(file.read(6))

		elif "update assistant" in query:
			speak("After downloading file please replace this file with the downloaded one")
			url = '# url after uploading file'
			r = requests.get(url, stream = True)
			
			with open("Voice.py", "wb") as Pypdf:
				
				total_length = int(r.headers.get('content-length'))
				
				for ch in progress.bar(r.iter_content(chunk_size = 2391975),
									expected_size =(total_length / 1024) + 1):
					if ch:
						Pypdf.write(ch)
					
		# NPPR9-FWDCX-D2C8J-H872K-2YT43
		elif "Daddy" in query:
			
			wishMe()
			speak("Daddy 1 point o in your service Mister")
			speak(assname)

		elif "weather" in query:
			
			# Google Open weather website
			# To Do: API of Open weather 
			api_key = "Api key"
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url) 
			x = response.json() 
			
			if x["code"] != "404": 
				y = x["main"] 
				current_temperature = y["temp"] 
				current_pressure = y["pressure"] 
				current_humidiy = y["humidity"] 
				z = x["weather"] 
				weather_description = z[0]["description"] 
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
			
			else: 
				speak(" City Not Found ")
			
		elif "send message " in query:
				#To Do: Add Acc Key, and Auth Token
				account_sid = 'Account Sid key'
				auth_token = 'Auth token'
				client = Client(account_sid, auth_token)

				message = client.messages \
								.create(
									body = takeCommand(),
									from_='Sender No',
									to ='Receiver No'
								)

				print(message.sid)

		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query: 
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("Cannot compute love")

		elif "what is" in query or "who is" in query:
			
			# Use the same API key 
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")
		elif "open book" in query:
			speak("please tell me the subject and chapter number")
			aa = takeCommand()
			print(aa)
			if aa == "science chapter 1":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 1.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 2":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 2.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 3":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 3.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 4":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 4.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 5":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 5.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 6":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 6.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 7":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 7.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 8":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 8.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 9":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 9.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 9":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 10.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 9":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 11.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "science chapter 9":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Science Chapter 12.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "history chapter 1":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\History Chapter 1.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "history chapter 2":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\History Chapter 2.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "history chapter 3":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\History Chapter 3.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "history chapter 4":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\History Chapter 4.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "civics chapter 4":
				path =(r"C:\Users\drish\OneDrive\Documents\Project\Books\Civics Chapter 4.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "Geography Chapter 6":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Geography Chapter 6.pdf")
				subprocess.Popen([path], shell = True)
			if aa == "Hindi chapter 4":
				path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Hindi Chapter 4.pdf")
				subprocess.Popen([path], shell = True)
		
		elif "open english presentation" in query:
			path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\no men are foreign.pptx")
			os.startfile(path)
		elif "open python presentation" in query:
			path = (r"C:\Users\drish\OneDrive\Documents\Project\Books\Python for Loop.pptx")
			os.startfile(path)
   
		
		# elif "" in query:
			# Command go here
			# For adding more commands
   
   
