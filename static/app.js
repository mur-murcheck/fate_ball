const form = document.getElementById("prediction-form");
const questionInput = document.getElementById("question");
const predictionElement = document.getElementById("prediction");
const errorElement = document.getElementById("error-message");
const submitButton = document.getElementById("submit-button");
const ballElement = document.querySelector(".ball");

async function handleSubmit(event) {
    event.preventDefault();
    predictionElement.classList.remove("revealed");
    predictionElement.textContent = "";
    errorElement.textContent = "";
    submitButton.disabled = true;
    submitButton.textContent = "Consulting the stars...";
    ballElement.classList.add("thinking");
    const question = questionInput.value.trim();
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

        if (!response.ok) {
            errorElement.textContent = data.message;
            return;
        }

        predictionElement.textContent = data.prophecy;
        predictionElement.classList.add("revealed");
    } catch (error) {
        errorElement.textContent = 
            "The crystal ball has lost its connection to the beyond. Try again.";
        console.error(error);
    } finally {
        submitButton.disabled = false;
        submitButton.textContent = "Ask the Orb";
        ballElement.classList.remove("thinking");
    }
}

form.addEventListener("submit", handleSubmit);