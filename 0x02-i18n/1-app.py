#!/usr/bin/env python3
"""instantiate the Babel object in your app."""


from flask_babel import Babel, _
babel = Babel(app)

class Config:
    """create a class config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
