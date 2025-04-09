# Funciones

**Funciones Tradicionales**  
Definen bloques de código reutilizables usando la palabra clave _function_.

```javascript
function sumar(num1, num2) {
  return num1 + num2;
}
console.log(sumar(3, 2)); // Imprime 5
```

**Funciones Anónimas**  
Se asignan a una variable sin nombre explícito.

```javascript
let sumar = function(num1, num2) {
  return num1 + num2;
};
console.log(sumar(3, 2));
```

**Arrow Functions**  
Sintaxis corta y moderna; si la función solo devuelve un valor, se omiten llaves y la palabra _return_.

```javascript
// Con dos parámetros:
let sumar = (num1, num2) => num1 + num2;
console.log(sumar(3, 2)); // Imprime 5

// Con un solo parámetro:
let doble = num => 2 * num;
console.log(doble(3)); // Imprime 6
```

> **Nota:** Las arrow functions no tienen acceso a `this` ni a `arguments`, por lo que, si necesitas ese comportamiento, usa funciones tradicionales o anónimas.