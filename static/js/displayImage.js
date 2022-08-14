const fileName = document.getElementById("file-name");
const input = document.getElementById("file-input");

const displayImage = (e) => {
  while (fileName.firstChild) {
    fileName.removeChild(fileName.firstChild);
  }
  const image = document.createElement("img");
  const div = document.createElement("div");
  div.textContent = e.target.files[0].name;
  image.src = URL.createObjectURL(e.target.files[0]);
  imgUrlDownload = image.src;
  image.style.marginTop = "20px";
  image.style.maxWidth = "200px";
  fileName.appendChild(image);
  fileName.appendChild(div);
};

input.addEventListener("change", displayImage);
