# Reference example only; compare with your deployed Lambda before replacing it.
import json
import os
import boto3

table = boto3.resource("dynamodb").Table(
    os.environ.get("INVENTORY_TABLE", "fishstall-inventory-dev")
)

def lambda_handler(event, context):
    result = table.scan()
    items = result.get("Items", [])
    while "LastEvaluatedKey" in result:
        result = table.scan(ExclusiveStartKey=result["LastEvaluatedKey"])
        items.extend(result.get("Items", []))
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"message": "Inventory retrieved successfully", "items": items}, default=str)
    }
