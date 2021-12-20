from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.config['MONGO_URI']="mongodb://localhost/sustituir"
mongo=PyMongo(app)

@app.route('/', methods=['POST'])

def agregar_palabra():

	palabra = request.json['palabra']
	significado = request.json['significado']

	if palabra and significado:
		id=mongo.db.slangdic.insert(
				{'palabra':palabra, 'significado':significado}
			)
		response = {
			'id':str(id),
			'palabra':palabra,
			'significado':significado,
		}
		return response
	else:
		return not_found()

	return {'message':'received'}

@app.route("/",methods=['GET'])
def get_palabras():
	palabras = mongo.db.slangdic.find()
	response=json_util.dumps(palabras)
	return Response(response, mimetype='application/json')




@app.errorhandler(404)
def not_found(error=None):
	response = jsonify({
		'message': 'Resource Not Found: ' + request.url,
		'status': 404
	})
	return response





if __name__ == "__main__":
	app.run(port=5022,debug=True)