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

const login = document.getElementById("submit");
const usernameEl = document.querySelector('#username');
const emailEl = document.querySelector('#email');
const passwordEl = document.querySelector('#password');
const form = document.querySelector('.form');



const checkEmail = () => {
    let valid = false;
    const email = emailEl.value.trim();
    if (!isRequired(email)) {
        showError(emailEl, 'Email cannot be blank.');
    } else {
        showSuccess(emailEl);
        valid = true;
    }
    return valid;
};

const checkPassword = () => {
    let valid = false;


    const password = passwordEl.value.trim();

    if (!isRequired(password)) {
        showError(passwordEl, 'Password cannot be blank.');
    }  else {
        showSuccess(passwordEl);
        valid = true;
    }

    return valid;
};

/* const checkConfirmPassword = () => {
    let valid = false;
    // check confirm password
    const confirmPassword = confirmPasswordEl.value.trim();
    const password = passwordEl.value.trim();

    if (!isRequired(confirmPassword)) {
        showError(confirmPasswordEl, 'Please enter the password again');
    } else if (password !== confirmPassword) {
        showError(confirmPasswordEl, 'The password does not match');
    } else {
        showSuccess(confirmPasswordEl);
        valid = true;
    }

    return valid;
}; */

const isEmailValid = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

const isRequired = value => value === '' ? false : true;
const isBetween = (length, min, max) => length < min || length > max ? false : true;


const showError = (input, message) => {
    // get the form-field element
    const field = input.parentElement;
    // add the error class
    field.classList.remove('success');
    field.classList.add('error');

    // show the error message
    const error = field.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const field = input.parentElement;

    // remove the error class
    field.classList.remove('error');
    field.classList.add('success');

    // hide the error message
    const error = field.querySelector('small');
    error.textContent = '';
}

const loggin = (e) => {
    e.preventDefault();

     // validate fields
    let isEmailValid = checkEmail(),
    isPasswordValid = checkPassword();
   
    let isFormValid = isEmailValid &&
     isPasswordValid;

    const http = new XMLHttpRequest();
    const fd = new FormData(e.target);
    http.addEventListener("load", (ev) => {
      // submit to the server if the form is valid
      if (isFormValid) {
        login.textContent = "Authenticating....";
        
      }
    });
    http.open("POST", location.origin + "/login/", true);
    http.send(fd);
  };

form.addEventListener('submit',loggin);


const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

form.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'email':
            checkEmail();
            break;
        case 'password':
            checkPassword();
            break;

    }
}));