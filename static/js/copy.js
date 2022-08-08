const downloadBtn = document.querySelector(".down-btn-pri");
const secondModal = document.getElementById("modal2");
const test = document.querySelector('.prettyprint')
const closeButtonDeskCopy = document.querySelector(".close-modal22")
const copyHtml = document.querySelector('.down-btn-grey2')
const width = window.innerWidth;

downloadBtn.addEventListener("click", ()=>{
    
        modal.style.display = "none";
      closeButtonDeskCopy.classList.remove('hidden')
        secondModal.style.display = "flex";

});

const closeModal2 = () => {
    secondModal.style.display = "none";
  closeButtonDeskCopy.classList.add('hidden')
  };
closeButtonDeskCopy.addEventListener('click', closeModal2)
// copyHtml.addEventListener('click', closeModal2)
  document.addEventListener("keydown", (e) => {
    // console.log(e.key)
    if (e.key === "Escape" && !modal.classList.contains("hidden")) {
      closeModal2();
    }
  });

  //Copying embedded html code for the generated favicon
function CopyToClipboard2(containerId) {
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