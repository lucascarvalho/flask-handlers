# -*- coding: utf-8 -*-
from flask import jsonify
from werkzeug.exceptions import HTTPException, default_exceptions


# Method was copied and modified from:
# - http://flask.pocoo.org/snippets/83/
def set_json_error_handler(app):
    """
    Creates a JSON-oriented Flask app.

    All error responses that you don't specifically
    manage yourself will have application/json content
    type, and will contain JSON like this (just an example):

    { "message": "405: Method Not Allowed" }
    """
    def make_json_error(exception):
        if getattr(exception, 'description', None) is None:
            message = str(exception)
        else:
            message = exception.description
        response = jsonify({
            'id': exception.__class__.__name__.lower(),
            'message': message
        })
        response.status_code = (exception.code
                                if isinstance(exception, HTTPException)
                                else 500)
        response.headers = {'Content-Type': 'application/json'}
        return response

    for code in default_exceptions.iterkeys():
        app.register_error_handler(code, make_json_error)
