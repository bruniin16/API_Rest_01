from flask import Flask
from flask_restful import Api, Resource
from resources.Employee import Employee


app = Flask(__name__)
api = Api(app)

api.add_resource(Employee, "/employee", endpoint="buscar", methods=["GET"])
api.add_resource(Employee, "/employee", endpoint="incluir", methods=["POST"])
api.add_resource(Employee, "/employee/<int:id>", endpoint="alterar", methods=["PUT"])
api.add_resource(Employee, "/employee/<int:id>", endpoint="deletar", methods=["DELETE"])

if __name__ == "__main__":
    app.run(debug=True)