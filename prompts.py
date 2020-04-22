import json
import datetime
import numpy as np

with open('questions/questions.json', 'r') as f:
    questions = json.load(f)


def get_random_question(lang='en'):
    days = list(questions.keys())
    return questions[np.random.choice(days)][lang]


def get_todays_question(lang='en'):
    mmdd = datetime.date.today().strftime("%m-%d")
    return questions[mmdd][lang]