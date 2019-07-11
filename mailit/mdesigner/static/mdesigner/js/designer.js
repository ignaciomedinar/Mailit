createjs.CSSPlugin.install();
const mailCanvas = document.getElementById("mailCanvas");
const moduleOne = document.getElementById("moduleOne");
const heroOne = document.getElementById("heroOne");

const mLeft = document.getElementById("leftMenu");
const informacion =document.getElementById("informacion")
const dotHam = document.getElementById("hamburguer");
const usuario = document.getElementById("usuario");

const dropDown = document.getElementById("dropDown");
const dropdownHero = document.getElementById('dropdownHero');
const dropdownText = document.getElementById('dropdownText');
const dropdownImage = document.getElementById('dropdownImage');
const dropdownExtra = document.getElementById('dropdownExtra');
const dropdownFooter = document.getElementById('dropdownFooter');
const dropdownWidget = document.getElementById('dropdownWidget');

const bHeader = document.getElementById("bHeader");
const bHero = document.getElementById("bHero");
const bText = document.getElementById("bText");
const bImage = document.getElementById("bImage");
const bExtra = document.getElementById("bExtra");
const bFooter = document.getElementById("bFooter");
const bWidget = document.getElementById("bWidget");

const modulesMenus = document.getElementById("modulesMenus");
const hModules = document.getElementById("hamburguerModules");
let fatherModules = document.getElementsByClassName("fatherModules");
const tituloMo = document.getElementById("tituloMo")
const allModules = document.getElementById("allModules");

const headers = document.getElementById("headers");

// open the modules

let buttonStates = 0;


dropDown.style.display = "none";
dropdownHero.style.display = "none";
dropdownText.style.display = "none";
dropdownImage.style.display = "none";
dropdownExtra.style.display = "none";
dropdownFooter.style.display = "none";
dropdownWidget.style.display = "none";


function theButton(theTarget){

    if(theTarget.style.display == "none"){
        theTarget.style.display = "flex"
    }else{
        theTarget.style.display = "none"
    }

    console.log("buttonStates:" + theTarget.style.display)
}




