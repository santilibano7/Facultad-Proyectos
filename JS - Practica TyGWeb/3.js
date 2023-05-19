var valores = [true, 5, false, "hola","adios", 2];

//Ejercicio A
var hola = valores[3];
var adios = valores[4];

if (hola.length > adios.length){
    console.log(hola + " es mayor que " + adios);
} else if (hola.length < adios.length){
    console.log(adios + " es mayor que " + hola);
} else{
    console.log("Ambos tienen la misma longitud.");
}

//Ejercicio B
var resultadoTrue = valores[0] || valores[2]; // true || false
console.log(resultadoTrue); // true

var resultadoFalse = valores[0] && valores[2]; // true && false
console.log(resultadoFalse); // false

//Ejercicio C
var cinco = valores[2];
var dos = valores[5];

let suma = cinco + dos;
console.log(suma);

let resta = cinco - dos;
console.log(resta);

let multi = cinco * dos;
console.log(multi);

let div = cinco / dos;
console.log(div);

let exp = cinco ** dos;
console.log(exp);