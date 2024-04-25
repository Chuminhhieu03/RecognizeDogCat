document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("formRecognize")
    .addEventListener("submit", function (event) {
      event.preventDefault();

      let formData = new FormData(this);
      fetch("/recognize/", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          document.getElementById("text-result").textContent = data.message;
        })
        .catch((error) => console.error("Error:", error));
    });
});
