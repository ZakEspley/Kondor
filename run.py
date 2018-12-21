from flask import Flask
from flask import json as json
from kondorapp.api.Model import db, User, Role, Course, Hole, Pairing
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_admin import helpers as admin_helpers
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from kondorapp.admin.ModelView import ProtectedAdminIndexView

# from werkzeug.config.fixers import ProxyFix


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from kondorapp.api.app import api_bp
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    
    db.init_app(app)

    from kondorapp.site.routes import site_app
    app.register_blueprint(site_app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    # from kondorapp.admin.app import admin, admin_app
    # app.register_blueprint(admin_app)

    admin = Admin(app, name="Kondor", template_mode='bootstrap3', index_view=ProtectedAdminIndexView())
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Course, db.session))
    admin.add_view(ModelView(Hole, db.session))
    admin.add_view(ModelView(Pairing, db.session))

    # @security.context_processor
    # def security_context_processor():
    #     return dict(
    #         admin_base_template=admin.base_template,
    #         admin_view=admin.index_view,
    #         h=admin_helpers,
    #     )

    return app

if __name__ == "__main__":
    app = create_app("config")
    # app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)
    mail = Mail(app)
    app.run(debug=True)