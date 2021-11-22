import tkinter 
from PIL import Image,ImageTk,ImageSequence
import os 
import sqlite3 

class App:

	def __init__(self,parent,width = 1024,height = 600):
		self.parent = parent # This is root window
		self.width = width 
		self.height = height
		self.canvas = tkinter.Canvas(parent,width = self.width,height = self.height)
		self.canvas.pack()
		self.animate()

	def dbconnect(self):
		self.conn = sqlite3.connect("./source/site.db")
		c = self.conn.cursor()
		c.execute(f"SELECT *FROM showman WHERE id = 1")
		itype = c.fetchone()[-1]
		if itype == 'emo':
			c.execute(f"SELECT *FROM showman WHERE id = 1")
			emotion = c.fetchone()[2]
			self.conn.commit()
			return itype, emotion
		elif itype == 'info':
			c.execute(f"SELECT *FROM showman WHERE id = 1")
			content = c.fetchone()[1]
			self.conn.commit()
			return itype,content 
		else:
			return None

	def animate(self,stime = 100):

		itype,item = self.dbconnect()

		if itype == 'info':
			content = tkinter.Label(self.parent,text = item,fg = 'black',font= ('Arial',10))
			self.canvas.create_window(512,300,anchor = 'nw',window = content)

		elif itype = 'info':
			conte

root = tkinter.Tk()
app = App(root)
root.mainloop()