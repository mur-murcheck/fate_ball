const form = document.getElementById("prediction-form");
const questionInput = document.getElementById("question");
const predictionElement = document.getElementById("prediction");

async function handleSubmit(event) {
    event.preventDefault();
    const question = questionInput.value.trim();
    const requestBody = {"question": question};
    const jsonBody = JSON.stringify(requestBody);
    console.log(jsonBody);
    const response = await fetch("/api/predictions", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: jsonBody
    });
    console.log(response.status);
    const data = await response.json();
    predictionElement.textContent = data.prophecy;
    console.log(data);
    console.log(data.prophecy);
}

form.addEventListener("submit", handleSubmit);