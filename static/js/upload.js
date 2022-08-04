// Switch Dark and Light background
const darkMode = document.querySelector(".child2");
const lightMode = document.querySelector(".child1");
const prevModalVDiv = document.querySelector(".prev-board");
const codeDiv = document.querySelector(".cp-space");
darkMode.addEventListener("click", () => {
  lightMode.classList.remove("active-toggle");
  darkMode.classList.add("active-toggle");
  prevModalVDiv.style.backgroundColor = "#232330";
  codeDiv.style.backgroundColor = "#232330";
  codeDiv.style.color = "#ffffff";
});
lightMode.addEventListener("click", () => {
  lightMode.classList.add("active-toggle");
  darkMode.classList.remove("active-toggle");
  prevModalVDiv.style.backgroundColor = "#ddd";
  codeDiv.style.backgroundColor = "#ddd";
});
//closing the modal of upload page
const closeButton = document.querySelector(".close-modal");
const closeModal = () => {
  modal.style.display = "none";
};
closeButton.addEventListener("click", closeModal);
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
    range.moveToElementText(document.querySelector(".cp-space"));
    range.select().createTextRange();
    navigator.clipboard.writeText(range);
  } else if (window.getSelection) {
    let range = document.createRange();
    range.selectNode(document.querySelector(".cp-space"));
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    navigator.clipboard.writeText(range);
  }
}

//Adding embedded html code from the user selection of preferred sizes
let checkboxes = document.querySelectorAll("input[type=checkbox]");

const insertDiv = document.getElementById("box");

/*  function func() {
      checkboxes[1].checked = true;
  } */

for (let i = 0; i < checkboxes.length; i++) {
  checkboxes[i].addEventListener("click", function (i) {
    let value = i.target.value;
    let iconType = i.target.classList.value;
    let checked = i.target.checked;
    console.log(value, iconType, checked);
    let html2 = ` &lt;link rel="manifest" href="/site.webmanifest"&gt; `;
    let html3 = `<code class="prettyprint"> &lt;link rel="apple-touch-icon" sizes="${i.value}x${i.value}" href="/apple-touch-icon.png"&gt; </code>`;
    let html1 = `<code class="prettyprint"> &lt;link rel="icon" type="image/png" sizes="${value}x${value}" href="/favicon-${value}x${value}.png"&gt; </code>`;
    if ((checked = true)) {
      if (iconType == "size-icon") {
        insertDiv.insertAdjacentHTML("afterbegin", html1 + "\n");
      } else if (iconType == "mani") {
        insertDiv.insertAdjacentHTML("afterbegin", html2 + "\n");
      } else if (iconType == "apple") {
        insertDiv.insertAdjacentHTML("afterbegin", html3 + "\n");
      }
    } else if ((checked = false)) {
      insertDiv.textContent = "";
    }
  });
}

