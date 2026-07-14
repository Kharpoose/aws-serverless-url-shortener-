# API Gateway

## API Type

```text
HTTP API
```

## Routes

| Method | Path | Integration |
|---------|------|-------------|
| POST | /shorten | create-short-url |
| GET | /{shortId} | redirect-url |

## Endpoint Example

```text
https://your-api-id.execute-api.ap-southeast-2.amazonaws.com
```

## Request Example

### Create Short URL

```http
POST /shorten
Content-Type: application/json
```

Request Body

```json
{
  "url": "https://www.google.com"
}
```

Response

```json
{
  "shortId": "Ab12Cd",
  "originalUrl": "https://www.google.com"
}
```

### Redirect

```http
GET /Ab12Cd
```

If the short ID exists, the API returns an HTTP **302 Redirect** response and automatically redirects the client to the original URL.
