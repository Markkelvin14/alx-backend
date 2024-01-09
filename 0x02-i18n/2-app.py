#!/usr/bin/env python3
"""Create a get_locale function with the babel.localeselector decorator"""


from flask import Flask, render_template, request

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
