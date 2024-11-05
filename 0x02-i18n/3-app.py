#!/usr/bin/env python3


"""task2"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)

# Set the default locale and timezone
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ['en', 'fr']

babel = Babel(app)

# Function to get the best language match
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

