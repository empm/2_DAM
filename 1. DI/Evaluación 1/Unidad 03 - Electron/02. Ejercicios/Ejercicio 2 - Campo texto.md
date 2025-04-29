# Parte 1

> Mostrar una alerta con el valor del campo de texto, al presionar el botón

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campo texto</title>
</head>
<body>

    <div id="etiquetas">
        <label for="texto">Campo de texto HTML</label>
        <input type="text" name="texto" id="texto">
        <input type="button" value="Boton" id="boton">        
    </div>
    <div id="muestra"></div>
    
    <script src="functions.js"></script>    
</body>
</html>
```

### `functions.js`

```js
// Asignar variable
let texto = document.getElementById("texto");

let button = document.getElementById("boton");
button.addEventListener('click', () => {
    // Texto.value para obtener su valor
    alert(texto.value);
});
```

# Parte 2 - Eventos de teclado

```js
// Asignar variable
let texto = document.getElementById("texto");

let button = document.getElementById("boton");
button.addEventListener("click", () => {
  // Texto.value para obtener su valor
  alert(texto.value);
});
let muestra = document.getElementById("muestra");

texto.addEventListener("keyup", (evento) => {
  if (evento.key == "Enter") {
    // alert("Enter!");
    muestra.innerHTML = texto.value;
  }
});
```