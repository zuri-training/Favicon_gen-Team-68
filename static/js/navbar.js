const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const genDropDown = document.querySelector('.drop-down');
const generate = document.
getElementById('nav-generate');
const acc = document.querySelector('.acc')
const accDropDown = document.querySelector('.drop-down-2')
// const bar = document.getElementById('bar');
const activeUpload = document.querySelector('.up');
hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("activebar");
});

document.querySelectorAll(".nav-link").forEach((n) =>
  n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    hamburger.style.top = 80%
    navMenu.classList.add("activebar");
  })
);

const genDrop = ()=>{
  genDropDown.style.display = 'flex'  
}
const removeGendrop = ()=>{
  genDropDown.style.display = 'none'
}

generate.addEventListener("click", genDrop);
generate.addEventListener("mouseover", genDrop);
generate.addEventListener('mouseout', removeGendrop)
activeUpload.addEventListener("mouseover", function(){
  activeUpload.classList.toggle("active-upload");
});
activeUpload.addEventListener("click", function(){
  activeUpload.classList.add("active-upload");
});
const displayAcc = () =>{
accDropDown.style.display = 'flex'
}
const removeAcc = () =>{
  accDropDown.style.display = 'none'
}
acc.addEventListener('click', displayAcc)

acc.addEventListener('mouseout', removeAcc)