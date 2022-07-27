const visibility = document.querySelector("#visibility");
    const password = ("click", "#password");

visibility.addEventListener('click', function(e) {
    const type = password.getAttribute('type')=== "password" ? "text" : "password";
    password.setAttribute('type', type)
    this.classList.toggle('fa-eye-slash');
});
