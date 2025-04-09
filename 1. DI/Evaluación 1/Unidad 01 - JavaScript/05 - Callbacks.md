# Callbacks

**Concepto:**  
Un callback es una función que se pasa como argumento a otra función y se ejecuta cuando se cumple una tarea asíncrona o una condición.

**Sintaxis:**

```js
function saludar(callback) {
  callback("¡Hola, mundo!");
}

saludar(function(mensaje) {
  console.log(mensaje); // Imprime: ¡Hola, mundo!
});
```

> **Anotación**: En este ejemplo, la función _saludar_ recibe una función (callback) y la ejecuta pasando el mensaje "¡Hola, mundo!" como argumento.

**Ejemplo con setTimeout:**

```javascript
setTimeout(function() {
  console.log("Finalizado callback");
}, 2000);
console.log("Hola");
```

> **Anotación:** En este ejemplo, "Hola" se imprime inmediatamente y "Finalizado callback" aparece después de 2 segundos, demostrando la ejecución asíncrona mediante un callback.

**Ejemplo leyendo un archivo:**

```js
const fs = require('fs');

// Lee el archivo 'miArchivo.txt' de forma asíncrona
fs.readFile('miArchivo.txt', 'utf8', function(err, data) {
  if (err) {
    console.error("Error leyendo el archivo:", err);
    return;
  }
  console.log("Contenido del archivo:", data);
});
```

> **Anotación:** En este caso, la función pasada a `readFile` es el callback que se ejecutará cuando se termine de leer el archivo, gestionando el error o mostrando el contenido.


