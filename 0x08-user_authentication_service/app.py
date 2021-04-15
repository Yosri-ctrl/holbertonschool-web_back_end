#!/usr/bin/env python3
"""basic Flask app
"""


@app.route('/', methods=['GET'], strict_slashes=False)
def basic():
    """Return a simple dict message
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
