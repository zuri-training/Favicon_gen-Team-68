const visibility = document.getElementById("visibility")
visibility.addEventListener("click", toggleVisibility)

function toggleVisibility(){
    const passwordInput = document.getElementById("password")
    if (passwordInput.type === "password") {
        passwordInput.type = "text"
    }
    else{
        passwordInput.type = "password"
    }
}