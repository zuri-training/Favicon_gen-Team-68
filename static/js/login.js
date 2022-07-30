const togglePassword1 = document.querySelector("#hide1");
const togglePassword2 = document.querySelector("#hide2");
const password = document.querySelector("#password");

togglePassword1.addEventListener("click", function () {
  // toggle the type attribute
  if (password.type === 'password'){
    password.type = 'text'
    togglePassword1.style.display = 'block'
  }
});
