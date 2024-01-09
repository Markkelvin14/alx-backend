#!/usr/bin/env python3
"""Change your get_locale function to use a user’s preferred local if it is supported."""


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

def get_locale():
    # Check locale from URL parameters
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # Check user's preferred locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # Check locale from request header
    header_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    # Default to the app's default locale
    return app.config['BABEL_DEFAULT_LOCALE']

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
