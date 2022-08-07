const form = document.getElementById("upload");
const modal = document.getElementById("modal");
const overlay = document.querySelector(".overlay");
const fileName = document.getElementById("file-name");
const input = document.getElementById("file-input");
const closeBtnDesk = document.querySelector("..close-modal1")
const closeButton = document.querySelector(".close-modal");
const width = window.innerWidth;

const displayImage = (e) => {
  while (fileName.firstChild) {
    fileName.removeChild(fileName.firstChild);
  }
  const image = document.createElement("img");
  const div = document.createElement("div");
  div.textContent = e.target.files[0].name;
  image.src = URL.createObjectURL(e.target.files[0]);
  image.style.marginTop = "20px";
  image.style.maxWidth = "200px";
  fileName.appendChild(image);
  fileName.appendChild(div);
};

const generateIcon = (e) => {
  e.preventDefault();
  const http = new XMLHttpRequest();
  const fd = new FormData(e.target);
  http.addEventListener("load", (ev) => {
    if(width > 768){
      closeBtnDesk.classList.remove('hidden')
      closeButton.style.display = "none"
      modal.style.display = "flex";
    }else{
      modal.style.display = "flex";
    }
    
  });
  if (fd.get("file-input").size > 10e6) {
    alert("file size exceeded 10 mb");
    return;
  }
  http.addEventListener("error", (event) => {
    alert("Oops failed to upload");
  });
  http.open("POST", location.origin + "/upload/", true);
  http.send(fd);
};

input.addEventListener("change", displayImage);
form.addEventListener("submit", generateIcon);
