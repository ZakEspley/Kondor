from flask import Blueprint, render_template
from flask_security import login_required
from kondorapp.api.Model import User, Course, Hole, db

site_app = Blueprint('site', __name__, template_folder="templates")



@site_app.route("/")
def homepage():
    return "<h1>This is a test of the homepage</h1>"
@login_required
@site_app.route("/user/<int:id>")
def userpage(id):
    user = User.query.get(id)
    print(user)
    return render_template("site/profile.html", user=user)

@login_required
@site_app.route("/round")
def roundpage():
    course = Course.query.get(1)
    holes = Hole.query.filter(Hole.course == course.id)
    print(holes)
    return render_template("site/round.html", course=course, holes=holes)