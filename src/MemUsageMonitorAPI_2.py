#!/usr/bin/python3

import json
from flask import Flask, jsonify, request, Response
from flask_restplus import Api, Resource, fields
import MemUsageMonitor

flask_app = Flask(__name__)
api = Api(app = flask_app, version = '1.0', title = 'My mem API', description = 'Swagger for mem API')
name_space = api.namespace('api', description='Memory usage APIs')

mum = MemUsageMonitor.MemUsageMonitor()

# curl -d '{"threshold":40}' -H "Content-Type: application/json" -X POST http://<IP>:5000/api/memusage

@name_space.route('/help')
class HomeAPI(Resource):
    def get(self):
        helpMsg = { "/"                                      : "This help message",
                    "/memusage"                              : "Memory usage",
                    "/memusage POST data {'threshold' : 40}" : "Change mem usage threshold"
                   }
        return jsonify(helpMsg)

mem_threshold_model = api.model('Mem threshold Model', 
                                {'threshold': fields.Integer(required = True, 
                                                             description="Memory usage threshold", 
                                                             help="Name cannot be blank.")})

@name_space.route("/memusage")
class MemUsageAPI(Resource):
    def get(self):
        return jsonify(mum.getMemUsage())

    @api.doc(responses={ 200: 'OK', 400: 'Invalid mem usage threshold'}, params={})
    @api.expect(mem_threshold_model)
    def post(self):
        request_data = request.get_json()
        if 'threshold' in request_data:
            threshold = request_data['threshold']
            mum.setMemUsageThreshold(threshold)
            return Response("", 200, mimetype='application/json')
        else:
            invalidThresholdErrMsg = {
                "error" : "Invalid mem usage threshold",
                "helpString" : "Valid data should be like {'threshold' : 40}"
            }
            return Response(json.dumps(invalidThresholdErrMsg), status=400, mimetype='application/json')


# pip3 install flask
# pip3 install flask-restplus
# $ pip3 freeze | grep -i flask
# Flask==1.1.2
# flask-restplus==0.13.0
# flask-swagger==0.2.14
# $ pip3 freeze | grep -i werk
# Werkzeug==1.0.1
# pip3 uninstall Werkzeug
# pip3 install Werkzeug==0.16.1

if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0')

