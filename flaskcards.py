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

@app.route("/game/<category>/easy")
def egame(category):
        random_index=randrange(len(ENGLISH))
        random_index1=randrange(len(GERMAN))
        random_index2=randrange(len(GERMAN))
        rand1=ENGLISH[random_index]
        rand2=GERMAN[random_index]
        rand3=random.sample(list(GERMAN),2)
        rand3.append(rand2)
        random.shuffle(rand3)
        return render_template('egame.html', cat=category, rand1=rand1, rand2=rand2, rand3=rand3), 200


@app.route("/game/<category>/med")
def mgame(category):
        #return "Output: " + category + cards
        return render_template('mgame.html', cat=category), 200

@app.route("/game/<category>/hard")
def hgame(category):
        #return "Output: " + category + cards
        return render_template('hgame.html', cat=category), 200

@app.route("/game/<category>/<cards>")
def zgame(category, cards):
	#return "Output: " + category + cards
	return render_template('game.html', cat=category, diff=cards), 200

@app.route("/test/<firstname>/<surname>")
def test(firstname, surname):
	return "Name:" + firstname + surname

@app.errorhandler(404)
def not_found():
	return "Page not found"
#    return make_response(render_template("404.html"), 404)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
