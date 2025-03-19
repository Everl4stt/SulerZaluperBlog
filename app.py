from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Start page, Vovan dolzen sdelat'

@app.route('/index')
def about():
    return 'Main page, Vovan toze dolzen sdelat'

@app.route('/user/<username>')
def user_profile(username):
    return f"{username}'s page, Vovan poka chto ne sdelal"

if __name__ == '__main__':
    app.run(port=8080, debug=True)