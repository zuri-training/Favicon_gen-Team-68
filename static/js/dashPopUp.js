const femiBox = document.querySelector(".femi-box");
const femiSBox1 = document.querySelector(".femi-subbox.femi-subbox-1");
const femiSBox2 = document.querySelector(".femi-subbox.femi-subbox-2");

const download = document.querySelector("#original-download");
const fileDownload = document.querySelector("#file-download");
console.log(femiBox, femiSBox1, femiSBox2);
const cancelBoxes = document.querySelector(".cancel-boxes");

const popUp = (e) => {
  femiBox.style.display = "block";
  femiSBox1.style.display = "flex";
};

window.addEventListener("load", popUp);

download.addEventListener("click", (e) => {
  fileDownload.click();
  femiSBox1.style.display = "none";
  femiSBox2.style.display = "flex";
});

const rmit = () => {
  femiSBox1.style.display = "none";
  femiSBox2.style.display = "none";
};

cancelBoxes.addEventListener("click", rmit);
document.addEventListener("keydown", (e) => {
  if (e.key == "Escape") rmit();
});
const code_ = document.querySelector(".code code");
const text = code_.textContent;

const femiCopyMe = document.querySelector("#femi-copy-me");

femiCopyMe.addEventListener("click", (e) => {
  navigator.clipboard.writeText(text).then(
    function () {
      alert("Copying to clipboard was successful!");
    },
    function (err) {
      alert("Could not copy text: ", err);
    }
  );
});
