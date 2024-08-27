#!/usr/bin/env python3
'''This function handles requests to the root URL ('/') and returns the
    rendered 'index.html' template.'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    '''
    Route for the homepage.
    Returns:
        str: Rendered HTML content for the homepage.
    '''
    return render_template('0-index.html')


if __name__ == '__main__':

    app.run(debug=True)
