#!/usr/bin/python3

import json
from flask import Flask, jsonify, request, Response
from flask_swagger_ui import get_swaggerui_blueprint
import MemUsageMonitor

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/api'
API_URL = '/static/swagger_3.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,   # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={
        'app_name': "Memory usage API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


mum = MemUsageMonitor.MemUsageMonitor()

# curl -d '{"threshold":40}' -H "Content-Type: application/json" -X POST http://<IP>:5000/memusage

@app.route('/')
def index():
    helpMsg = { "/"                                      : "This help message",
                "/memusage"                              : "Memory usage",
                "/memusage POST data {'threshold' : 40}" : "Change mem usage threshold"
               }
    return jsonify(helpMsg)

@app.route('/memusage', methods=['GET'])
def memusage():
    return jsonify(mum.getMemUsage())

@app.route('/memusage', methods=['POST'])
def setMemUsageThreshold():
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

# pip3 install python
# pip3 install flask_swagger_ui
# $ pip3 freeze | grep -i flask-swagger-ui
# flask-swagger-ui==3.36.0

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