function loadTheHTML(){

    mailCanvas.innerHTML +=
        `

        <!-- START: BP01 Master - Simple Default -->
<!--[if mso | IE]>
<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="620" align="center" style="width:620px;">
<tr>
<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
<![endif]-->
<div style="background: #FFFFFF; margin: 0px auto; max-width: 620px;">
  <table role="presentation" cellpadding="0" cellspacing="0" style="border-collapse: collapse; font-size: 0px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;"
    align="center" border="0" bgcolor="#FFFFFF">
    <tbody>
      <tr>
        <td style="border-collapse: collapse; direction: ltr; font-size: 0px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 20px;"
          class="bp-logo-padding" align="right" valign="top">
          <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
            <tbody>
              <tr>
                <td width="35%" style="border-collapse: collapse; font-size: 0px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 0px; word-break: break-word;"
                  valign="top">
                  <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                    <tbody>
                      <tr>
                        <td class="bp-logo" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 60px;" width="60">
                          <a href="http://www.americanexpress.com/australia" target="_blank" style="font-family: HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif;">
                            <img src="/static/mdesigner/images/AMXIMG_250x250_amex_logo.jpg" alt="AMERICAN EXPRESS" title="American Express Logo"
                              height="auto" style="-ms-interpolation-mode: bicubic; border: 0 none; color: #333333; display: block; font-family: sans-serif; font-size: 10px; height: auto; line-height: 100%; outline: none; text-decoration: none; width: 60px;"
                              width="60">
                          </a>
                        </td>
                        <td width="12" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> </td>

                        <td class="bp-tagline" width="65" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                          <a href="#LINK_TO" target="_blank" style="font-family: HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif;">
                            <img src="/static/mdesigner/images/DLLWI.gif" alt="Don't live life without it" title="Don't live life without it" height="auto"
                              style="-ms-interpolation-mode: bicubic; border: 0 none; color: #333333; display: block; font-family: sans-serif; font-size: 12px; height: auto; line-height: 100%; outline: none; text-decoration: none; width: 65px;"
                              width="65">
                          </a>
                        </td>

                        <td style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
                <td width="65%" align="right" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" valign="top">

                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                    <tr>
                      <td style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                        <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">

                          <tr>
                            <td class="bp-text" style="border-collapse: collapse; color: #333333; cursor: auto; font-family: HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 22px; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                              align="right" valign="top">
                              Account ending: 12345
                            </td>
                          </tr>

                          <tr>
                            <td class="bp-text bp-hide" style="border-collapse: collapse; color: #333333; cursor: auto; font-family: HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 22px; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                              align="right" valign="top">
                              Member since: 2018
                            </td>
                          </tr>

                        </table>
                      </td>

                    </tr>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>

      <tr>
        <td class="bp-acct-padding" style="border-bottom-color: #d9d9d6; border-bottom-style: solid; border-bottom-width: 1px; border-collapse: collapse; border-top-color: #d9d9d6; border-top-style: solid; border-top-width: 1px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 10px 20px;">
          <table role="presentation" cellpadding="0" cellspacing="0" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
            align="right" border="0" width="100%">
            <tbody>
              <tr>
                <td style="border-collapse: collapse; font-size: 0px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                  align="left" valign="middle">
                  <div class="bp-text" style="color: #333333; cursor: auto; font-family: HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 22px;">Hello, Ann Cardmember</div>
                </td>
                <td style="border-collapse: collapse; font-size: 0px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                  align="right">
                  <table border="0" cellspacing="0" cellpadding="0" align="right" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                    <tr>

                      <td style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                        <table border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                          <tr>
                            <td align="center" style="border-collapse: collapse; border-radius: 3px; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" bgcolor="#ffffff">
                              <a href="http://www.americanexpress.com/australia" class="bp-login-button" target="_blank" style="background: #ffffff; border: 1px solid #006fcf; border-radius: 3px; color: #006fcf; display: inline-block; font-family: HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 15px; font-weight: normal; line-height: 100%; margin: 0px; padding: 11px 12px 12px; text-decoration: none; text-transform: none;">Log in</a>
                            </td>
                          </tr>
                        </table>
                      </td>

                    </tr>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
</div>
<!--[if mso | IE]>
</td></tr></table>
<![endif]-->
<!-- END: BP01 Master - Simple Default -->


        `


}





var colorin;
var defaultColor = "#000000";

window.addEventListener("load", startup, false);

function startup() {
    colorin = document.querySelector("#colorin");
    colorin.value = defaultColor;
    colorin.addEventListener("input", updateFirst, false);
    colorin.addEventListener("change", updateAll, false);
    colorin.select();

    txtTi = document.querySelector("#colorin");
    txtTi.value = defaultColor;
    txtTi.addEventListener("input", updateFirst, false);
    txtTi.addEventListener("change", updateAll, false);
    txtTi.select();

    txtCu = document.querySelector("#colorin");
    txtCu.value = defaultColor;
    txtCu.addEventListener("input", updateFirst, false);
    txtCu.addEventListener("change", updateAll, false);
    txtCu.select();
  }


  var color = "#567890"


  function updateFirst(event) {
    var p = document.getElementById("color");
    var cambiaColor = document.getElementById("cambiaColor");
    var txtTitulo = document.getElementById("txtTitulo");
    var txtCuerpo = document.getElementById("txtCuerpo");





    color = event.target.value;
    // txtTitulo.innerText = event.target.value;
    // txtCuerpo.innerText = event.target.value;

    // p.innerHTML = color;
    // cambiaColor.innerHTML = color;
    console.log(color);

    if (cambiaColor) {
      cambiaColor.style.backgroundColor = event.target.value;
    //   p.style.color = event.target.value;
    //   color = p.style.color;
    }

    if (txtTitulo) {
        txtTitulo.innerText = event.target.value;
      //   p.style.color = event.target.value;
      //   color = p.style.color;
      }

      if (txtCuerpo) {
        txtCuerpo.innerText = event.target.value;
      //   p.style.color = event.target.value;
      //   color = p.style.color;
      }
  }

  function updateAll(event) {
  document.querySelectorAll("p").forEach(function(p) {
    // p.style.color = event.target.value;
    cambiaColor.style.backgroundColor = event.target.value;
    color = event.target.value;
    txtCuerpo.innerHTML = event.target.value;
    txtTitulo.innerText = event.target.value;
  });
}





