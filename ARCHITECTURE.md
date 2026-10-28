# AWS Architecture

```text
Browser
  |
  v
Amazon S3 static website
  |
  v
Amazon API Gateway HTTP API
  | GET /inventory             | POST /orders
  v                            v
Lambda: list inventory    Lambda: create order
  |                            |
  v                            v
DynamoDB inventory       DynamoDB inventory + orders
                             (transactional stock deduction)

Lambda logs -> Amazon CloudWatch
```

Ensure the actual API stage URLs, CORS, table names, and Lambda permissions match the deployed AWS configuration.
