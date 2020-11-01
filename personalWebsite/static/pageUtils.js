window.addEventListener("scroll", resizeElementsOnScroll);

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
    document.getElementById("navbar-brand").style.fontSize="1.5em";
  }
  else{
    document.getElementById("navigation-bar").style.padding = ".5em";
    document.getElementById("nav-list-container").style.fontSize = "21px";
    var x = document.getElementById("navbar-logo");
    x.style.width = "65px";
    x.style.height = "65px";
    document.getElementById("navbar-brand").style.fontSize="1.8em";
  }
}
