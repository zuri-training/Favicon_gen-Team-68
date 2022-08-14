const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const genDropDown = document.querySelector('.drop-down');
const generate = document.
getElementById('nav-generate');
const acc = document.querySelector('.acc')
const accDropDown = document.querySelector('.drop-down-2')
// const bar = document.getElementById('bar');
const activeUpload = document.querySelectorAll('.up');
const user = document.querySelector('.nav-paragraph')


hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("activebar");
});

document.querySelectorAll(".nav-link").forEach((n) =>
  n.addEventListener("click", () => {
    hamburger.classList.remove("active");
   
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
// activeUpload.addEventListener("mouseover", function(){
//   activeUpload.classList.toggle("active-upload");
// });
activeUpload.forEach((on) => on.addEventListener("click", () =>{
  on.classList.contains("active-upload")? on.classList.remove("active-upload"):on.classList.add("active-upload");
  
}));
activeUpload.forEach((on) => on.addEventListener("mouseover", () =>{
  on.classList.toggle("active-upload");
  
}));
const displayAcc = () =>{
accDropDown.style.display = 'flex'
} 
const removeAcc = () =>{
  accDropDown.style.display = 'flex'? accDropDown.style.display = 'none' : accDropDown.style.display = 'flex'
 }
acc.addEventListener('click', displayAcc)
acc.addEventListener('mouseover', displayAcc)
acc.addEventListener('click', removeAcc)
user.addEventListener('click', displayAcc)
user.addEventListener('mouseover', displayAcc)
user.addEventListener('click', removeAcc)

document.querySelectorAll('.accprof').forEach((link) =>link.addEventListener('click', removeAcc))