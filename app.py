from flask import Flask, redirect, url_for, render_template, request
import feedparser
app = Flask(__name__)

@app.route("/")
def home():
    url = "http://feeds.bbci.co.uk/mundo/rss.xml"
    feed = feedparser.parse(url)
    noticias = feed.entries[:5]
    return render_template("index.html", noticias=noticias)

@app.route("/login", methods=['GET','POST'])

def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return redirect(url_for("user", user=nombre))
    else:
        return render_template("login.html")
    
@app.route("/<user>")
def user(user):
    return f"<h1>{user}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
