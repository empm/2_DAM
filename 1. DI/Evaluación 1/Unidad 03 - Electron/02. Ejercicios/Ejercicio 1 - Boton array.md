Crea un proyecto electron que muestre la siguiente ventana:
![[Pasted image 20250422064325.png]]
Los datos que muestra saldrán de un array definido en el fichero de funciones:  

```js
let nombre = ["Nombre 1", "Nombre 2", "Nombre 3","Nombre 4"];  
```

Para mostrar el contenido del vector con ese aspecto puedes recorrer el vector e ir concatenando a una variable string el contenido del vector más un salto de línea:  

```js
s += nombre[i] + "<br>";  
```

Cuando ya se han concatenado todo se asigna a la propiedad innerHTML del div.

---
# Resuelto:

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 1</title>
   </head>
<body>
    <h1>Hello Array!</h1>
    <div id="datos"></div>
    <script src="functions.js"></script>
</body>
</html>
```

### `main.js`

```js
const { app, BrowserWindow } = require("electron");
function createWindow() {
  let win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });
  win.loadFile("index.html");
}
app.on("ready", createWindow);
```

### `functions.js`

```js
let nombre = ["Nombre 1", "Nombre 2", "Nombre 3", "Nombre 4"];

let vectorDatos = document.getElementById("datos");

let button = document.createElement("button");
button.textContent="Open Window";

//vectorDatos.appendChild(button);
/*
Si lo haces de esta forma, el boton desaparece
*/
document.body.appendChild(button);
/*
Si lo haces de esta forma, el boton se mantiene al hacer click
*/

let index = "";

button.addEventListener("click", () => {
   for (let i = 0; i < nombre.length; i++) {
    index += nombre[i] + "<br>";
   }
   vectorDatos.innerHTML = index;
});
```

