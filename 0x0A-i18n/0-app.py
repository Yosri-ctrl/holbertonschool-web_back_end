#!/usr/bin/env python3
"""task 0
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    """return page containig header
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
