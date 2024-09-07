#!/usr/bin/env python3
'''
    This script sets up a basic Flask application with internationalization
    support using Flask-Babel. It demonstrates how to use the `_()` function
    to parametrize templates and handle multiple languages based on the
    user's browser settings.

    Modules:
        - Flask: Web framework for building the application.
        - render_template: Function to render HTML templates.
        - request: Object to handle incoming request data.
        - Babel: Extension for adding i18n support to Flask.
        - _: Alias for gettext, used for marking strings for translation.

    Classes:
        - Config: class config for setting up languages, locale, and timezone.

    Functions:
        - get_locale: Determines the best match for the supported languages
        based on the request's `Accept-Language` header.
        - index: Renders the index.html template with localized content.
'''

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    '''Configuration class for Flask app.
        Attributes:
            LANGUAGES (list): List of supported languages.
            BABEL_DEFAULT_LOCALE (str): Default locale for the app.
            BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    '''Select the best match for the supported languages based on the request.
        Uses the `Accept-Language` header from the incoming request to find
        the best match for the supported languages defined in the Config class.
        Returns:
            str: The best-matching language code (e.g., 'en' or 'fr').
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''Render the homepage with localized content.

        Renders the '3-index.html' template and provides localized content for
        the title and header based on the selected language.

        Returns:
            str: Rendered HTML content for the homepage.
    '''
    return render_template('3-index.html',
                           home_title=_("home_title"),
                           home_header=_("home_header"))


if __name__ == '__main__':
    '''Start the application in debug mode for development and testing'''

    app.run(debug=True)
