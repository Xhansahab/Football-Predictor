console.log("Football Predictor JS Loaded");

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const button = document.getElementById("predictBtn");
    const btnText = document.getElementById("btnText");
    const loader = document.getElementById("loader");

    form.addEventListener("submit", () => {
        // Change button text
        btnText.textContent = "Predicting...";

        // Show loader
        loader.classList.remove("hidden");

        // Disable button to prevent multiple clicks
        button.disabled = true;
    });
});
