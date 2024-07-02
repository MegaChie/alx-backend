#!/usr/bin/env python3
"""Flask-Bable app"""
from flask_babel import Babel
# Aliasing render_template to renTemp
from flask import Flask, render_template as renTemp


class Config:
    """Configeration class for babel to set language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def welcome() -> str:
    """Returns the greeting page"""
    return renTemp("1-index.html")


if __name__ == "__main__":
    app.run()