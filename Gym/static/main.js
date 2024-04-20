// static/js/validations.js

$(document).ready(function () {
  // Validación de solo letras para todos los campos de texto
  $('input[type="text"]').on('keypress', function (e) {
    var tecla = e.keyCode || e.which;
    var patron = /[A-Za-z\s]/;
    var teclaFinal = String.fromCharCode(tecla);
    return patron.test(teclaFinal);
  });

  // Validación de solo números para todos los campos numéricos
  $('input[type="number"]').on('keypress', function (e) {
    var tecla = e.keyCode || e.which;
    var patron = /\d/;
    var teclaFinal = String.fromCharCode(tecla);
    return patron.test(teclaFinal);
  });
});

