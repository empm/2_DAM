
Importante que dentro de un mismo grupo, para que solo se pueda seleccionar un valor, todos deben tener el mismo `name`

elemento change

```js
let opciones = document.getElementById("cars");
opciones.addEventListener('change', () => {
	console.log(opciones.value);
	console.log(opciones.selectedIndex);
})
```

Al cambiar el select se ver'ia

```
functions.js:8 audi
functions.js:9 1
functions.js:8 bmw
functions.js:9 3
functions.js:8 volvo
functions.js:9 0
```

Si tenemos mas de un radio, podemos crear un array y revisar si estan marcados con un if (radio1.checked) console.log(ra.value);

Otra forma de capturar los inputs
```js
let input = Array.from(document.getElementsByTagName('input'));
input = input.filter(inp => inp.type == 'radio');
console.log(input.forEach(elem => console.log(elem.value)));
```


