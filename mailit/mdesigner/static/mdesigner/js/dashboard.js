
createjs.CSSPlugin.install();

const ham = document.getElementById("hamburguer");

const firstMenu = document.getElementById("dashboard");

const logo = document.getElementById("elLogo");

ham.addEventListener("mousedown", openMenu);

firstMenu.style.width = "45px";

function openMenu(){
    
    
    // createjs.Tween.get(firstMenu).to({width:"180"},1000,createjs.Ease.backIn);   
    


    if(firstMenu.style.width == "45px"){
        createjs.Tween.get(firstMenu).to({width:"180"},1000,createjs.Ease.backIn);  
    }else{
        createjs.Tween.get(firstMenu).to({width:"45"},1000,createjs.Ease.sinOut);  
    }



    // var pos = 45;
    // var id = setInterval(frame, 2);

    // console.log("scaleX:" + scaleX)


    
    // function frame(){
    //     if (pos == 180){
    //         clearInterval(id);
    //     } else{
    //         pos++;
    //         firstMenu.style.width = pos + "px";
    //     }
    // }

    // logo.innerHTML = "mail IT";
}


