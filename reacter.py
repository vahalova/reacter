from flask import Flask, url_for, render_template, request, redirect

import requests
app = Flask(__name__)

URL = 'https://api.github.com/repos/{}/{}/issues/comments/{}/reactions'

@app.template_filter("cap")
def capitalize(word):
    return word[0].upper() + word[1:]

@app.route('/')
def index(): #pohledová funkce
    return render_template("reacter.html")

@app.route("/hello/")
@app.route("/hello/<name>/<int:count>/")
def hello(name=None,count=1):
    return render_template("reacter.html", name=name)

@app.route("/reacter/", methods=['POST'])
def url():
    owner = request.form['owner']
    repository_name = request.form['repository_name']
    id_num = request.form['id']
    url = URL.format(owner,repository_name,id_num)
    response_for_status(url)
    return redirect(url_for("index"))
    


def get_session():
    with open('auth.cfg') as f:
        token = f.read().strip()
    headers = {'Authorization': 'token ' + token}
    session = requests.Session()
    session.headers.update(headers)
    return session

def response_for_status(url):
    session = get_session()
    response = session.post(url,
    headers={'Accept': 'application/vnd.github.squirrel-girl-preview+jso'},
    json={'content': 'hooray'})
