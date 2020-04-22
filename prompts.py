import json
import datetime
import random

with open('questions/questions.json', 'r') as f:
    questions = json.load(f)


def get_random_question(lang='en'):
    days = list(questions.keys())
    i = random.randrange(0, len(days))  # do without np.random so that AWS Lambda doesn't need numpy
    key = list(questions)[i]
    return questions[key][lang]


def get_todays_question(lang='en'):
    mmdd = datetime.date.today().strftime("%m-%d")
    return questions[mmdd][lang]