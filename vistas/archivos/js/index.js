

document.querySelector('#botonLoguin').addEventListener('click', () => {
    email = document.querySelector('#email').value
    contraseña = document.querySelector('#contraseña').value

    var data = {
        email,
        contraseña
    }
    $.ajax({
        url: "/auth",
        method: "POST",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (respuesta) {
            if (respuesta.login) {
                window.location.href = respuesta.home
            } else {
                window.location.href = respuesta.home
            }

        }

    });

});



