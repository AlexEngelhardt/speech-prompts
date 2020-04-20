import json
import datetime
import numpy as np

from flask import Flask, request
from flask_restful import Resource, Api

from webargs import fields, validate
from webargs.flaskparser import parser


# This is now the recommended way to parse GET arguments. flask_restful.reqparse
# is deprecated.
# https://webargs.readthedocs.io/en/latest/quickstart.html
get_lang_arg = {
    'lang': fields.Str(
        default="en",
        required=False,
        validate=validate.OneOf(['en', 'de', 'fr'])
    )
}

with open('questions/questions.json', 'r') as f:
    questions = json.load(f)

app = Flask('01-serve-question')
api = Api(app)


class RandomQuestion(Resource):
    def get(self):
        args = parser.parse(get_lang_arg, request)
        lang = args['lang']
        return questions[np.random.choice(questions.keys())][lang]


class TodaysQuestion(Resource):
    def get(self):
        args = parser.parse(get_lang_arg, request)
        lang = args['lang']
        mmdd = datetime.date.today().strftime("%m-%d")
        return questions[mmdd][lang]


api.add_resource(RandomQuestion, '/v2/questions/random')
api.add_resource(TodaysQuestion, '/v2/questions/today')

app.run(port='5002', debug=True)
