const rights = document.querySelectorAll(".right-cont");
const centers = document.querySelectorAll(".center-cont");
const lefts = document.querySelectorAll(".left-cont");

const options = {
  threshold: 0,
  rootMargin: "0px 0px -200px 0px",
};

const appearOnScroll = new IntersectionObserver(function (
  entries,
  appearOnScroll
) {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add("appear");
    console.log(entry.target);
    appearOnScroll.unobserve(entry.target);
  });
},
options);

lefts.forEach((left) => appearOnScroll.observe(left));
rights.forEach((right) => appearOnScroll.observe(right));
centers.forEach((center) => appearOnScroll.observe(center));
