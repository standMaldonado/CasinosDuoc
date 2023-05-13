$.validator.addMethod("correito", function (value, element) {
    var pattern = /^([a-zA-Z0-9_.-])+@([a-zA-Z0-9_.-])+\.([a-zA-Z])+([a-zA-Z])+/;
    return this.optional(element) || pattern.test(value);
 }, "Formato del correo incorrecto");

 $.validator.addMethod("nombresito", function (value, element) {
    var pattern = /^[a-zA-Z]+$/;
    return this.optional(element) || pattern.test(value);
 }, "Formato del nombre incorrecto");


$("#formulario").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 40,
            nombresito: true
        },
        email: {
            required: true,
            email: true,
            correito: true
        },
        
        subject:{
            required: true,
            minlength: 10,
            maxlength: 30
        },

        comentario:{
            required: true,
            minlength: 30
        }
    }
})

$("#enviar").click(function(){
    if($("#formulario").valid() == false){
        return; 
    } 
    let nombre = $("nombre").val()
    let email = $("email").val()
    let asunto = $("asunto").val()
    let comentario = $("comentario").val()
    
})