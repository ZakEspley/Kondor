from flask import Blueprint
from flask_security import login_required
from flask_admin import Admin
from flask_admin import helpers as admin_helpers
from flask_admin.contrib.sqla import ModelView
from kondorapp.api.Model import User, Course, Hole, Pairing, db

admin_app = Blueprint("admin", __name__)


admin = Admin(admin_app, name="Kondor", template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Course, db.session))
admin.add_view(ModelView(Hole, db.session))
admin.add_view(ModelView(Pairing, db.session))

