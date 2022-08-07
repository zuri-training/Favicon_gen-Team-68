const downloadBtn = document.querySelector(".down-btn-pri");
const secondModal = document.getElementById("modal2");
const test = document.querySelector('.prettyprint')
const closeBtnDesk2 = document.querySelector('.close-modal2')
const copyHtml = document.querySelector('.down-btn-grey2')
const width = window.innerWidth;

downloadBtn.addEventListener("click", ()=>{
    if(width > 768){
        modal.style.display = "none";
        closeBtnDesk.classList.remove('hidden')
        secondModal.style.display = "flex";
    }
});

const closeModal2 = () => {
    secondModal.style.display = "none";
    closeBtnDesk2.classList.add('hidden')
  };
  closeBtnDesk2.addEventListener('click', closeModal2)
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