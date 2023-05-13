$.validator.addMethod("correito", function (value, element) {
    var pattern = /^([a-zA-Z0-9_.-])+@([a-zA-Z0-9_.-])+\.([a-zA-Z])+([a-zA-Z])+/;
    return this.optional(element) || pattern.test(value);
 }, "Formato del email incorrecto");

$("#formulario").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 5,
            maxlength: 40
        },
        email: {
            required: true,
            email: true,
            correito: true
        },
        rut: {
            required: true,
            minlength: 9,
            number : true
        },
        comentario:{
            required: true,
            minlength: 50
        }
    }
})

$("#enviar").click(function(){
    if($("formulario").valid() == false){
        return; 
    } 
    let nombre = $("nombre").val()
    let email = $("email").val()
    let comentario = $("comentario").val()
    
})