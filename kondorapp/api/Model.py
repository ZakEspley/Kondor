from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, SmallInteger, String, Time, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.types import BIT
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


db = SQLAlchemy()
ma = Marshmallow()

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.ForeignKey('roles.id'), nullable=False)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    confirmed_at = db.Column(db.DateTime())
    active = db.Column(db.Boolean())
    roles = db.relationship("Role", secondary='roles_users', backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    holeCount = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Numeric(2, 0))
    phone = db.Column(db.String(16))

    def __repr__(self):
        return self.name


class Hole(db.Model):
    __tablename__ = 'holes'

    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.ForeignKey('courses.id'), nullable=False, index=True)
    holeNumber = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=False)
    handicap = db.Column(db.Integer)
    blueLength = db.Column(db.SmallInteger, nullable=False)
    whitelength = db.Column(db.SmallInteger)
    blacklength = db.Column(db.SmallInteger)

    course1 = db.relationship('Course', primaryjoin='Hole.course == Course.id', backref='holes')


class Pairing(db.Model):
    __tablename__ = 'pairings'

    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.ForeignKey('rounds.id'), nullable=False, index=True, server_default=db.FetchedValue())
    user = db.Column(db.ForeignKey('users.id'), nullable=False, index=True, server_default=db.FetchedValue())

    round1 = db.relationship('Round', primaryjoin='Pairing.round == Round.id', backref='pairings')
    user1 = db.relationship('User', primaryjoin='Pairing.user == User.id', backref='pairings')


class Round(db.Model):
    __tablename__ = 'rounds'

    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.ForeignKey('courses.id'), nullable=False, index=True)
    date = db.Column(db.Date, nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)

    course1 = db.relationship('Course', primaryjoin='Round.course == Course.id', backref='rounds')


class Score(db.Model):
    __tablename__ = 'scores'

    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.ForeignKey('rounds.id'), nullable=False, index=True)
    hole = db.Column(db.ForeignKey('holes.id'), nullable=False, index=True)
    user = db.Column(db.ForeignKey('users.id'), nullable=False, index=True)
    score = db.Column(db.Integer, nullable=False)
    gir = db.Column(db.Boolean(1), nullable=False)
    fir = db.Column(db.Boolean(2), nullable=False)
    putts = db.Column(db.Integer, nullable=False)
    chips = db.Column(db.Integer, nullable=False)
    penaties = db.Column(db.Integer, nullable=False)
    gsbunker = db.Column(db.Integer, nullable=False)

    hole1 = db.relationship('Hole', primaryjoin='Score.hole == Hole.id', backref='scores')
    round1 = db.relationship('Round', primaryjoin='Score.round == Round.id', backref='scores')
    user1 = db.relationship('User', primaryjoin='Score.user == User.id', backref='scores')




##########################################################
##### This is the Marshmallow Schema Definitions.    #####
##########################################################
class CourseSchema(ma.ModelSchema):
    class Meta:
        model = Course


class HoleSchema(ma.ModelSchema):
    class Meta:
        model = Hole

  
class PairingSchema(ma.ModelSchema):
    class Meta:
        model = Pairing


class RoundSchema(ma.ModelSchema):
    class Meta:
        model = Round


class ScoreSchema(ma.ModelSchema):
    class Meta:
        model = Score


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

class RoleSchema(ma.ModelSchema):
    class Meta:
        model = Role

class RolesUsersSchema(ma.ModelSchema):
    class Meta:
        model = RolesUsers