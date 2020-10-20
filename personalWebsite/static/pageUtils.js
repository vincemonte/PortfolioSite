window.addEventListener("scroll", resizeElementsOnScroll);

function resizeElementsOnScroll() {
  resizeJumbotron();
  resizeNavBar();
}

function resizeJumbotron(){
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50){
    document.getElementById("home-jumbotron").style.padding = "1.5em";
  }
  else{
    document.getElementById("home-jumbotron").style.padding = "4em";
  }
}

function resizeNavBar(){
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50){
    document.getElementById("navigation-bar").style.padding = "0";
    document.getElementById("page-links").style.fontSize="16px";
    var x = document.getElementById("logo");
    x.style.width = "40px";
    x.style.height = "40px";
  }
  else{
    document.getElementById("navigation-bar").style.padding = ".5em";
    document.getElementById("page-links").style.fontSize = "19px";
    var x = document.getElementById("logo");
    x.style.width = "60px";
    x.style.height = "60px";
  }
}
