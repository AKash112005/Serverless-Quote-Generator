import json
import random

# Sample data (can later move to DynamoDB)
QUOTES = [
    {"quote": "Success is built daily.", "author": "Akash"},
    {"quote": "Practice makes perfect.", "author": "Unknown"},
    {"quote": "Keep learning AWS.", "author": "Cloud Engineer"},
    {"quote": "Consistency beats motivation.", "author": "Developer Mindset"}
]

def lambda_handler(event, context):
    try:
        # Allow only GET requests
        method = event.get("requestContext", {}).get("http", {}).get("method", "")
        
        if method and method != "GET":
            return response(405, {"message": "Method Not Allowed"})

        selected = random.choice(QUOTES)

        return response(200, {
            "success": True,
            "data": selected,
            "message": "Quote fetched successfully"
        })

    except Exception as e:
        return response(500, {
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        })


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "GET"
        },
        "body": json.dumps(body)
    }