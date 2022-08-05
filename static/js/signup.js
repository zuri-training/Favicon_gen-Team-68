const toggle = document.querySelector(".eyes");
const password = document.querySelector("#password");

toggle.addEventListener("click", () => {
  // toggle the type attribute
  if (password.type === "password") {
    password.type = "text";
    toggle.classList.replace("fa-eye-slash", "fa-eye");
  } else {
    password.type = "password";
    toggle.classList.replace("fa-eye", "fa-eye-slash");
  }
});

const signup = document.getElementById("submit");
signup.addEventListener("click", () => {
  signup.textContent = "Creating account....";
});
