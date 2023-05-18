// Obtener referencia al formulario y al botón de envío
const formulario = document.getElementById('miFormulario');
const botonSubmit = document.getElementById('botonSubmit');

// Agregar un evento de escucha al botón de envío
botonSubmit.addEventListener('click', validarFormulario);

// Función de validación del formulario
function validarFormulario(evento) {
  evento.preventDefault(); // Evitar el envío del formulario por defecto

  // Obtener el valor del campo "nombre"
  const nombreInput = document.getElementById('nombre');
  const nombre = nombreInput.value.trim();

  // Verificar si el campo "nombre" está vacío
  if (nombre === '') {
    mostrarError('El campo Nombre está vacío');
  } else {
    mostrarMensaje('Nombre completo');
    formulario.submit(); // Enviar el formulario si la validación pasa
  }
}

// Función para mostrar un mensaje de error
function mostrarError(mensaje) {
  const errorDiv = document.getElementById('error');
  errorDiv.textContent = mensaje;
}

// Función para mostrar un mensaje de éxito
function mostrarMensaje(mensaje) {
  const mensajeDiv = document.getElementById('mensaje');
  mensajeDiv.textContent = mensaje;
}
