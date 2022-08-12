const myDonwload = document.querySelector(".down.btn-pri");
const downloadForm = document.querySelector("#result-gen");
const downloadForMe = (e) => {
  e.preventDefault();
  console.log(e.target);
  const http = new XMLHttpRequest();
  const fd = new FormData(e.target);
  http.addEventListener("load", (ev) => {
    alert("loaded");
  });
  http.addEventListener("error", (ev) => {
    alert("Oops failed");
  });
  http.onreadystatechange = () => {
    if (http.readyState === 4) {
      console.log(http.response, "checking it");
    }
  };
  http.open("POST", location.origin + "/result/", true);
  http.send(fd);
};

//downloadForm.addEventListener("submit", downloadForMe);

/*const targetImgSrc = document.querySelector("#file-name img")?.src;
const downloadImg = document.querySelector(".prev-board google");
downloadImg?.src = targetImgSrc;*/
