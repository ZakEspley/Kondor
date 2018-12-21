# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, SmallInteger, String, Time
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.types import BIT
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Course(db.Model):
    __tablename__ = 'courses'

    idCourses = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    holeCount = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Numeric(2, 0))
    phone = db.Column(db.String(16))


class Hole(db.Model):
    __tablename__ = 'holes'

    idHoles = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.ForeignKey('courses.idCourses'), nullable=False, index=True)
    holeNumber = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=False)
    handicap = db.Column(db.Integer)
    blueLength = db.Column(db.SmallInteger, nullable=False)
    whitelength = db.Column(db.SmallInteger)
    blacklength = db.Column(db.SmallInteger)

    course1 = db.relationship('Course', primaryjoin='Hole.course == Course.idCourses', backref='holes')


class Pairing(db.Model):
    __tablename__ = 'pairings'

    idPairings = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.ForeignKey('rounds.idRounds'), nullable=False, index=True, server_default=db.FetchedValue())
    user = db.Column(db.ForeignKey('users.idUsers'), nullable=False, index=True, server_default=db.FetchedValue())

    round1 = db.relationship('Round', primaryjoin='Pairing.round == Round.idRounds', backref='pairings')
    user1 = db.relationship('User', primaryjoin='Pairing.user == User.idUsers', backref='pairings')


class Round(db.Model):
    __tablename__ = 'rounds'

    idRounds = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.ForeignKey('courses.idCourses'), nullable=False, index=True)
    date = db.Column(db.Date, nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)

    course1 = db.relationship('Course', primaryjoin='Round.course == Course.idCourses', backref='rounds')


class Score(db.Model):
    __tablename__ = 'scores'

    idScores = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.ForeignKey('rounds.idRounds'), nullable=False, index=True)
    hole = db.Column(db.ForeignKey('holes.idHoles'), nullable=False, index=True)
    user = db.Column(db.ForeignKey('users.idUsers'), nullable=False, index=True)
    score = db.Column(db.Integer, nullable=False)
    gir = db.Column(db.BIT(1), nullable=False)
    fir = db.Column(db.BIT(2), nullable=False)
    putts = db.Column(db.Integer, nullable=False)
    chips = db.Column(db.Integer, nullable=False)
    penaties = db.Column(db.Integer, nullable=False)
    gsbunker = db.Column(db.Integer, nullable=False)

    hole1 = db.relationship('Hole', primaryjoin='Score.hole == Hole.idHoles', backref='scores')
    round1 = db.relationship('Round', primaryjoin='Score.round == Round.idRounds', backref='scores')
    user1 = db.relationship('User', primaryjoin='Score.user == User.idUsers', backref='scores')


class User(db.Model):
    __tablename__ = 'users'

    idUsers = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
