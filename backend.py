#! /usr/bin/env python
import pymongo

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__, template_folder='templates')
api = Api(app)

class Plants(Resource):
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['db']
        self.plants = self.db['plants']
        self.columns = ["country", "country_long", "name", "gppd_idnr", "capacity_mw"]

    def get(self):
        results = self.plants.find({}, {'_id': 0})
        results = list(map(dict, results))
        return results

api.add_resource(Plants, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)