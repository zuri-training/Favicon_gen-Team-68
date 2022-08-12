const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const genDropDown = document.querySelector('.drop-down');
const generate = document.
getElementById('nav-generate');
const acc = document.querySelector('.acc')
const accDropDown = document.querySelector('.drop-down-2"')
// const bar = document.getElementById('bar');
const activeUpload = document.querySelector('.up');
// hamburger.addEventListener("click", () => {
//   hamburger.classList.toggle("active");
//   navMenu.classList.toggle("active");
// });

document.querySelectorAll(".nav-link").forEach((n) =>
  n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
  })
);

const genDrop = ()=>{
  genDropDown.style.display = 'flex'  
}

generate.addEventListener("click", genDrop);
generate.addEventListener("hover", genDrop);
activeUpload.addEventListener("hover", function(){
  activeUpload.classList.toggle("active-upload");
});
activeUpload.addEventListener("click", function(){
  activeUpload.classList.add("active-upload");
});
const displayAcc = () =>{
accDropDown.style.display = 'flex'
}
acc.addEventListener('click', displayAcc)
acc.addEventListener('hover', displayAcc)