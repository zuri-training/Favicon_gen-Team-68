var togglePassword1 = document.querySelector("#hide1");
var togglePassword2 = document.querySelector("#hide2");
var password = document.querySelector("#password");

togglePassword1.addEventListener("click", function () {
   
  // toggle the type attribute
  if (password.type === 'password'){
    password.type = 'text'
    togglePassword1.style.display = block
    togg
  }
 
});
        // prevent form submit
        var form = document.querySelector("form");
        form.addEventListener('submit', function (e) {
            e.preventDefault();
        });