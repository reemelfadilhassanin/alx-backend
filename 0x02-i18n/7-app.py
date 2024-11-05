#!/usr/bin/env python3
"""task7"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError

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

# Function to validate the timezone
def get_timezone():
    # 1. Check for timezone parameter in the URL
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Validate if the timezone is a valid timezone
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            # If invalid, fallback to UTC
            return app.config['BABEL_DEFAULT_TIMEZONE']

    # 2. Check the user's timezone preference
    if g.user and g.user.get('timezone'):
        timezone = g.user['timezone']
        try:
            # Validate user timezone
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            # If user timezone is invalid, fallback to UTC
            return app.config['BABEL_DEFAULT_TIMEZONE']

    # 3. Default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']

# This function selects the best timezone
@babel.timezoneselector
def select_timezone():
    return get_timezone()

@app.route('/')
def index():
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
