document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();

  fetch("/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, message })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("formResponse").textContent = data.message;
    document.getElementById("contactForm").reset();
  })
  .catch(error => {
    document.getElementById("formResponse").textContent = "Error sending message.";
    console.error("Error:", error);
  });
});
