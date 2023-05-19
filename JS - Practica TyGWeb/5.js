//Definir una función que muestre información sobre una cadena de texto que se le
//pasa como argumento. A partir de la cadena que se le pasa, la función determina si
//esa cadena está formada sólo por mayúsculas, sólo por minúsculas o por una mezcla
//de ambas.

function mostrarInfo(string){
    if (string === string.toUpperCase()){
        console.log("La cadena esta formada enteramente por mayusculas.");

    } else if (string === string.toLowerCase()){
        console.log("La cadena esta formada enteramente por minusculas.");
    } else{
        console.log("La cadena es una mezcla de las dos.")
    }
}