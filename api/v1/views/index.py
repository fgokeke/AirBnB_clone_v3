#!/usr/bin/python3
"""
This module defines view functions related to the index of the API.
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
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
