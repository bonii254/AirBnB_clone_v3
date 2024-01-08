#!/usr/bin/python3
"""Index of views"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """Return the status of the api."""
    return jsonify({"status": "OK"}), 200
