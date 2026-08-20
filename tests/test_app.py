# import app (the Flask object) from app.py
from app import app

# we need prefix test_ so Pytest could find it
def test_health():
    # testing client (like Postman)
    client = app.test_client()
    # virtual GET query to the client
    # calling /api/health -> get dictionary -> turns it into JSON -> 
    # -> create a response object -> return it to the test
    # response is HTTP-response (status-code, headers, content-type, body)
    response = client.get("/api/health")

    # check if right expression is True
    assert response.status_code == 200 
    # get_json takes JSON's body and turn it into Python dictionary
    # then, compare two dictionaries actual_response == expected_response
    assert response.get_json() == {"status": "ok"}

# the success response
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

# the question fiel is required
def test_prophecy_without_question():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={}
    )
    data = response.get_json()

    assert response.status_code == 422
    assert data == {"message": "The question field is required"}

# the question fiel is empty
def test_prophecy_with_empty_question():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={"question": ""}
    )
    data = response.get_json()


    assert response.status_code == 422
    assert data == {"message": "The question must not be empty."}

# wrong type of the question field
def test_prophecy_with_non_string_question():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={"question": 42}
    )
    data = response.get_json()


    assert response.status_code == 422
    assert data == {"message": "The question must be a string."}

# length contents less than 513 characters
def test_prophecy_proper_length():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={"question": "a"*512}
    )
    data = response.get_json()


    assert response.status_code == 200
    assert "prophecy" in data

# length contents more than 512 characters
def test_prophecy_inproper_length():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json={"question": "a"*513}
    )
    data = response.get_json()


    assert response.status_code == 422
    assert data == {"message": "The question must not contain more than 512 characters"}

# wrong Content-type
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

# wrong JSON form
def test_prophecy_JSON_is_not_an_object():
    client = app.test_client()
    response = client.post(
        "/api/predictions",
        json=["Will I be rich?"]
    )
    data = response.get_json()


    assert response.status_code == 400
    assert data == {"message": "Request body must be a JSON object."}


def test_main_page_content():
    client = app.test_client()
    response = client.get("/")
    html = response.get_data(as_text=True)


    assert response.status_code == 200
    assert "FATE BALL" in html
    assert "prediction-form" in html
    assert "/static/app.js" in html