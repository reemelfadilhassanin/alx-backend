#!/usr/bin/env python3
"""task6"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Set the default locale and timezone
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ['en', 'fr']

# Mock users table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

babel = Babel(app)

# Function to get the user from the URL parameter (login_as)
def get_user():
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None

# This function is called before every request
@app.before_request
def before_request():
    user = get_user()
    g.user = user

# Function to get the best language match
@babel.localeselector
def get_locale():
    # 1. Check for locale parameter in the URL
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Check if the user has a preferred locale
    if g.user and g.user.get('locale') and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Check the Accept-Language header
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']

@app.route('/')
def index():
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
