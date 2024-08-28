#!/usr/bin/env python3
'''Basic Babel setup'''
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    '''
    Configuration class for Flask app.
    Attributes:
        LANGUAGES (list): The list of supported languages.
        BABEL_DEFAULT_LOCALE (str): The default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone for the app.
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    '''
    Route for the homepage.
    This function handles requests to the root URL ('/') and returns the
    rendered '1-index.html' template.
    Returns:
        str: Rendered HTML content for the homepage.
    '''
    return render_template('1-index.html')


if __name__ == '__main__':

    app.run(debug=True)
