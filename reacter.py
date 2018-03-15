from flask import Flask, url_for, render_template, request, redirect
import requests

app = Flask(__name__)

URL = 'https://api.github.com/repos/{}/{}/issues/comments/{}/reactions'

@app.route('/')
def index(): 
    return render_template("reacter.html")

@app.route("/reacter/", methods=['POST'])
def url():
    owner = request.form['owner']
    repository_name = request.form['repository_name']
    id_num = request.form['id']
    url = URL.format(owner,repository_name,id_num)
    reaction = request.form['reaction']
    raise_for_status(url, reaction)
    return redirect(url_for("index"))
    


def get_session():
    with open('auth.cfg') as f:
        token = f.read().strip()
    headers = {'Authorization': 'token ' + token}
    session = requests.Session()
    session.headers.update(headers)
    return session

def raise_for_status(url, reaction):
    session = get_session()
    response = session.post(url,
    headers={'Accept': 'application/vnd.github.squirrel-girl-preview+jso'},
    json={'content': reaction})
