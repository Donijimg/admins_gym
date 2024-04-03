const ficha = document.getElementById("ficha");
const nombre = document.getElementById("nombre");
const apellidos = document.getElementById("apellidos");
const correo = document.getElementById("correo");
const telefono = document.getElementById("telefono");
const genero = document.getElementsByName("genero");
const contenedor_genero = document.getElementById("contenedor_genero")
const ciudad = document.getElementById("ciudad");
const gustos = document.getElementsByName("gustos");
const contenedor_gustos = document.getElementById("contenedor_gustos")
const enviar = document.getElementById("enviar");

let reFicha = /^[a-zA-Z]{3}_[0-9]{5}$/;
let reNombres = /^[a-zA-Z]+(?: [a-zA-Z]+){0,19}$/;
let reCorreo = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/;
let reTelefono = /^[0-9]{10}$/;


const entradaValida = function (campo) {
  if (campo.classList.contains("borde-rojo")) {
    campo.classList.remove("borde-rojo");
  }
  campo.classList.add("borde-verde");
}

const entradaInvalida = function (campo) {
  if (campo.classList.contains("borde-verde")) {
    campo.classList.remove("borde-verde");
  }
  campo.classList.add("borde-rojo");
}


const validarFicha = function () {
  if (reFicha.test(ficha.value)) {
    return true;
    // ficha.focus()
    // bordeRojo(ficha)
  } else {
    return false;
  }
}


const validarSoloLetras = function (campo) {
  if (reNombres.test(campo.value)) {
    return true;
  } else {
    return false;
  }
}

const validarCorreo = function () {
  if (reCorreo.test(correo.value)) {
    return true;
  } else {
    return false;
  }
}
const validarTelefono = function () {
  if (reTelefono.test(telefono.value)) {
    return true;
  } else {
    return false;
  }
}

const letras = function (e) {
  const key = e.keyCode || e.which;
  const tecla = String.fromCharCode(key).toLowerCase();
  const letras = "áéíóúabcdefghijklmnopqrstuvwxyz";
  const especiales = ['8', '32', '37', '39', '46'];
  let tecla_especial = false
  for (const i in especiales) {
    if (key == especiales[i]) {
      tecla_especial = true;
      break;
    }
  }
  if (letras.indexOf(tecla) == -1 && !tecla_especial) {
    e.preventDefault()
  }
}



const numeros = (e) => {
  //Validamos que el keyCode corresponda a las teclas de los números
  if ((e.keyCode < 48 || e.keyCode > 57) && e.keyCode) {
    e.preventDefault()
  }
}

const validarGenero = function () {
  let genero_valido = 0
  for (const boton of genero) {
    if (boton.checked) {
      genero_valido = boton.value
      break
    }
  }
  if (genero_valido != 0) {
    return true
    // e.preventDefault()
    // alert("Indique un género")
  } else {
    return false
  }
}

const validarCiudad = function () {
  if (ciudad.value != "") {
    return true

  }
  else {
    return false
  }
}

const validarGustos = function () {
  let checkbox_activos = 0
  for (const box of gustos) {
    if (box.checked) {
      checkbox_activos += 1
    }
  }
  if (checkbox_activos >= 3) {
    return true
    // e.preventDefault()
    // alert("Seleccione mínimo 3 gustos")
  } else {
    return false
  }
}

const validarFormulario = function(e){
  if (validarFicha()){
    entradaValida(ficha);
    if (validarSoloLetras(nombre)) {
      entradaValida(nombre);
      if (validarSoloLetras(apellidos)) {
        entradaValida(apellidos);
        if (validarCorreo()){
          entradaValida(correo);
          if (validarTelefono()){
            entradaValida(telefono);
            if (validarGenero()) {
              entradaValida(contenedor_genero);
              if (validarCiudad()){
                entradaValida(ciudad);
                if (validarGustos()){
                  entradaValida(contenedor_gustos);
                  alert("Enviando formulario");
                } else {
                  entradaInvalida(contenedor_gustos);
                  e.preventDefault();
                } //gustos
              } else {
                entradaInvalida(ciudad);
                e.preventDefault();
                ciudad.focus()
              } //ciudad
            } else {
              entradaInvalida(contenedor_genero);
              e.preventDefault();
            }//genero
          } else {
            entradaInvalida(telefono);
            e.preventDefault();
            telefono.focus()
          } // telefono
        } else {
          entradaInvalida(correo);
          e.preventDefault();
          correo.focus()
        }//correo
      } else {
        entradaInvalida(apellidos);
        e.preventDefault();
        apellidos.focus()
      } //apellidos
    } else {
      entradaInvalida(nombre);
      e.preventDefault();
      nombre.focus()
    } //nombre
  } else {
    entradaInvalida(ficha);
    e.preventDefault();
    ficha.focus()
  }//ficha
}
// ficha.addEventListener('blur', () => {
//   validarFicha(ficha);
// })



// apellidos.addEventListener('blur', () => {
//   validarSoloLetras(apellidos);
// })

// correo.addEventListener('blur', () => {
//   validarCorreo(correo);
// })

nombre.addEventListener('keypress', letras)
apellidos.addEventListener('keypress', letras)
telefono.addEventListener('keypress', numeros)




enviar.addEventListener("click", validarFormulario)

// enviar.addEventListener("click", validarGenero)

// enviar.addEventListener("click", validarGustos)
enviar.addEventListener("click", validarCiudad)


