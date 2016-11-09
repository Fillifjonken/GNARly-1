import webapp2

from flask import Flask, render_template
from google.appengine.api import users

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))

@app.route('/')
@app.route('/index/')
def index():
    """Return a friendly HTTP greeting."""
    return render_template('index1.html')

@app.route('/profile/')
def profile():
    profile = None
    return render_template('profile.html', profile=profile)

@app.route('/competition/')
def competition():
    return render_template('comp.html')

@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/leaderboard/')
def leaderboard():
    return render_template('leaderboard.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
