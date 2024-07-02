#!/usr/bin/env python3
"""Flask-Bable app"""
# Aliasing render_template to renTemp
from flask import Flask, render_template as renTemp

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome() -> str:
    """Returns the greeting page"""
    return renTemp("0-index.html")


if __name__ == "__main__":
    app.run()
