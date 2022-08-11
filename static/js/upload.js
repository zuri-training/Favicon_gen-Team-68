// Switch Dark and Light background
const darkMode = document.querySelector(".child2");
const lightMode = document.querySelector(".child1");
const prevModalVDiv = document.querySelector(".prev-board");
const centerContainerUpload = document.querySelector(".container-main");
const closeButtonDeskUpload = document.querySelector(".close-modal1");
const closeButtonMobileUpload = document.querySelector(".close-modal");

const codeDiv = document.querySelector(".cp-space");
darkMode?.addEventListener("click", () => {
  lightMode.classList.remove("active-toggle");
  darkMode.style.backgroundColor = "#0a0a0b";
  darkMode.style.color = "#ffffff";
  prevModalVDiv.style.backgroundColor = "#232330";
});
lightMode?.addEventListener("click", () => {
  lightMode.classList.add("active-toggle");
  darkMode.style.backgroundColor = "#ffffff";
  darkMode.style.color = "#191a1c";
  prevModalVDiv.style.backgroundColor = "#ffffff";
});
//closing the modal of upload page

const closeModal = () => {
  modal.style.display = "none";
  closeButtonDeskUpload.classList.add("hidden");
};
closeButtonDeskUpload.addEventListener("click", closeModal);
closeButtonMobileUpload.addEventListener("click", closeModal);
centerContainerUpload.addEventListener("click", closeModal);
document.addEventListener("keydown", (e) => {
  // console.log(e.key)
  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});

const resultForm = document.getElementById("result-gen");
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
    let valueSet = `${value}x${value}`;
    console.log(value, iconType, checked);
    let sizes = [];

    //     if ((checked = true)) {

    //       let faviconLink = `<link rel="icon" type="images/x-icon" sizes="${sizes}" href="/favicon.ico">`;
    //       sizes.push(valueSet);
    //       console.log(sizes.join(" "));
    //       insertDiv.textContent = faviconLink;
    //     } else if ((checked = false)) {
    //       insertDiv.textContent = "";
    //     }
  });
}

