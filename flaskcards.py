from flask import Flask, render_template, url_for, flash, session, make_response, request
from random import randrange
from markupsafe import escape
import random
app =  Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200

@app.route("/language/<langid>/")
def language(langid):
	return render_template('lang.html', languageid=langid), 200

@app.route("/language/<langid>/<category>/<diff>")
def egame(langid, category, diff):
	with open("static/langdata/" + langid + "/" + langid + category + ".txt") as file:
		dict = [line.rstrip() for line in file]
	with open("static/langdata/english/english" + category + ".txt") as qfile:
		ENGLISH = [line.rstrip() for line in qfile]
	rIndex=randrange(len(ENGLISH))
	qCard=ENGLISH[rIndex]
	aCard=dict[rIndex]
	if diff == "2":
	        rSample=random.sample(list(dict),2)
	        rSample.append(aCard)
	        random.shuffle(rSample)
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
        #app.logger.info('\n Logging Start \n random_index=' + random_index1 + '\n random_index2=' + random_index2)
	#app.logger.info('random_index:' + str(random_index))
	#app.logger.info('random_index1:' + str(random_index1))
	#app.logger.info('random_index2:' + str(random_index2))
	#app.logger.info('qCard:' + str(qCard))
	#app.logger.info('aCard:' + str(aCard))
	#app.logger.info('rSample:' + str(rSample))
	#app.logger.info('langid:'+ str(langid))
	#app.logger.info('eng len:' + str(len(ENGLISH)))
	#app.logger.info('ger len:' + str(len(GERMAN)))
	#app.logger.info('type: langid:' + str(type(langid)))

@app.route("/test/<firstname>/<surname>")
def test(firstname, surname):
	return "Name:" + firstname + surname

@app.errorhandler(404)
def not_found():
	return "Page not found"
#    return make_response(render_template("404.html"), 404)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
