#!/usr/bin/env python3
"""Flask-Bable app"""
from flask_babel import Babel
# Aliasing render_template to renTemp
from flask import Flask, render_template as renTemp, g, request
from typing import Union, Dict


class Config:
    """Configeration class for babel to set language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


def get_user(login_as) -> Union[Dict, None]:
    """
    returns a user dictionary or
    None if the ID cannot be found or if login_as was not passed.
    """
    return None if login_as is None else users.get(int(login_as))


@app.before_request
def before_request() -> None:
    """
    Executed before all other functions and use get_user function to
    to find a user if any, and set it as a global on flask.g.user.
    """
    login_as = request.args.get('login_as', None)
    g.user = get_user(login_as)


@babel.localeselector
def get_locale() -> str:
    """Returns the page in the local language of the browser"""
    if 'locale' in request.args:
        if request.args['locale'] in app.config['LANGUAGES']:
            return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def welcome() -> str:
    """Returns the greeting page"""
    return renTemp("5-index.html")


if __name__ == "__main__":
    app.run()
