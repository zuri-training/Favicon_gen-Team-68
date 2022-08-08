const right = document.querySelectAll('right-cont')
const center = document.querySelectAll('center-cont')
const left = document.querySelectAll('left-cont')

const options = {
  threshold: 0;
  rootMargin: '0px 0px -200px 0px'
}

const appearOnScroll = new IntersectionObserver(function (entries, appearOnScroll){
  entries.forEach((entry) => {
    if(!entry.isIntersecting) return;
    entry.target.classList.add('appear')
    appearOnScroll.unobserve(entry.target);
  })
}, options)


