---

https://hub.docker.com/r/swaggerapi/swagger-editor/

docker pull swaggerapi/swagger-editor
docker run -d -p 80:8080 swaggerapi/swagger-editor

You can now open swagger-editor on your machine via 80

---

https://hub.docker.com/r/swaggerapi/swagger-ui

docker pull swaggerapi/swagger-ui
docker run -d -p 80:8080 swaggerapi/swagger-ui

You can now open swagger-ui on your machine via 80

---

https://swagger.io/docs/open-source-tools/swagger-codegen/
https://github.com/swagger-api/swagger-codegen
https://hub.docker.com/r/swaggerapi/swagger-codegen-cli

docker pull swaggerapi/swagger-codegen-cli

usage: swagger-codegen-cli <command> [<args>]

The most commonly used swagger-codegen-cli commands are:
    config-help   Config help for chosen lang
    generate      Generate code with chosen lang
    help          Display help information
    langs         Shows available langs
    meta          MetaGenerator. Generator for creating a new template set and configuration for Codegen.  The output will be based on the language you specify, and includes default templates to include.
    validate      Validate specification
    version       Show version information

$ docker run swaggerapi/swagger-codegen-cli version
2.4.16
$ docker run swaggerapi/swagger-codegen-cli config-help -l python

CONFIG OPTIONS
	packageName
	    python package name (convention: snake_case). (Default: swagger_client)

	projectName
	    python project name in setup.py (e.g. petstore-api).

	packageVersion
	    python package version. (Default: 1.0.0)

	packageUrl
	    python package URL.

	sortParamsByRequiredFlag
	    Sort method arguments to place required parameters before optional parameters. (Default: true)

	hideGenerationTimestamp
	    Hides the generation timestamp when files are generated. (Default: true)

	library
	    library template (sub-template) to use (Default: urllib3)
$ docker run swaggerapi/swagger-codegen-cli config-help -l python-flask

CONFIG OPTIONS
	sortParamsByRequiredFlag
	    Sort method arguments to place required parameters before optional parameters. (Default: true)

	ensureUniqueParams
	    Whether to ensure parameter names are unique in an operation (rename parameters that are not). (Default: true)

	allowUnicodeIdentifiers
	    boolean, toggles whether unicode identifiers are allowed in names or not, default is false (Default: false)

	packageName
	    python package name (convention: snake_case). (Default: swagger_server)

	packageVersion
	    python package version. (Default: 1.0.0)

	controllerPackage
	    controller package (Default: controllers)

	defaultController
	    default controller (Default: default_controller)

	supportPython2
	    support python2 (Default: false)

	serverPort
	    TCP port to listen to in app.run (Default: 8080)



docker run -v ${PWD}/src:/swagger-api/out -v ${PWD}:/swagger-api/yaml swaggerapi/swagger-codegen-cli \
           -i /swagger-api/yaml/my_swagger.yaml -l python -o swagger-api/out/my_swagger


---

https://github.com/OpenAPITools/openapi-generator#16---docker

# From root directory of the project: input is swagger_2.json, output code to src/swagger_2 subdirectory
docker run -v ${PWD}/src:/swagger-api/out -v ${PWD}:/swagger-api/yaml openapitools/openapi-generator-cli generate \
           -i /swagger-api/yaml/swagger_2.json -g python -o swagger-api/out/swagger_2

swagger_2# python3 setup.py install --user

---
src/MemUsageMonitorAPI_1.py

https://pypi.org/project/flask-swagger/
https://github.com/gangverk/flask-swagger

A Swagger 2.0 spec extractor for Flask
pip install flask-swagger
Flask-swagger provides a method (swagger) that inspects the Flask app for endpoints that contain YAML docstrings
with Swagger 2.0 Operation objects.

---
src/MemUsageMonitorAPI_2.py

https://flask-restplus.readthedocs.io/
https://github.com/kb22/Understanding-Flask-and-Flask-RESTPlus

Flask-RESTPlus is an extension for Flask that adds support for quickly building REST APIs. Flask-RESTPlus encourages 
best practices with minimal setup. If you are familiar with Flask, Flask-RESTPlus should be easy to pick up. It
provides a coherent collection of decorators and tools to describe your API and expose its documentation properly
(using Swagger).


pip3 install flask-restplus

---
src/MemUsageMonitorAPI_3.py

https://pypi.org/project/flask-swagger-ui/
https://github.com/sveint/flask-swagger-ui

Simple Flask blueprint for adding Swagger UI to your flask application.
Included Swagger UI version: 3.36.0.

pip3 install flask-swagger-ui

SWAGGER_URL = '/api'
API_URL = '/static/swagger_3.json'

/static/swagger_3.json is a copy of swagger_1.json

---
src/MemUsageMonitorAPI_4.py

git clone https://github.com/swagger-api/swagger-ui.git

cp -r swagger-ui/dist/ swagger_examples/src
cp swagger_1.json src/dist/swagger_4.json
Change url in src/dist/index.html from "https://petstore.swagger.io/v2/swagger.json" to "./swagger_4.json"

===

src/MemUsageMonitorAPI_0.py
http://<server-ip>:5000/

src/MemUsageMonitorAPI_1.py
http://<server-ip>:5000/api
Swagger spec: http://<server-ip>:5000/spec
Swagger spec saved as swagger_1.json

src/MemUsageMonitorAPI_2.py
Swagger UI: http://<server-ip>:5000/
Swagger spec: http://<server-ip>:5000/swagger.json
Swagger spec saved as swagger_2.json

src/MemUsageMonitorAPI_3.py
Swagger UI: http://<server-ip>:5000/api

src/MemUsageMonitorAPI_4.py
Swagger UI: http://<server-ip>:5000/ui

