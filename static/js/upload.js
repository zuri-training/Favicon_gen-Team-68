
const darkMode = document.querySelector('.child2')
const lightMode = document.querySelector('.child1')
const prevModalVDiv = document.querySelector('prev-board')
darkMode.addEventListener('click', ()=>{
    prevModalVDiv.style.backgroundColor = '#323337'
    lightMode.classList.remove('active-toggle')
    darkMode.classList.add('active-toggle')
   
})


