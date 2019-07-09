
createjs.CSSPlugin.install();

const ham = document.getElementById("hamburguer");

const firstMenu = document.getElementById("dashboard");

const logo = document.getElementById("elLogo");

ham.addEventListener("mousedown", openMenu);

firstMenu.style.width = "45px";

function openMenu(){
    
    if(firstMenu.style.width == "45px"){
        createjs.Tween.get(firstMenu).to({width:"180"},1000,createjs.Ease.backIn);  
    }else{
        createjs.Tween.get(firstMenu).to({width:"45"},1000,createjs.Ease.sinOut);  
    }

}


