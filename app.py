from flask import Flask
from flask import request
from ball_body import fate

app = Flask(__name__)

@app.route("/api/health")
def health_check():
    return {
        "status": "ok"
    }


@app.route("/api/predictions", methods=["POST"])
def get_prediction():
    data = request.json
    question = data.get("question")

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

    return question


if __name__ == '__main__':
    app.run(debug=True) 