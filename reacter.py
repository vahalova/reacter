import requests


URL = 'https://api.github.com/repos/vahalova/flask-demo/issues/1'


def get_session():
    with open('auth.cfg') as f:
        token = f.read().strip()
    headers = {'Authorization': 'token ' + token}
    session = requests.Session()
    session.headers.update(headers)
    return session

def response_for_status():
    session = get_session()
    response = session.post(
    'https://api.github.com/repos/vahalova/flask-demo/issues/comments/371145341/reactions',
    headers={'Accept': 'application/vnd.github.squirrel-girl-preview+jso'},
    json={'content': '+1'})

response_for_status()
