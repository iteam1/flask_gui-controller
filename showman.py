import tkinter 
from PIL import Image,ImageTk,ImageSequence
import os 
import sqlite3 

class App:

	def __init__(self,parent,width = 1024,height = 600,path = './source/static/huma/'):
		self.parent = parent # This is root window
		self.path = path # the path lead to gif, images,... of the showman
		self.width = width 
		self.height = height
		self.canvas = tkinter.Canvas(parent,width = self.width,height = self.height)
		self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(self.path + 'happyblink' +'.gif'))]
		self.canvas.pack()
		self.animate(1)

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
		elif itype == 'img':
			c.execute(f"SELECT *FROM showman WHERE id = 1")
			content = c.fetchone()[3]
			self.conn.commit()
			return itype,content 
		else:
			return None

	def animate(self,counter,stime = 50):

		itype,item = self.dbconnect()

		if itype == 'info':
			self.canvas.delete("all") # clear canvas before draw something new
			content = tkinter.Label(self.parent,text = item,fg = 'black',font= ('Arial',30))
			self.canvas.create_window(312,250,anchor = 'nw',window = content)
			self.parent.after(stime, lambda: self.animate(0))

		elif itype == 'emo':
			self.canvas.delete("all")
			self.sequence = [ImageTk.PhotoImage(img.resize(((self.width),(self.height)))) for img in ImageSequence.Iterator(Image.open(self.path + item +'.gif'))]
			self.image = self.canvas.create_image(512,300,image= self.sequence[0])
			try:
				self.canvas.itemconfig(self.image, image = self.sequence[counter])
			except:
				pass
			self.parent.after(stime,lambda: self.animate((counter+1)%len(self.sequence)))

		elif itype == 'img':
			self.canvas.delete("all")
			img = Image.open(self.path + item +'.png')
			img = img.resize(((self.width),(self.height)))
			self.image = ImageTk.PhotoImage(img)
			self.canvas.create_image(0,0,anchor = 'nw',image = self.image)
			self.parent.after(stime, lambda: self.animate(0))


root = tkinter.Tk()
app = App(root)
root.mainloop()