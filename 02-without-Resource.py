import json
import datetime
import numpy as np

from flask import Flask, request

with open('questions/questions.json', 'r') as f:
    questions = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return('This is the index!')


@app.route('/v1/questions/random')
def random_question():
    lang = request.args.get('lang', default='en', type=str)
    days = list(questions.keys())
    return questions[np.random.choice(days)][lang]


@app.route('/v1/questions/today')
def todays_question():
    lang = request.args.get('lang', default='en', type=str)
    mmdd = datetime.date.today().strftime("%m-%d")
    return questions[mmdd][lang]


app.run(port='5002', debug=True)
