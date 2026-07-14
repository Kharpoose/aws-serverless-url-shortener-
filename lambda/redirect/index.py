import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")
table_name = os.environ["TABLE_NAME"]
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    try:
        short_id = event["pathParameters"]["shortId"]
    except (KeyError, TypeError):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "shortId is required"})
        }


    try:
        response = table.get_item(
            Key={
                "shortId": short_id
            }
        )

    except Exception as e:
        print(f"Error reading DynamoDB: {e}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal Server Error"
            })
        }

    item = response.get("Item")

    if not item:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "Short URL not found"
            })
        }

    return {
        "statusCode": 302,
        "headers": {
            "Location": item["originalUrl"]
        }
    }
