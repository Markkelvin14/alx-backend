#!/usr/bin/env python3
"""detect if the incoming request contains locale argument and ifs value is a supported locale, return it"""
from flask_babel import Babel, _
babel = Babel(app)


@babel.localeselector
def get_locale():
    forced_locale = request.args.get('locale')
    if forced_locale and forced_locale in app.config['LANGUAGES']:
        return forced_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
