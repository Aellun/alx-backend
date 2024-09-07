#!/usr/bin/env python3
'''
This script sets up a basic Flask application with internationalization
support using Flask-Babel.
'''
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    '''
    Babel Configuration
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    '''
    Returns a user dictionary or None if ID value is not found
    or if 'login_as' URL parameter was not found.
    '''
    id = request.args.get('login_as')
    try:
        id = int(id)
    except (TypeError, ValueError):
        return None
    return users.get(id)


@app.before_request
def before_request():
    '''
    Add user to Flask's g object before each request
    '''
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    '''
    Select and return language match based on supported languages
    '''
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    '''
    route handler
    '''
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
