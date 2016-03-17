import tkinter
from tkinter import *
#from tkinter.ttk import *

import urllib.request
import urllib.error
import urllib.parse
import json

def create_window():
	pu_window = tkinter.Toplevel(window)
	pu_window.geometry("800x480")
	pu_window.configure(background='goldenrod')

def fetch_weather():
	print ("Fetching new weather data...")
	#-------------------------------------------------#
	#api = urllib.request.urlopen('http://api.wunderground.com/api/1153cd7c28e94f7a/geolookup/conditions/q/NY/Binghamton.json')
	#json_string = api.readall().decode('utf-8')
	#parsed_json = json.loads(json_string)
	#location = parsed_json['location']['city']
	#temp_f = parsed_json['current_observation']['temp_f']
	#print (("Current temperature in %s is: %s" % (location, temp_f)))
	#api.close()
	#-------------------------------------------------#
	
	temp_f=40 #DELETE *********************************
	location="Binghamton" #DELETE *********************
	print (("Current temperature in %s is: %s" % (location, temp_f))) #DELETE********************

	temp = Label(window, text=temp_f, bg="bisque", font=("Helvetica", 15))
	temp.grid(row=3, rowspan=3, column=1)
	city = Label(window, text=location, bg="bisque", font=("Helvetica", 15))
	city.grid(row=6, rowspan=3, column=1)
	return None

window = tkinter.Tk()

window.title("ThinkHome UI")
window.geometry("800x480")
window.configure(background='bisque')
fetch_weather()

title = Label(window, text="ThinkHome", bg="bisque",font=("Helvetica", 30))
title.grid(row=1, rowspan=3, column=2, sticky=N)
b1 = Button(window, text="Button 1", bg="bisque", command=create_window )
b1.grid(row=9, rowspan=3, column=3)

b2 = Button(window,text="Refresh", bg="bisque", command=fetch_weather )
b2.grid(row=9, rowspan=3, column=1)

#title.pack(side=TOP)
#b1.pack(side=LEFT)
#b2.pack(side=CENTER)

window.mainloop()