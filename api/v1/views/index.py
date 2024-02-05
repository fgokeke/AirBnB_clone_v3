#!/usr/bin/python3
"""
This module defines view functions related to the index of the API.
"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


hbnb_dict = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def status():
    """
    Return the status of the API.

    This endpoint provides a simple way to verify that the API
    service is operational.
    When accessed via a GET request,
    it returns a JSON response indicating that the API status is "OK".

    Returns:
        A JSON object with a key 'status' and value 'OK'.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Retrieve the number of each object by type"""
    return_dict = {}
    for key, value in hbnb_dict.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)


if __name__ == "__main__":
    pass
