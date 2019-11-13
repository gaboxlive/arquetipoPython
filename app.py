#IMPORTAR LIBRERIAS
from flask import Flask, request, redirect
from models.models import db
from service.service import *
from flask_restful import Api, Resource
from flasgger import Swagger
from flasgger.utils import swag_from
from flask_restful_swagger import swagger
from routes.routes import Inicio
import config as CONF

app = Flask(__name__)
api = Api(app)
api = swagger.docs(
	Api(app),
	apiVersion = CONF.SWAGGER['apiVersion'],
	api_spec_url = CONF.SWAGGER['api_spec_url']
)

app.config['DEBUG'] = True
app.config[
	'SQLALCHEMY_DATABASE_URI'
] = '{}://{}:{}@{}:{}/{}'.format(
	CONF.MYSQL['driver'],
	CONF.MYSQL['user'],
	CONF.MYSQL['pw'],
	CONF.MYSQL['host'],
	CONF.MYSQL['port'],
	CONF.MYSQL['db']
) 
db.init_app(app)

#DECLARACION DE RUTAS
api.add_resource(
	Inicio,
	'/'
)

if __name__ == CONF.APPNAME:
	app.run(
		host = CONF.APP['host'],
		port = CONF.APP['port'],
		debug = CONF.APP['debug']
	)