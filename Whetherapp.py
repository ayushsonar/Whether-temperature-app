import tkinter as tk
import requests
from tkinter import font
from PIL import Image, ImageTk
height=600
width=600

def Output(whether):
	try:
		name = whether['name']
		desc = whether['weather'][0]['description']
		temperature = whether['main']['temp']
		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temperature)
		return final_str
	except:
		label['text'] = "Problem Occured :("

def get_whether(city):
	whether_key = "be60d5af963ec3d9faeb0f802887a50a"
	url = "https://api.openweathermap.org/data/2.5/weather"
	params = {"APPID": whether_key, "q" : city, "units" : "Metric"}
	response = requests.get(url, params = params)
	whether = response.json()
	label['text'] = Output(whether)
	
root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()
backgroundimage = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=backgroundimage)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="black", bd=5)
frame.place(relx= 0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font =40, bg="white")
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Whether", font=40, bg = "#d2fcfc", fg = "black", command=lambda: get_whether(entry.get()))
button.place(relx= 0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg = 'black', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font = ("Georgia", 20))
label.place(relwidth=1, relheight=1)


root.mainloop()