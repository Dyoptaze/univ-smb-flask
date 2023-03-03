const nom = document.getElementById("myTH")

window.addEventListener("click",
    function(nom){
        let nomInfo = nom.target.getAttribute("data-info");
        console.log(nomInfo);
        if( nomInfo != null){
            alert(nomInfo);
        }
    })