#!/usr/bin/env python3
'''2. Get locale from request'''

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    ''''
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


@babel.localeselector
def get_locale():
    '''
    Select the best match for supported languages based on the request.

    This function uses the request's Accept-Language headers to determine the
    best match for the supported languages defined in the Config class.

    Returns:
        str: The best-matching language code (e.g., 'en' or 'fr').
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''
    Route for the homepage.
    This function handles requests to the root URL ('/') and returns the
    rendered '2-index.html' template.

    Returns:
        str: Rendered HTML content for the homepage.
    '''
    return render_template('2-index.html')


if __name__ == '__main__':

    app.run(debug=True)
