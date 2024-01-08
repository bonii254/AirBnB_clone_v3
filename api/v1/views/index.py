#!/usr/bin/python3
"""Index of views"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """Return the status of the api."""
    return jsonify({"status": "OK"}), 200


@app_views.route('/stats', strict_slashes=False)
def stats():
    """endpoint that retrieves the number of each objects by type"""
    obj_counts = {}
    objects = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users",
    }

    for key, value in objects.items():
        obj_counts[value] = storage.count(key)
    return jsonify(obj_counts), 200
