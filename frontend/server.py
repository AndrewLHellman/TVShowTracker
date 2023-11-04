# Aided by https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3#step-3-using-html-templates

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tvshows")
def tvshows():
    return render_template("tvshows.html")

@app.route("/movies")
def movies():
    return render_template("movies.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
