import json
import boto3
import random
import string
from datetime import datetime, timezone
import os

dynamodb = boto3.resource("dynamodb")
table_name = os.environ["TABLE_NAME"]
table = dynamodb.Table(table_name)


def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def lambda_handler(event, context):

    original_url = event.get("url")

    if not original_url:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "url is required"
            })
        }

    short_id = generate_short_id()

    try:
        table.put_item(
            Item={
                "shortId": short_id,
                "originalUrl": original_url,
                "createdAt": datetime.now(timezone.utc).isoformat()
            }
        )
    except Exception as e:
    print(f"Error saving item to DynamoDB: {e}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Failed to save URL"
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "shortId": short_id,
            "originalUrl": original_url
        })
    }
