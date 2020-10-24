/* Métodos de validación */
$.validator.addMethod( "pattern", function( value, element, param ) {
    if ( this.optional( element ) ) {
        return true;
    }
    if ( typeof param === "string" ) {
        param = new RegExp( "^(?:" + param + ")$" );
    }
    return param.test( value );
}, "Formato invalido." );

$.validator.addMethod( "rut", function( value, element ) {
	if ( this.optional( element ) ) {
		return "dependency-mismatch";
	}

	var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car = value.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = value.slice(-1).toUpperCase();

	return dv == dv_usuario;
}, "Ingrese un rut correcto. Utilice 10 dígitos " );

$.validator.addMethod( "nowhitespace", function( value, element ) {
	return this.optional( element ) || /^\S+$/i.test( value );
}, "No se aceptan espacios en blanco." );

$.validator.addMethod( "precio", function( value, element ) {
	return this.optional( element ) || value > 0;
}, "Precio debe ser mayor a 0." );


/* Parámetros de validación */
jQuery.validator.setDefaults({
errorClass: 'error-text',
highlight: function(element) {
    $(element)
    .removeClass('borde')
    .addClass('error');
},
unhighlight: function(element) {
    $(element)
    .removeClass('error')
    .addClass('valido');
}
});

/* Ejecutar Validación */
$( "#formLogin" ).validate({
    rules: {
        usuario: {
            required: true,
            nowhitespace: true
        },
        contrasena: {
            required: true
        },
    }
});

$( "#formInsumos" ).validate({
    rules: {
        precio: {
            required: true,
            digits: true,
            minlength: 1,
            precio: true
        },
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 120,
            pattern: "([a-zA-Z ])+"
        },
        stock: {
            required: true
        },
        descripcion: {
            required: false,
            minlength: 3,
            maxlength: 200,
            pattern: "([a-zA-Z ])+"
        },
    }
});

$( "#formRegistro" ).validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 80,
            pattern: "([a-zA-Z ])+"
        },
        apellido: {
            required: true,
            minlength: 3,
            maxlength: 80,
            pattern: "([a-zA-Z ])+"
        },
        correo: {
            required: true,
            email: true
        },
        usuario: {
            required: true,
            minlength: 8,
            nowhitespace: true
        },
        contrasena: {
            required: true,
            minlength: 8
        },
        confirmacion: {
            required: true,
            equalTo: "#txtContrasena"
        },
    }
});

/* Mensajes de error Login */
$("#txtUser").rules("add", {
    messages: {
        required: "Campo obligatorio"
      }
});
$("#txtPassword").rules("add", {
    messages: {
        required: "Campo obligatorio"
      }
});

/* Mensajes de error Registro */
$("#txtRut").rules("add", {
    messages: {
        required: "Campo obligatorio",
        pattern: "Campo inválido"
      }
});
$("#txtNombre").rules("add", {
    messages: {
        required: "Campo obligatorio",
        minlength: jQuery.validator.format("Por favor, ingresar al menos {0} caracteres"),
        maxlength: jQuery.validator.format("Por favor, ingresar máximo {0} caracteres"),
        pattern: "Campo inválido"
      }
});
$("#txtApellido").rules("add", {
    messages: {
        required: "Campo obligatorio",
        minlength: jQuery.validator.format("Por favor, ingresar al menos {0} caracteres"),
        maxlength: jQuery.validator.format("Por favor, ingresar máximo {0} caracteres"),
        pattern: "Campo inválido"
      }
});
$("#txtCorreo").rules("add", {
    messages: {
        required: "Campo obligatorio",
        email: "Por favor, ingrese un email válido"
      }
});
$("#dtpFechaNac").rules("add", {
    messages: {
        required: "Campo obligatorio",
        max: jQuery.validator.format("Por favor, ingresar una fecha menor o igual a {0}")
      }
});
$("#txtUsuario").rules("add", {
    messages: {
        required: "Campo obligatorio",
        minlength: jQuery.validator.format("Por favor, ingresar al menos {0} caracteres")
      }
});
$("#txtContrasena").rules("add", {
    messages: {
        required: "Campo obligatorio",
        minlength: jQuery.validator.format("Por favor, ingresar al menos {0} caracteres")
      }
});
$("#txtConfirmar").rules("add", {
    messages: {
        required: "Campo obligatorio",
        equalTo: "La contraseña no coincide"
      }
});

/* Mensajes de error Insumos */
$("#txtPrecio").rules("add", {
    messages: {
        required: "Campo obligatorio",
        minlength: jQuery.validator.format("Por favor, ingresar al menos {0} caracteres")
      }
});
$("#txtStock").rules("add", {
    messages: {
        required: "Campo obligatorio"
      }
});
$("#txtDescripcion").rules("add", {
    messages: {
        required: "Campo obligatorio",
        minlength: jQuery.validator.format("Por favor, ingresar al menos {0} caracteres"),
        maxlength: jQuery.validator.format("Por favor, ingresar máximo {0} caracteres"),
        pattern: "Campo inválido"
      }
});
