import json
import datetime
import numpy as np

from flask import Flask
from flask_restful import Resource, Api

with open('questions/questions.json', 'r') as f:
    questions = json.load(f)

app = Flask('01-random-question')
api = Api(app)


class RandomQuestion(Resource):
    def get(self, lang="en"):
        return questions[np.random.choice(questions.keys())][lang]


class TodaysQuestion(Resource):
    def get(self, lang="en"):
        mmdd = datetime.date.today().strftime("%m-%d")
        return questions[mmdd][lang]


api.add_resource(RandomQuestion, '/v1/questions/random')
api.add_resource(TodaysQuestion, '/v1/questions/today')

app.run(port='5001')
