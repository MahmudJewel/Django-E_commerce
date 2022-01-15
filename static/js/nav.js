// responsive left-index 
const burger=document.querySelector(".burger");
const nav=document.querySelector(".nav_right");
const bb=document.querySelector(".bb");

 // for sliding navbar
burger.addEventListener('click', navSlide);  
bb.addEventListener('click', navSlide);

function navSlide(){
	nav.classList.toggle('nav_active');
	burger.classList.toggle('toggle');
}