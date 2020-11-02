function isMobile() {
  var check = false;
  if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
  check = true;
  }
  return check;
};

if( isMobile() == false ) {
 window.addEventListener("scroll", resizeElementsOnScroll);
}


function resizeElementsOnScroll() {
  resizeNavBar();
}


function resizeNavBar(){
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50){
    document.getElementById("navigation-bar").style.padding = ".1em";
    document.getElementById("nav-list-container").style.fontSize="19.3px";
    var x = document.getElementById("navbar-logo");
    x.style.width = "40px";
    x.style.height = "40px";
    x= document.getElementById("image-link");
    x.style.width = "36px";
    x.style.height = "36px";
    x.style.paddingTop = "4px";
    document.getElementById("navbar-brand").style.fontSize="1.5em";
  }
  else{
    document.getElementById("navigation-bar").style.padding = ".5em";
    document.getElementById("nav-list-container").style.fontSize = "21px";
    var x = document.getElementById("navbar-logo");
    x.style.width = "65px";
    x.style.height = "65px";
    x= document.getElementById("image-link");
    x.style.width = "40px";
    x.style.height = "40px";
    x.style.paddingTop = "inherit";
    document.getElementById("navbar-brand").style.fontSize="1.8em";
  }
}
