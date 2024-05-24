#!/usr/bin/python3
""" Represeents the api's status."""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def status_return():
    """ Returns the status check"""
    return jsonify(status: "OK")

@app_views('/stat', strict_slashes=False)
def get_objects():
    """ Retrieves the number of each objects by type"""
    obj_types = {'state': State, 'user': User,
            'amenities': Amenity,'cities': City,
            'place': Place,'reviews': Review}
    for k in obj_types:
        obj_types[k] = storage.count(obj_types[k])
    return jsonify(obj_types)
