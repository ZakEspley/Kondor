from flask import request
from flask_restful import Resource
from kondorapp.api.Model import db, Course, CourseSchema
from marshmallow import ValidationError


courses_schema = CourseSchema(many=True)
course_schema = CourseSchema()

class CourseResource(Resource):
    def get(self):
        courses = Course.query.all()
        courses = courses_schema.dump(courses).data
        return {"status": "success", "data":courses}, 200
    
    def post(self):
        try:
            course = course_schema.load(request.form, db.session)
            print(course.data)
            db.session.add(course.data)
            db.session.commit()
        except ValidationError:
            print(request)
            print("Validation Error")