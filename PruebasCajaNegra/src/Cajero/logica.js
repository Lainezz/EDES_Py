

/**
 * No modificar este método. Permite la ejecución del programa de forma correcta.
 * Para la resolución de los ejercicios, simplemente codifica lo que se pide dentro
 * de la función correspondiente.
 * @param {*} e 
 */
const checkForm = (e) => {
  e.preventDefault();
  
};

const ingresar = () => {
  const inputCantidad = document.querySelector("#inputCantidad").value;
  if (inputCantidad < 0) {
    alert("La cantidad no puede ser negativa");
  }else if(inputCantidad > 3500){
    alert("Alerta por ingreso mayor a 3500€. Se procederá a avisar a Hacienda")
  }else{;
    var pSaldo = document.querySelector("#pSaldo");
    let saldo = parseFloat(pSaldo.innerHTML.split("€")[0]) + parseFloat(inputCantidad)
    pSaldo.innerHTML = saldo + "€"
  }
};

const retirar = () => {
  const inputCantidad = document.querySelector("#inputCantidad").value;
  var pSaldo = document.querySelector("#pSaldo");
  if (inputCantidad < 0) {
    alert("La cantidad no puede ser negativa");
  } else if (inputCantidad > 3500) {
    alert("Alerta por ingreso mayor a 3500€. Se procederá a avisar a Hacienda");
  } else {
    
    let saldo = parseFloat(pSaldo.innerHTML.split("€")[0]) - parseFloat(inputCantidad);
    pSaldo.innerHTML = saldo + "€";
  }
};


function onIniciar() {
  const btnIngresar = document.querySelector("#ingresar");
  const btnRetirar = document.querySelector("#retirar");
  btnIngresar.addEventListener("click", ingresar);
  btnRetirar.addEventListener("click", retirar);
}

window.onload = onIniciar();
