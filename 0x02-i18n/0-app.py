#!/usr/bin/env python3
"""setup a basic Flask app in 0-app.py"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('0-index.html', title=_('home_title'), header=_('home_header'))

if __name__ == '__main__':
    app.jinja_env.add_extension('jinja2.ext.i18n')
    app.run(debug=True)
