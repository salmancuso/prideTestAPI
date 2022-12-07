from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


class participants(Resource):
    def get(self):
        data = pd.read_csv('participants.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code
        
api.add_resource(participants, '/participants')  # '/users' is our entry point for Users


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # run our Flask app on port 8000