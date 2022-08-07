// Switch Dark and Light background
const darkMode = document.querySelector(".child2");
const lightMode = document.querySelector(".child1");
const prevModalVDiv = document.querySelector(".prev-board");
const codeDiv = document.querySelector(".cp-space");
darkMode.addEventListener("click", () => {
  lightMode.classList.remove("active-toggle");
  darkMode.classList.add("active-toggle");
  prevModalVDiv.style.backgroundColor = "#232330";
 
});
lightMode.addEventListener("click", () => {
  lightMode.classList.add("active-toggle");
  darkMode.classList.remove("active-toggle");
  prevModalVDiv.style.backgroundColor = "#ffffff";
  
});
//closing the modal of upload page
const closeButton = document.querySelector(".close-modal");
const closeBtnDesk = document.querySelector(".close-modal1")
const closeModal = () => {
  modal.style.display = "none";
  closeBtnDesk.classList.add('hidden')
};
closeButton.addEventListener("click", closeModal);
closeBtnDesk.addEventListener("click", closeModal);
document.addEventListener("keydown", (e) => {
  // console.log(e.key)
  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});

const resultForm = document.getElementById("result-gen");
resultForm.addEventListener("submit", (e) => {
  e.preventDefault();
});
//Copying embedded html code for the generated favicon
function CopyToClipboard(containerId) {
  if (document.selection) {
    let range = document.body.createTextRange();
    range.moveToElementText(document.querySelector(".prettyprint"));
    range.select().createTextRange();
    navigator.clipboard.writeText(range);
  } else if (window.getSelection) {
    let range = document.createRange();
    range.selectNode(document.querySelector(".prettyprint"));
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    navigator.clipboard.writeText(range);
  }
}

//Adding embedded html code from the user selection of preferred sizes
let checkboxes = document.querySelectorAll("input[type=checkbox]");

let insertDiv = document.querySelector(".prettyprint");

/*  function func() {
      checkboxes[1].checked = true;
  } */



for (let i = 0; i < checkboxes.length; i++) {
  checkboxes[i].addEventListener("click", function (i) {
    let value = i.target.value;
    let iconType = i.target.classList.value;
    let checked = i.target.checked;
    let valueSet = `${value}x${value}`
    console.log(value, iconType, checked);
   
    if ((checked = true)) {
      let sizes = ['16x16']
      let faviconLink = `<link rel="icon" type="images/x-icon" sizes="${sizes}" href="/favicon.ico">`
     sizes.push(valueSet)
     console.log(sizes.join(' '));
     insertDiv.textContent = faviconLink
    } else if ((checked = false)) {
      insertDiv.textContent = "";
    }
  });
}

