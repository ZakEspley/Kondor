from flask import request
from flask_restful import Resource
from kondorapp.api.Model import db, User, UserSchema

users_schema = UserSchema(many=True)
user_schema = UserSchema()

class UserResource(Resource):
    def get(self, userID):
        user = User.query.get(userID)
        user = user_schema.dump(user).data
        return {"status": "success", "data":user}, 200

class UserList(Resource):
    def get(self):
        users = User.query.all()
        users = users_schema.dump(users).data
        return {"status": "success", "data":users}, 200