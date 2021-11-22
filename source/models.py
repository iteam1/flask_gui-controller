from source import db 

class GUI(db.Model):
	id = db.Column(db.Integer,primary_key = True) # the showman's id
	content = db.Column(db.String(),nullable = False, default = 'Good days') # The sentece will display on showman window
	emotion = db.Column(db.String(),nullable = False,default = 'happyblink') # The emotion will display on showman window
	itype = db.Column(db.String(),nullable = False, default = 'emo') # emo = gif,img, info

	def __repr__(self):
		return f"GUI({self.id},{self.itype})"