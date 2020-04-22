import json
import prompts


def random_question_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(prompts.get_random_question())
    }


def todays_question_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(prompts.get_todays_question())
    }