const ficha = document.getElementById("id_ficha");
const nombre = document.getElementById("id_nombre");
const apellidos = document.getElementById("id_apellidos");
const correo = document.getElementById("id_correo");
const telefono = document.getElementById("id_telefono");

let reFicha = /^[a-zA-Z]{3}_[0-9]{5}$/;
let reNombres = /^[a-zA-Z]+(?: [a-zA-Z]+){0,19}$/;
let reCorreo = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
let reTelefono = /^[0-9]{10}$/;

const validarCampo = function (campo, regex) {
  return regex.test(campo.value.trim());
}

const mostrarError = function (campo, mensaje) {
  // Muestra el mensaje de error al usuario (puedes implementar esto según tus necesidades)
  console.error(mensaje);
}

const validarFormulario = function (e) {
  if (!validarCampo(ficha, reFicha)) {
    e.preventDefault();
    mostrarError(ficha, "Formato de ficha incorrecto. Debe ser de la forma ABC_12345");
  }
  if (!validarCampo(nombre, reNombres)) {
    e.preventDefault();
    mostrarError(nombre, "El nombre no puede estar vacío y solo puede contener letras");
  }
  if (!validarCampo(apellidos, reNombres)) {
    e.preventDefault();
    mostrarError(apellidos, "Los apellidos no pueden estar vacíos y solo pueden contener letras");
  }
  if (!validarCampo(correo, reCorreo)) {
    e.preventDefault();
    mostrarError(correo, "Correo electrónico inválido");
  }
  if (!validarCampo(telefono, reTelefono)) {
    e.preventDefault();
    mostrarError(telefono, "El número de teléfono debe contener 10 dígitos");
  }
}

// Registra el evento de validación al enviar el formulario
document.getElementById("formulario").addEventListener("submit", validarFormulario);



const documentoAdmin = document.getElementById("id_documento_admin");
const identificacionPropietario = document.getElementById("id_identificacion_propietario");

// Agrega más campos según sea necesario

let reDocumento = /^[0-9]{8}$/;
let reIdentificacion = /^[a-zA-Z0-9]{8}$/;

// Agrega más expresiones regulares según sea necesario

const validarCampoAdmin = function (campo, regex) {  // Renombrar la función para evitar conflicto
  return regex.test(campo.value.trim());
}

const mostrarErrorAdmin = function (campo, mensaje) {  // Renombrar la función para evitar conflicto
  // Muestra el mensaje de error al usuario (puedes implementar esto según tus necesidades)
  console.error(mensaje);
}

const validarFormularioAdmin = function (e) {
  if (!validarCampoAdmin(documentoAdmin, reDocumento)) {  // Utilizar la función renombrada
    e.preventDefault();
    mostrarErrorAdmin(documentoAdmin, "El documento debe contener 8 dígitos numéricos");  // Utilizar la función renombrada
  }
  if (!validarCampoAdmin(identificacionPropietario, reIdentificacion)) {  // Utilizar la función renombrada
    e.preventDefault();
    mostrarErrorAdmin(identificacionPropietario, "La identificación debe contener 8 caracteres alfanuméricos");  // Utilizar la función renombrada
  }
  // Agrega más validaciones según sea necesario para otros campos del formulario Admin
}

// Registra el evento de validación al enviar el formulario Admin
document.getElementById("formulario_admin").addEventListener("submit", validarFormularioAdmin);

// Agrega funciones de validación y eventos para otros formularios si es necesario
