# Import the Flask application without starting a real development server.
# Every test uses Flask's in-process test client instead of Postman or a port.
from app import app

# Pytest automatically discovers functions whose names start with `test_`.
def test_health():
    client = app.test_client()
    response = client.get("/api/health")

    # Check both parts of the public contract: HTTP status and JSON body.
    assert response.status_code == 200 
    assert response.get_json() == {"status": "ok"}

# A random prophecy cannot be compared with one exact sentence. Instead, verify
# the stable response shape, value type, and non-empty content.
def test_prophecy():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={"question": "Will I be rich?"}
    )
    data = response.get_json()


    assert response.status_code == 200
    assert "prophecy" in data
    assert isinstance(data["prophecy"], str)
    assert data["prophecy"].strip()

# A valid empty JSON object is different from a missing/non-JSON request body:
# its structure is understood, but the required field is absent.
def test_prophecy_without_question():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={}
    )
    data = response.get_json()

    assert response.status_code == 422
    assert data == {"message": "The question field is required"}

# Empty strings are valid JSON strings but invalid questions.
def test_prophecy_with_empty_question():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={"question": ""}
    )
    data = response.get_json()


    assert response.status_code == 422
    assert data == {"message": "The question must not be empty."}

# The question field must contain text, not another valid JSON type.
def test_prophecy_with_non_string_question():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={"question": 42}
    )
    data = response.get_json()


    assert response.status_code == 422
    assert data == {"message": "The question must be a string."}

# Test the accepted side of the 512-character boundary.
def test_prophecy_proper_length():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={"question": "a"*512}
    )
    data = response.get_json()


    assert response.status_code == 200
    assert "prophecy" in data

# Test the rejected side of the same boundary to catch off-by-one errors.
def test_prophecy_inproper_length():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={"question": "a"*513}
    )
    data = response.get_json()


    assert response.status_code == 422
    assert data == {"message": "The question must not contain more than 512 characters"}

# `data` sends plain text and an explicit text/plain Content-Type, unlike the
# test client's `json` argument, which serializes data and declares JSON.
def test_prophecy_is_not_JSON():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        data="Will I be pretty?",
        content_type="text/plain"
    )
    data = response.get_json()


    assert response.status_code == 400
    assert data == {"message": "Request body must be JSON."}

# A JSON array is syntactically valid JSON, but the API requires an object.
def test_prophecy_JSON_is_not_an_object():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json=["Will I be rich?"]
    )
    data = response.get_json()


    assert response.status_code == 400
    assert data == {"message": "Request body must be a JSON object."}


# Confirm that Flask can render the template and that essential page hooks for
# the form and JavaScript integration are present in the returned HTML.
def test_main_page_content():
    client = app.test_client()
    response = client.get("/")
    html = response.get_data(as_text=True)


    assert response.status_code == 200
    assert "FATE BALL" in html
    assert "prediction-form" in html
    assert "/static/app.js" in html
