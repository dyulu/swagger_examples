#!/usr/bin/python3

import json
from flask import Flask, jsonify, request, Response
from flask.views import MethodView
from flask_swagger import swagger
import MemUsageMonitor

app = Flask(__name__)

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Memory usage API"
    return jsonify(swag)

mum = MemUsageMonitor.MemUsageMonitor()

# curl -d '{"threshold":40}' -H "Content-Type: application/json" -X POST http://<IP>:5000/memusage

class HelpAPI(MethodView):
    def get(self):
        """
        Get the help message
        ---
        tags:
          - help
        responses:
          200:
            description: Return the help message
        """
        helpMsg = { "/"                                      : "This help message",
                    "/memusage"                              : "Memory usage",
                    "/memusage POST data {'threshold' : 40}" : "Change mem usage threshold"
                   }
        return jsonify(helpMsg)

help_view = HelpAPI.as_view('help')
app.add_url_rule('/', view_func = help_view, methods = ["GET"])

class MemUsageAPI(MethodView):
    def get(self):
        """
        Get the memory usage
        ---
        tags:
          - memusage
        responses:
          200:
            description: Return the memory usage info
        """
        return jsonify(mum.getMemUsage())

    def post(self):
        """
        Set memory usage threshold
        ---
        tags:
          - memusage
        definitions:
          - schema:
              id: MemThreshold
              required: threshold
              properties:
                threshold:
                  type: integer
                  description: memory usage threshold
                  example: 40
        parameters:
          - name: payload
            required: true
            in: body
            schema:
              $ref: "#/definitions/MemThreshold"
        responses:
          201:
            description: Threshold successfully set
          400:
            description: Invalid memory usage threshold input
        """
        request_data = request.get_json()
        if 'threshold' in request_data:
            threshold = request_data['threshold']
            mum.setMemUsageThreshold(threshold)
            return Response("", 201, mimetype='application/json')
        else:
            invalidThresholdErrMsg = {
                "error" : "Invalid mem usage threshold",
                "helpString" : "Valid data should be like {'threshold' : 40}"
            }
            return Response(json.dumps(invalidThresholdErrMsg), status=400, mimetype='application/json')

mem_view = MemUsageAPI.as_view('memusage')
app.add_url_rule('/memusage', view_func = mem_view, methods = ["GET"])
app.add_url_rule('/memusage', view_func = mem_view, methods = ["POST"])

# pip3 install flask
# pip install flask-swagger
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

