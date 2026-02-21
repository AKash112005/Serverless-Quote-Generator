import json
import random

QUOTES = [
    {"quote": "Success is built daily.", "author": "Akash"},
    {"quote": "Practice makes perfect.", "author": "Unknown"},
    {"quote": "Keep learning AWS.", "author": "Cloud Engineer"},
    {"quote": "Consistency beats motivation.", "author": "Developer Mindset"}
]

def lambda_handler(event, context):
    try:
        selected = random.choice(QUOTES)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "GET"
            },
            "body": json.dumps({
                "success": True,
                "quote": selected["quote"],
                "author": selected["author"]
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }