# Fate Ball

Fate Ball is a playful web game where users ask a question and receive a random prophecy wrapped in mystery and seasoned with a joke. The animated cosmic orb delivers answers through a small Flask JSON API and an interactive
browser interface.

## Features

- Random, humorous prophecies in English
- Interactive cosmic orb with loading and reveal animations
- Responsive layout for desktop and mobile screens
- Accessible live regions for prophecies and errors
- Reduced-motion support based on the user's system preference
- Server-side validation for request format, question type, content, and length
- Friendly handling of HTTP and connection errors
- Health-check endpoint
- Automated tests for the web page and API contract
- Optional console version of the game

## Tech Stack

- Python 3.12
- Flask 3
- HTML5
- CSS3
- JavaScript
- Pytest
- Postman for manual API testing

## Project Structure

```text
fate_ball/
├── app.py                 # Flask application and API routes
├── ball_body.py           # Prophecy collection and random selection logic
├── requirements.txt       # Reproducible Python dependencies
├── static/
│   ├── app.js             # Browser interaction and API requests
│   └── styles.css         # Responsive cosmic-orb design and animations
├── templates/
│   └── index.html         # Main game page
└── tests/
    └── test_app.py        # Flask route and validation tests
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mur-murcheck/fate_ball.git
cd fate_ball
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Start the development server

```bash
python -m flask --app app run --debug --port 5001
```

Open [http://127.0.0.1:5001](http://127.0.0.1:5001) in a browser.

The Flask development server is intended for local development only. Do not
use debug mode in production.

## How to Play

1. Enter a question in the text area.
2. Select **Ask the Orb**.
3. Wait while the cosmic sphere consults the stars.
4. Read the prophecy revealed inside the orb.
5. Ask again whenever destiny seems suspiciously vague.

Questions may use any language, must contain text, and may not exceed 512
characters.

## API

### Create a prediction

```http
POST /api/predictions
Content-Type: application/json
```

Request body:

```json
{
  "question": "Will I become a great developer?"
}
```

Successful response — `200 OK`:

```json
{
  "prophecy": "The stars predict success, followed by one extremely educational mistake."
}
```

Validation error — `422 Unprocessable Content`:

```json
{
  "message": "The question must not be empty."
}
```

Request-format errors return `400 Bad Request`. Examples include a non-JSON
body or a JSON value that is not an object.

### Health check

```http
GET /api/health
```

Successful response — `200 OK`:

```json
{
  "status": "ok"
}
```

## Validation Rules

The prediction endpoint requires:

1. A request with `Content-Type: application/json`.
2. A JSON object containing the `question` field.
3. A question whose value is a string.
4. A question that is not empty or made only of whitespace.
5. A question no longer than 512 characters.

## Running Tests

Run the complete test suite from the project root:

```bash
python -m pytest
```

The tests cover the main page, health check, successful predictions, request
format errors, validation errors, and both sides of the 512-character boundary.

## Console Version

The original console version is still available:

```bash
python ball_body.py
```

Enter a question in the terminal to receive a random prophecy.

## Future Improvements

- Add weighted prophecy categories and rare responses
- Avoid repeating the same prophecy too frequently
- Add a favicon and social preview image
- Expand automated coverage for game-selection logic
- Add structured logging and reusable API response helpers
- Prepare a production server configuration
- Deploy the game publicly
