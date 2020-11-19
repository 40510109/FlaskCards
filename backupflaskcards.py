from flask import Flask, render_template, url_for, flash, session
from random import randrange
from markupsafe import escape
import random
app =  Flask(__name__)

#secret_key
app.secret_key = 'bZ_5#y2ddQ8sSs2z\n\c]/'


@app.route('/visits-counter/')
def visits():
    if 'user' in session:
        session['user'] = session.get('user')  # reading and updating session data
    else:
        session['user'] = 'marc' # setting session data
    return "Welcome back {}".format(session.get('user'))

@app.route('/delete-visits/')
def delete_visits():
    session.pop('user', None) # delete visits
    return 'Visits deleted'




@app.route('/')
def root():
	return render_template('home.html'), 200

@app.route("/language/<langid>/")
def language(langid):
	return render_template('lang.html', languageid=langid), 200

ENGLISH = ["hello", "car", "bus", "train", "school bus", "kid", "kids", "man", "woman"]
GERMAN = ["hallo", "das auto", "der bus", "der zug", "der schulbus", "das kind", "die kinder", "der mann", "die frau"]
FRENCH = ["bonjour", "le car", "le autobus", "le train", "bus scolaire", "des gamins", "homme", "femme"]
SPANISH = []

@app.route("/language/<langid>/<category>/<diff>")
def egame(langid, category, diff):
	with open("static/langdata/" + langid + "/" + langid + category + ".txt") as file:
		dict = [line.rstrip() for line in file]
	#if langid == 'german':
	#	dict = GERMAN
	#elif langid == 'french':
	#	dict = FRENCH
	random_index=randrange(len(ENGLISH))
	random_index1=randrange(len(dict))
	random_index2=randrange(len(dict))
	rand1=ENGLISH[random_index]
	rand2=dict[random_index]
	if diff == "2":
	        rand3=random.sample(list(dict),2)
	        rand3.append(rand2)
	        random.shuffle(rand3)
	        return render_template('egame.html', langid=langid, cat=category, rand1=rand1, rand2=rand2, rand3=rand3), 200
	elif diff == "5":
	        rand3=random.sample(list(dict),5)
	        rand3.append(rand2)
	        random.shuffle(rand3)
	        return render_template('mgame.html', langid=langid, cat=category, rand1=rand1, rand2=rand2, rand3=rand3), 200
	elif diff == "8":
                rand3=random.sample(list(dict),8)
                rand3.append(rand2)
                random.shuffle(rand3)
                return render_template('hgame.html', langid=langid, cat=category, rand1=rand1, rand2=rand2, rand3=rand3), 200
	#app.logger.info('random_index:' + str(random_index))
	#app.logger.info('random_index1:' + str(random_index1))
	#app.logger.info('random_index2:' + str(random_index2))
	#app.logger.info('rand1:' + str(rand1))
	#app.logger.info('rand2:' + str(rand2))
	#app.logger.info('rand3:' + str(rand3))
	#app.logger.info('langid:'+ str(langid))
	#app.logger.info('eng len:' + str(len(ENGLISH)))
	#app.logger.info('ger len:' + str(len(GERMAN)))
	#app.logger.info('type: langid:' + str(type(langid)))

@app.route("/labs/")
def filetest():
	my_file = open("static/langdata/germantest.txt", "r")
	content_list = my_file.readlines()
	return str(content_list)


@app.route("/test/<firstname>/<surname>")
def test(firstname, surname):
	return "Name:" + firstname + surname

@app.errorhandler(404)
def not_found():
	return "Page not found"
#    return make_response(render_template("404.html"), 404)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
