from flask import Flask
from flask import request
from ball_body import fate
from flask import render_template

# Create the Flask application. Flask uses __name__ to locate templates and
# static files relative to this module.
app = Flask(__name__)

# Serve the browser interface. The prediction itself is requested separately
# from the JSON API below, so this route only renders the initial HTML page.
@app.route("/")
def index():
    return render_template("index.html")

# A lightweight endpoint for checking that the application is running.
@app.route("/api/health")
def health_check():
    return {
        "status": "ok"
    }


@app.route("/api/predictions", methods=["POST"])
def get_prediction():
    # Reject requests whose Content-Type does not declare JSON. This check must
    # happen before reading request.json.
    if not request.is_json:
        return {
            "message": "Request body must be JSON."
        },400
    
    data = request.json
    # Valid JSON can still be a list, string, or number. The API contract
    # requires a JSON object so that it can contain a "question" field.
    if not isinstance(data, dict):
        return {
            "message": "Request body must be a JSON object."
        }, 400
    
    question = data.get("question")

    # Validate from the most fundamental condition to the most specific one.
    # This order prevents string operations from being called on invalid types.
    if question is None:
        return {
            "message": "The question field is required"
        }, 422


    if not isinstance(question, str):
        return {
            "message": "The question must be a string."
        }, 422

    if question.strip() == "":
        return {
            "message": "The question must not be empty."
        }, 422

    if len(question) > 512:
        return {
            "message": "The question must not contain more than 512 characters"
        }, 422

    prophecy = fate(question)
    return {
        "prophecy": prophecy
    }


# Allow direct local execution with `python app.py`. When Flask imports this
# module through its CLI, this block is skipped.
if __name__ == '__main__':
    app.run(debug=True)
