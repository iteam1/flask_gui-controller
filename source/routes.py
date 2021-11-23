from source import app,db
from source.models import Showman 
from flask import render_template,request

@app.route('/',methods =['GET'])
def home():
	return render_template('helm.html')

@app.route('/content',methods =['GET','POST'])
def content():
	if request.method == 'POST':
		content = request.form.get('content')
		showman = Showman.query.get(1)
		showman.itype = 'info'
		showman.content = content
		db.session.commit()
		return render_template('helm.html')
	return render_template('helm.html')

@app.route('/emotion',methods =['GET','POST'])
def emotion():
	if request.method == 'POST':
		emotion = request.form.get('emotion')
		showman = Showman.query.get(1)
		showman.itype = 'emo'
		showman.emotion = emotion
		db.session.commit()
		return render_template('helm.html')
	return render_template('helm.html')

@app.route('/image',methods =['GET','POST'])
def image():
	if request.method == 'POST':
		image = request.form.get('image')
		showman = Showman.query.get(1)
		showman.itype = 'img'
		showman.image = image
		db.session.commit()
		return render_template('helm.html')
	return render_template('helm.html')

	