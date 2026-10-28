# ThoorigAI Fish Stall Order and Stock Tracker

AWS serverless demo project for fish inventory and order submission.

## AWS services
- Amazon S3: static website hosting
- Amazon API Gateway: HTTP API routes
- AWS Lambda: inventory retrieval and order creation
- Amazon DynamoDB: inventory and order data
- Amazon CloudWatch: logs and troubleshooting

## Structure
- `website/index.html` — website front end
- `lambda/list_inventory/lambda_function.py` — example inventory Lambda
- `lambda/create_order/lambda_function.py` — reference order Lambda
- `docs/ARCHITECTURE.md` — architecture overview

## Demo endpoints
- Inventory: `https://chtcaprz5c.execute-api.ap-south-1.amazonaws.com/inventory`
- Order: `https://chtcaprz5c.execute-api.ap-south-1.amazonaws.com/dev/orders`

Confirm these URLs/stages in API Gateway before presenting. These values reflect the demo setup at the time this README was prepared.

## Important
The Lambda files in this repository are reference examples, not a verified export of the deployed AWS code. The deployed order function was tested successfully and used a DynamoDB transaction to create an order and deduct stock atomically. Download the exact deployed code from AWS Lambda and compare it before replacing or redeploying anything.

## Setup summary
1. DynamoDB tables: `fishstall-inventory-dev` (partition key `itemId`) and `fishstall-orders-dev` (partition key `orderId`).
2. Configure Lambda execution roles with least-privilege DynamoDB permissions.
3. Configure API Gateway routes `GET /inventory` and `POST /orders`.
4. Configure CORS for the website's origin.
5. Upload `website/index.html` as `index.html` to the S3 website bucket.
6. Test inventory and one order, then verify both DynamoDB tables.

## Security
- Never upload AWS access keys, secret keys, passwords, `.env` files, or session tokens.
- Do not upload real customer contact details or production order exports.
- Public repositories are visible to everyone.
- S3 website endpoints use HTTP; CloudFront can provide HTTPS.

## Verified demo results
- Website inventory loaded from API Gateway.
- An order was successfully submitted.
- The order appeared in `fishstall-orders-dev`.
- Prawn stock decreased from 12 kg to 11 kg after a 1 kg test order.
