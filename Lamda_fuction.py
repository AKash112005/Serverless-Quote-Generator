import json
import random

def lambda_handler(event, context):
    quotes = [
        "Success is built daily.",
        "Practice makes perfect.",
        "Keep learning AWS."
    ]
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'quote': random.choice(quotes)
        })
    }