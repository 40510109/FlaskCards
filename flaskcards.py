from flask import Flask, render_template, url_for, flash, session, make_response, request
from random import randrange
from markupsafe import escape
import random
app =  Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200

@app.route("/language/<langid>/") #set game options template
def language(langid):
	return render_template('lang.html', languageid=langid), 200

@app.route("/language/<langid>/<category>/<diff>") #main
def egame(langid, category, diff):
	with open("static/langdata/" + langid + "/" + langid + category + ".txt") as file:
		dict = [line.rstrip() for line in file] #read file with language data into an array
	with open("static/langdata/english/english" + category + ".txt") as qfile:
		ENGLISH = [line.rstrip() for line in qfile] 
	rIndex=randrange(len(ENGLISH)) #generate random number from 1 to max number of lines in file so not to go out of bounds
	qCard=ENGLISH[rIndex]
	aCard=dict[rIndex]
	if diff == "2": #if difficulty is 2/easy generate 3 cards
	        rSample=random.sample(list(dict),2) #pick 2 random cards and assign to array
	        rSample.append(aCard) #append the correct card to the array
	        random.shuffle(rSample) #shuffle the array before passing to template
	        return render_template('egame.html', langid=langid, cat=category, qCard=qCard, aCard=aCard, rSample=rSample), 200
	elif diff == "5":
	        rSample=random.sample(list(dict),5)
	        rSample.append(aCard)
	        random.shuffle(rSample)
	        return render_template('mgame.html', langid=langid, cat=category, qCard=qCard, aCard=aCard, rSample=rSample), 200
	elif diff == "8":
                rSample=random.sample(list(dict),8)
                rSample.append(aCard)
                random.shuffle(rSample)
                return render_template('hgame.html', langid=langid, cat=category, qCard=qCard, aCard=aCard, rSample=rSample), 200
	#app.logger.info('\n debug \n rIndex=' + rIndex + '\n qCard=' + qCard + '\n aCard=' + aCard)  ##debugging

@app.errorhandler(404)
def not_found():
   	return make_response(render_template("404.html"), 404)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
