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
    if not request.is_json:
        return {
            "message": "Request body must be JSON."
        },400
    
    data = request.json
    if not isinstance(data, dict):
        return {
            "message": "Request body must be a JSON object."
        }, 400
    
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

    prophecy = fate(question)
    return {
        "prophecy": prophecy
    }


if __name__ == '__main__':
    app.run(debug=True) 