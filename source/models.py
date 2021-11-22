from source import db 

class showman(db.Model):
	id = db.Column(db.Integer,primary_key = True) # the showman's id
	content = db.Column(db.String(),nullable = False, default = 'Good days') # The sentece will display on showman window
	emotion = db.Column(db.String(),nullable = False,default = 'happy') # The emotion will display on showman window
	itype = db.Column(db.String(),nullable = False, default = 'emo') # indicate which kinds of info will display on the showman screen

	def __repr__(self):
		return f"Showman({self.id},{self.itype})"