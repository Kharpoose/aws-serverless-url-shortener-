# AWS Serverless URL Shortener

A simple serverless URL shortener built with **AWS Lambda**, **API Gateway**, and **Amazon DynamoDB**.

This project demonstrates how to build a fully serverless REST API using AWS services. Users can submit a long URL, receive a generated short ID, and access the original URL through an HTTP redirect.

---

# Architecture

```text
                    Client
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
 POST /shorten                 GET /{shortId}
        │                             │
        └──────────────┬──────────────┘
                       ▼
                Amazon API Gateway
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
create-short-url              redirect-url
     Lambda                       Lambda
        │                             │
        └──────────────┬──────────────┘
                       ▼
                Amazon DynamoDB
```

---

# AWS Services

- AWS Lambda
- Amazon API Gateway (HTTP API)
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

---

# Features

- Create shortened URLs
- Redirect to the original URL using HTTP 302
- Fully serverless architecture
- Store URL mappings in DynamoDB
- Environment Variables for configuration
- Error handling
- CloudWatch logging

---

# Project Structure

```text
aws-serverless-url-shortener/
│
├── create-short-url/
│   └── lambda_function.py
│
├── redirect-url/
│   └── lambda_function.py
│
└── README.md
```

---

# DynamoDB

## Table Configuration

**Table Name**

```text
url-shortener
```

**Partition Key**

```text
shortId (String)
```

**Billing Mode**

```text
On-demand
```

## Item Example

```json
{
  "shortId": "Ab12Cd",
  "originalUrl": "https://www.google.com",
  "createdAt": "2026-07-07T10:20:30Z"
}
```

---

# API Gateway

## API Type

```text
HTTP API
```

## Routes

| Method | Path | Lambda |
|---------|------|--------|
| POST | /shorten | create-short-url |
| GET | /{shortId} | redirect-url |

---

# API Examples

## Create Short URL

### Request

```http
POST /shorten
Content-Type: application/json
```

```json
{
  "url": "https://www.google.com"
}
```

### Response

```json
{
  "shortId": "Ab12Cd",
  "originalUrl": "https://www.google.com"
}
```

---

## Redirect

### Request

```http
GET /Ab12Cd
```

### Response

If the short ID exists, the API returns an **HTTP 302 Redirect** response and redirects the client to the original URL.

---

# Lambda Functions

## create-short-url

Responsibilities:

- Parse the incoming request body
- Generate a random short ID
- Store the URL in DynamoDB
- Return the generated short ID

---

## redirect-url

Responsibilities:

- Receive the short ID from the URL path
- Retrieve the original URL from DynamoDB
- Return an HTTP 302 redirect response
- Return HTTP 404 if the short ID does not exist

---

# Environment Variables

Both Lambda functions require the following environment variable:

| Name | Value |
|------|-------|
| TABLE_NAME | url-shortener |

---

# Example Workflow

```text
1. Client sends POST /shorten
                │
                ▼
      API Gateway
                │
                ▼
      create-short-url Lambda
                │
                ▼
          DynamoDB
                │
                ▼
      Returns shortId

-----------------------------------------

2. Client requests /Ab12Cd
                │
                ▼
        API Gateway
                │
                ▼
       redirect-url Lambda
                │
                ▼
         DynamoDB lookup
                │
                ▼
        HTTP 302 Redirect
                │
                ▼
        Original Website
```

---

# Future Improvements

- Return the complete shortened URL instead of only the short ID.
- Prevent duplicate shortened URLs for the same original URL.
- Add click statistics.
- Add URL expiration using DynamoDB TTL.
- Deploy the infrastructure using AWS SAM or Terraform.
- Add automated tests.

---

# Learning Objectives

This project demonstrates:

- Serverless application development
- REST API design
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- IAM permissions
- CloudWatch logging
- HTTP redirects
- Environment Variables
- Python with boto3
