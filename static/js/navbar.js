const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const genDropDown = document.querySelector('.drop-down');
const generate = document.
getElementById('nav-generate');
// const bar = document.getElementById('bar');
const activeUpload = document.querySelector('.up');
hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
});

document.querySelectorAll(".nav-link").forEach((n) =>
  n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
  })
);
const genDrop = ()=>{
  genDropDown.style.display = 'flex'  
}
generate.addEventListener("hover", genDrop);
generate.addEventListener("click", genDrop);
activeUpload.addEventListener("hover", function(){
  activeUpload.classList.toggle("active-upload");
});
activeUpload.addEventListener("click", function(){
  activeUpload.classList.add("active-upload");
});