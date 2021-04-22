#!/usr/bin/env python3
"""task 3
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user():
    """get user function
    """
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """set get_user as a global on g.user
    """
    g.user = get_user()


@app.route('/')
def hello_world():
    """return the render of index page
    """
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """return the matched language
    """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run()
