from flask import Blueprint, make_response
from flask_restful import Api
from flask import json
from .resources.Course import CourseResource
from .resources.User import UserResource, UserList

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
########################################################################
## This uses the Flask Json encoder rather than the default Python One.
## It has a few fancier nuts and bolts. It particularly lets us decode
## decimals.
@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp
########################################################################
api.add_resource(CourseResource, "/Courses")
api.add_resource(UserList, "/Users")
api.add_resource(UserResource, "/Users/id/<string:userID>")