// var colorin = document.getElementById("colorin");





var textTitulo = "Este es un título dinámico"
var textInside = "El texto debe cambiar con esta información";

function loadTheHeroOne(){

    mailCanvas.innerHTML +=
    `



    <!-- START: HB01 Block Left -->
<!--[if mso | IE]>
<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="620" align="center" style="width:620px;">
<tr>
<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
<![endif]-->
<div style="background: #A7A8AA; margin: 0px auto; max-width: 620px;">
  <table role="presentation" cellpadding="0" cellspacing="0" style="border-collapse: collapse; font-size: 0px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;"
    align="center" border="0" bgcolor="#A7A8AA">
    <tbody>
      <tr>
        <td style="border-collapse: collapse; direction: ltr; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" align="left" valign="middle">
          <table role="presentation" cellpadding="0" cellspacing="0" style="border-collapse: collapse; font-size: 0px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;"
            align="center" border="0">
            <tbody>
              <tr>
                <th id="cambiaColor" class="hb-full hb-reset" width="206" height="320" style="background-color:${color}; direction: ltr; font-weight: normal; height: 320px; width: 206px;" align="center" bgcolor="${color}" valign="middle">
                  <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                    <tr>
                      <td style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding-left: 20px; padding-right: 20px;"
                        class="hb-reset-text">
                        <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                          <tbody>

                            <tr>
                              <td align="center" style="border-collapse: collapse; color: #FFFFFF; cursor: auto; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 20px; line-height: 28px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                               >
                                <p id"txtTitulo" style="display: block; margin: 0;">${textTitulo}</p>
                              </td>
                            </tr>
                            <tr>
                              <td align="center" style="border-collapse: collapse; color: #FFFFFF; cursor: auto; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 22px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding-top: 8px; word-break: break-word;"
                               >
                                <p id= "txtCuerpo" style="display: block; margin: 0;">${textInside}</p>
                              </td>
                            </tr>

                            <tr>
                              <td align="center" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding-top: 20px;">
                                <table width="164" height="38" cellpadding="0" cellspacing="0" border="0" align="center" style="border-collapse: collapse; border-radius: 3px; mso-hide: all; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                  class="hb-hero-button">
                                  <tr>
                                    <td align="center" valign="middle" height="38" style="border-collapse: collapse; border-radius: 3px; color: #333333; font-family: HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 15px; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                      bgcolor="#ffffff">
                                      <a href="#LINK_TO" class="hb-hero-button" target="_blank" style="border-radius: 3px; color: #333333; display: inline-block; font-family: HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif; font-weight: normal; line-height: 22px; padding: 8px 0px; text-decoration: none; text-transform: none; width: 164px;">Find out more</a>
                                    </td>
                                  </tr>
                                </table>
                                <!--[if mso]>
                                  <table border="0" cellspacing="0" cellpadding="0" align="center" style="display: none; mso-hide: none!important;">
                                    <tr>
                                      <td>
                                        <table width="164" height="38" cellpadding="0" cellspacing="0" border="0" style="border-radius:3px;">
                                          <tr>
                                            <td align="center" valign="middle" width="164" height="38" style="background-color: #ffffff;font-family:HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif; font-size:15px;border-radius:3px;">
                                              <a href="#LINK_TO" target="_blank" style="color: #333333;font-family:HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif; display: inline-block; text-decoration: none; padding:8px 0px 8px 0px;line-height:22px; width:164px;font-weight:normal;text-transform:none;">Find out more</a>
                                            </td>
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                  </table>
                                <![endif]-->
                              </td>
                            </tr>

                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </table>
                </th>

                <th class="hb-full" width="414" style="direction: ltr; font-size: 0px; font-weight: normal; padding: 0px; width: 414px;" align="center" valign="middle">
                  <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                    <tbody>
                      <tr>
                        <td style="border-collapse: collapse; font-size: 0px; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 0px; word-break: break-word;"
                          align="center">
                          <table class="hbnb-imgBox" role="presentation" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border-spacing: 0px; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                            align="center" border="0">
                            <tbody>
                              <tr>
                                <td style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 414px;">
                                  <img src="/static/mdesigner/images/AMXIMG_414x320_placeholder.png" alt="" title="" height="320" style="-ms-interpolation-mode: bicubic; border: 0 none; display: block; height: 320px; line-height: 100%; outline: none; text-decoration: none; width: 414px;"
                                    width="414">
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </th>

              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
</div>
<!--[if mso | IE]>
</td></tr></table>
<![endif]-->
<!-- END: HB01 Block Left -->






    `
}


