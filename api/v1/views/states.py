#!/usr/bin/python3
""" handles all default RestFul API actions for State objects """
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """
    Gets all State objects
    """
    states = storage.all(State).values()
    state_list = []
    for state in states:
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ Getsa specific  State """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """
    Deletes State Object
    """

    state = storage.get(State, state_id)

    if not state:
        abort(404)

    storage.delete(state)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """
        Creates a State object
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    req_state = request.get_json()
    state_obj = State(**req_state)
    state_obj.save()
    return make_response(jsonify(state_obj.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """
      Updates a State object
    """
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    req = request.get_json()
    ignored_items= ['id', 'created_at', 'updated_at']
    for key, value in req.items():
        if key not in ignored_items:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
