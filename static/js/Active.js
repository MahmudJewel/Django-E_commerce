console.log("Hello!!!, js connected");

// Add active class to the current button (highlight it)
// let header = document.getElementById("subIndex");
// let btns = header.getElementsByClassName("abc");
// console.log(btns)
// for (let i = 0; i < btns.length; i++) {
//   btns[i].addEventListener("click", function () {
//     let current = document.getElementsByClassName("active");
//     current[0].className = current[0].className.replace(" active", "");
//     this.className += " active";
//   });
// }

//   for (let i = 0; i < btns.length; i++) {
//     btns[i].click(function(){
//         $(this).addClass("active").siblings().removeClass("active");
//       });
//   }
// Add active class to the current button (highlight it)
let hd = document.getElementById("subIndex");
let btnss = hd.getElementsByClassName("btn");
console.log(btnss)
for (let i = 0; i < btnss.length; i++) {
  btnss[i].addEventListener("click", function () {
    let current = document.getElementsByClassName("active");
    if (current.length>0){
        current[0].className = current[0].className.replace(" active", "");
        // console.log(current[0])
    }
    // current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
    console.log(this.className);
  });
}
