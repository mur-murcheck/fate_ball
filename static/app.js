// Cache the page elements used by the submit handler. Looking them up once
// keeps the event logic concise and makes each element's role explicit.
const form = document.getElementById("prediction-form");
const questionInput = document.getElementById("question");
const predictionElement = document.getElementById("prediction");
const errorElement = document.getElementById("error-message");
const submitButton = document.getElementById("submit-button");
const ballElement = document.querySelector(".ball");

async function handleSubmit(event) {
    // Take control of submission so the browser does not reload the page.
    event.preventDefault();

    // Reset the previous result and show a temporary busy state while the API
    // request is in progress.
    predictionElement.classList.remove("revealed");
    predictionElement.textContent = "";
    errorElement.textContent = "";
    submitButton.disabled = true;
    submitButton.textContent = "Consulting the stars...";
    ballElement.classList.add("thinking");
    const question = questionInput.value.trim();

    // fetch() sends text over HTTP, so convert the JavaScript object into a
    // JSON string matching the Flask API contract.
    const requestBody = {"question": question};
    const jsonBody = JSON.stringify(requestBody);

    try {
        const response = await fetch("/api/predictions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: jsonBody
        });
        const data = await response.json();

        // fetch() only rejects on connection failures. HTTP errors such as 422
        // still produce a response, so handle them explicitly via response.ok.
        if (!response.ok) {
            errorElement.textContent = data.message;
            return;
        }

        // Add the class after inserting the text so CSS can animate the new
        // prophecy each time a successful response arrives.
        predictionElement.textContent = data.prophecy;
        predictionElement.classList.add("revealed");
    } catch (error) {
        // This branch handles failures where no usable HTTP response arrives,
        // for example when the Flask server is unavailable.
        errorElement.textContent = 
            "The crystal ball has lost its connection to the beyond. Try again.";
        console.error(error);
    } finally {
        // finally always runs after success or failure, preventing the button
        // and orb from remaining stuck in their busy states.
        submitButton.disabled = false;
        submitButton.textContent = "Ask the Orb";
        ballElement.classList.remove("thinking");
    }
}

// Register the handler after all required DOM references have been collected.
form.addEventListener("submit", handleSubmit);