bHeader.addEventListener("click", theButton.bind(this, dropDown), false);
bHero.addEventListener("click", theButton.bind(this, dropdownHero), false);
bText.addEventListener("click", theButton.bind(this, dropdownText), false);
bImage.addEventListener("click", theButton.bind(this, dropdownImage), false);
bExtra.addEventListener("click", theButton.bind(this, dropdownExtra), false);
bFooter.addEventListener("click", theButton.bind(this, dropdownFooter), false);
bWidget.addEventListener("click", theButton.bind(this, dropdownWidget), false);


moduleOne.addEventListener("click", loadTheHTML);
heroOne.addEventListener("click", loadTheHeroOne);
// theButton(dropDown);





dotHam.addEventListener("click", openMenu);

mLeft.style.width = "45px";
dotHam.style.marginLeft = '1%';
usuario.style.opacity = "0.0";
informacion.style.marginLeft = "-700px";
usuario.style.display = "none";
headers.style.backgroundColor = "#757575";






// function that open the left menu
function openMenu(){

    if(mLeft.style.width == "45px"){

        usuario.style.display = "block";
        informacion.style.display = "block"
        createjs.Tween.get(informacion).to({marginLeft:"0"},1000,createjs.Ease.sineOut);
        createjs.Tween.get(dotHam).to({marginLeft:"65"},1000,createjs.Ease.sineOut);
        createjs.Tween.get(usuario).to({opacity:"0.9"},1000,createjs.Ease.sineOut);
        createjs.Tween.get(mLeft).to({width:"206"},1000,createjs.Ease.sineOut);
    }else{

        informacion.style.display = "none"
        usuario.style.display = "none";
        createjs.Tween.get(informacion).to({marginLeft:"-700"},1000,createjs.Ease.sineOut);
        createjs.Tween.get(informacion).to({opacity:"0"},1000,createjs.Ease.sineIn);
        createjs.Tween.get(usuario).to({opacity:"0"},1000,createjs.Ease.sineIn);
        createjs.Tween.get(dotHam).to({marginLeft:"1"},1000,createjs.Ease.sineIn);
        createjs.Tween.get(mLeft).to({width:"45"},1000,createjs.Ease.sineIn);
    }
}




modulesMenus.style.width = "333px";
hModules.addEventListener('click', openModules);
// fatherModules.style.marginRight = "0px";
allModules.style.marginLeft = "0px";


function openModules(){

    if(modulesMenus.style.width == "333px"){
        allModules.style.display = "none";
        tituloMo.style.display = "none";

        createjs.Tween.get(modulesMenus).to({width:"46"},1000,createjs.Ease.sineOut);
        createjs.Tween.get(allModules).to({marginLeft:"370"},1000,createjs.Ease.sineOut);
    }else{

        tituloMo.style.display = "inherit";
        allModules.style.display = "inherit";
        createjs.Tween.get(modulesMenus).to({width:"333"},1000,createjs.Ease.sineIn);
        createjs.Tween.get(allModules).to({marginLeft:"0"},1000,createjs.Ease.sineOut);
    }
}
