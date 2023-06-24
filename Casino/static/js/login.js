

if (nom === "admin" && con=== "admin") {
    modal.style.display = "none";
    btnAdministrar.disabled = false;
    console.log("bueno")
}else{
    console.log("malo")
    modal.style.display = "none";
    btnAdministrar.disabled = true;
}



window.onload = function() {
    var modal = document.getElementById("cuadro");
    
    // Comprobar si el modal ya se ha mostrado anteriormente
    var modalShown = sessionStorage.getItem("modalShown");
    
    if (!modalShown) {
        // Mostrar el modal si no se ha mostrado anteriormente
        modal.style.display = "block";
        sessionStorage.setItem("modalShown", true);
    }
    
}

