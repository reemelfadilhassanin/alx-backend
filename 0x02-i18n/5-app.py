from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Set the default locale and timezone
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ['en', 'fr']

babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Function to get a user by ID
def get_user():
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id)

# before_request function to set g.user
@app.before_request
def before_request():
    g.user = get_user()

# Function to get the best language match
@babel.localeselector
def get_locale():
    # If the user is logged in, use their locale, otherwise fallback
    if g.user and g.user.get('locale'):
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
