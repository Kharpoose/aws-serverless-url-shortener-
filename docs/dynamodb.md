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
