import prompts
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the index!'


@app.route('/v1/questions/random')
def random_question():
    lang = request.args.get('lang', default='en', type=str)
    return jsonify(prompts.get_random_question(lang=lang))


@app.route('/v1/questions/today')
def todays_question():
    lang = request.args.get('lang', default='en', type=str)
    return jsonify(prompts.get_todays_question(lang=lang))


app.run(port='5001', debug=True)
