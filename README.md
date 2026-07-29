# Bulk Notification API

A Django REST Framework API that allows creating a sender and multiple notifications in a single request.

The API validates all incoming data using Django REST Framework serializers and efficiently inserts notifications using Django's `bulk_create()`.

---

## Features

- Create a sender and multiple notifications in one API request
- Bulk insert notifications using `bulk_create()`
- Django REST Framework validation
- Atomic database transaction
- Clean JSON success and error responses

---

## Tech Stack

- Python 3.11+
- Django
- Django REST Framework
- SQLite (default)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/esther-malowa/bulk-notification-api.git
cd bulk-notification-api
```

### 2. Create a virtual environment

Windows

```bash
python -m venv env
env\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

The API will be available at

```
http://127.0.0.1:8000/api/notifications/bulk/
```

---

## API Endpoint

### POST

```
/api/notifications/bulk/
```

---

## Request Body

```json
{
  "name": "Edgar wafula",
  "email": "edgarwafula@gmail.com",
  "notifications": [
    {
      "title": "Welcome",
      "message": "Thank you for joining us.",
      "channel": "email"
    },
    {
      "title": "Reminder",
      "message": "Your appointment is tomorrow.",
      "channel": "sms"
    }
  ]
}
```

---

## Success Response

```json
{
  "message": "Sender and notifications created successfully.",
  "sender_id": 1,
  "notifications_created": 2
}
```

Status Code

```
201 Created
```

---

## Validation Errors

If validation fails, the API returns HTTP 400 with serializer errors.

Example:

```json
{
  "notifications": [
    {
      "channel": [
        "\"fax\" is not a valid choice."
      ]
    }
  ]
}
```

---
## Testing with cURL

```
curl -X POST [http://127.0.0.1:8000/api/notifications/bulk/](http://127.0.0.1:8000/api/notifications/bulk/) \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Edgar wafula",
    "email": "edgarwafula@gmail.com",
    "notifications": [
      {
        "title": "Welcome",
        "message": "Thank you for joining us.",
        "channel": "email"
      },
      {
        "title": "Reminder",
        "message": "Your appointment is tomorrow.",
        "channel": "sms"
      }
    ]
  }'
```


## Author

Esther Ooko
