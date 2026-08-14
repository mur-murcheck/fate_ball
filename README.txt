Project name: FATE BALL

Description: A funny and mysterious game where the user asks a question and then receives a prophecy wrapped in an enigma and spiced with a joke.

Example question: Does he truly love me?
Request:
{
    "question": "Does he truly love me?"
}

Response:
{
    "prophecy": "Unclear. The spirits are arguing over who forgot to charge the crystal ball."
}

Validation rules:
1. The question must not be empty
2. The question value must be a string
3. The question must not contain more than 512 characters

Additional requirements:
1. The user can ask using any language

API contract:
Method: POST
Path: /api/prophecy
Content-Type: application/json
Success status: 200 OK
Validation error status: 422 Unprocessable Content

Request:
{
    "question": ""
}
Response:
{
    "status-code": 422,
    "message": "The question must not be empty."
}

Request:
{
    "question": 42
}
Response:
{
    "status-code": 422,
    "message": "The question value must be a string."
}

Request:
{
    "question": "<a string containing 513 characters>"
}
Response:
{
    "status-code": 422,
    "message": "The question must not contain more than 512 characters"
}