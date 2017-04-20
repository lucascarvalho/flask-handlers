# -*- coding: utf-8 -*-
from flask import Flask, abort, json
from flask_handlers import set_json_error_handler

app = Flask(__name__)
set_json_error_handler(app)


@app.route('/', methods=['GET'])
def index():
    return abort(400, 'Invalid request.')


def test_error_handler():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 400
    assert response.content_type == 'application/json'
    assert json.loads(response.data) == {
        'message': 'Invalid request.',
        'id': u'badrequest'
    }
