#!/usr/bin/env python3
"""Define a get_timezone function and use the babel.timezoneselector decorator"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    return users.get(user_id)

def validate_timezone(timezone):
    try:
        import pytz
        pytz.timezone(timezone)
        return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return None

def get_timezone():
    # Check timezone from URL parameters
    url_timezone = request.args.get('timezone')
    if url_timezone and validate_timezone(url_timezone):
        return url_timezone

    # Check user's preferred timezone
    if g.user and g.user.get('timezone') and validate_timezone(g.user.get('timezone')):
        return g.user.get('timezone')

    # Default to UTC
    return 'UTC'

@babel.timezoneselector
def get_timezone():
    return get_timezone()

@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.jinja_env.add_extension('jinja2.ext.i18n')
    app.run(debug=True)
