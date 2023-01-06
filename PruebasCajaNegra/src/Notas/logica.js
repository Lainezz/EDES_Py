/**
 * No modificar este método. Permite la ejecución del programa de forma correcta.
 * Para la resolución de los ejercicios, simplemente codifica lo que se pide dentro
 * de la función correspondiente.
 * @param {*} e
 */
const checkForm = (e) => {
  e.preventDefault();
};

const comprobarNota = () => {
  let inputNota = document.querySelector("#inputNota").value;

  const reg = /^-?\d*\.{0,1}\d+$/;
  console.log(typeof inputNota);
  let mensaje;
  
  //Comprueba que lo que se ha introducido en el input corresponde con un número
  if (reg.test(inputNota)) {
    inputNota = parseFloat(inputNota);
    
    if (inputNota >= 0 && inputNota < 5) {
      mensaje = "Suspenso";
    } else if (inputNota >= 5 && inputNota < 10) {
      mensaje = "Aprobado";
    } else if (inputNota === 10) {
      mensaje = "Matricula";
    } else {
      mensaje = "Error";
    }
  
  } else { //Si se introduce otra cosa que no sea un número, imprime un mensaje de error
    alert("Error en el tipo de dato");
    mensaje = "Error en el tipo de dato";
  }

  document.querySelector("#pNota").innerHTML = mensaje;
};

function onIniciar() {
  const btnIngresar = document.querySelector("#comprobarNota");
  btnIngresar.addEventListener("click", comprobarNota);
}

window.onload = onIniciar();
