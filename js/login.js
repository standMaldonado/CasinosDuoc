
function entrar(){
    event.preventDefault();

    var nom = document.getElementById("nom").value;
    var con = document.getElementById("con").value;
    var modal = document.getElementById('cuadro');
    

    if (nom === "admin" && con=== "admin") {
        modal.style.display = "none";
    }else{
        alert("Los datos ingresados no son los correctos... ");
    }
    
}

