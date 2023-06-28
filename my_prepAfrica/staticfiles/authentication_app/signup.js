document.addEventListener("DOMContentLoaded", function () {
    console.log("linked")
  const passwordInput = document.getElementById("password");
  const confirmPasswordInput = document.getElementById("confirmPassword");
  const form = document.getElementById("signupForm");
  const errorContainer = document.getElementById("errorContainer");
  const errorMessage = document.getElementById("errorMessage");

  form.addEventListener("submit", function (event) {
    console.log(passwordInput.value);
    console.log(password.value);
    if (passwordInput.value !== confirmPasswordInput.value) {
      // Prevent form submission
      errorContainer.style.display = "block";
      errorMessage.textContent = "Passwords do not match.";
      event.preventDefault();
    } else {
      form.submit();
    }
  });
});
