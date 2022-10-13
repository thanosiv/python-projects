from flask import Flask
from flask_restful import Resource, Api
import pandas as pd
import config

app = Flask(__name__)
api = Api(app)
path = config.path

class Users(Resource):
    def get(self):
        data = pd.read_csv(path + 'users.csv')
        data = data.to_dict(orient='records') # orient='records' required here to format as individual rows
        return {'data':data}, 200 # return the JSON and 200 status (OK)
    pass

class Locations(Resource):
    def get(self):
        data = pd.read_csv(path + 'locations.csv')
        data = data.to_dict(orient='records') # orient='records' required here to format as individual rows
        return {'data':data}, 200 # return the JSON and 200 status (OK)
    pass

api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    app.run()  # run Flask app
    
# JSON.parse($("pre").textContent)['data'][0]
# format to get individual records once app is running