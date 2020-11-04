from flask import Flask, render_template
app =  Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200

@app.route("/language/<langid>/<mode>")
def language(langid, mode):
	return render_template('lang.html', languageid=langid, gamemode=mode), 200

@app.route("/test/<firstname>/<surname>")
def test(firstname, surname):
	return "Name:" + firstname + surname

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
