from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
	"""Base data model for all objects"""
	__abstract__ = True

class Invitacion(BaseModel, db.Model):
	"""Model for invitacion table"""
	__tablename__ = 'invitacion'

	id = db.Column(
		db.Integer,
		primary_key = True,
		autoincrement = True
	)
	dt_invitation_date = db.Column(
		db.DateTime
	)
	dt_event_date = db.Column(
		db.DateTime
	)
	ds_host_email = db.Column(
		db.String(255)
	)
	ds_place = db.Column(
		db.String(2000)
	)

class DetalleInvitados(BaseModel, db.Model):
	__tablename__ = 'invitacion_invitados'
	id = db.Column(
		db.Integer,
		primary_key = True,
		autoincrement = True
	)
	invitacion_id = db.Column(
		db.Integer,
		db.ForeignKey("invitacion.id")
	)
	ds_email_invitado = db.Column(
		db.String(255)
	)
	ds_nombre_invitado = db.Column(
		db.String(255)
	)
	kn_event_response = db.Column(
		db.Integer
	)