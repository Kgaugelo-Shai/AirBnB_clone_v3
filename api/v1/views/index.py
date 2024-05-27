#!/usr/bin/python3
""" gets the status """

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    return jsonify(status="OK")


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """
    endpoint that retrieves the number of each objects by type
    """
    cls_objs = {
        "users": storage.count("User"),
        "states": storage.count("State"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "amenities": storage.count("Amenity"),
        "reviews": storage.count("Review"),
    }
    counter = jsonify(cls_objs)
    counter.status_code = 200
    return counter
