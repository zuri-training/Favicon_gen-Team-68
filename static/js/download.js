const myDonwload = document.querySelector(".down.btn-pri");
const downloadForm = document.querySelector("#result-gen");
const downloadForMe = (e) => {
  e.preventDefault();
  console.log(e.target);
};

downloadForm.addEventListener("submit", downloadForMe);

/*const targetImgSrc = document.querySelector("#file-name img")?.src;
const downloadImg = document.querySelector(".prev-board google");
downloadImg?.src = targetImgSrc;*/
