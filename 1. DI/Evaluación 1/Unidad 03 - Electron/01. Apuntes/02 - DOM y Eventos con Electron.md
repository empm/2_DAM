
## **🧱 ¿Qué es el DOM?**

> El **DOM (Document Object Model)** es como un mapa en forma de árbol que representa todo lo que hay en una página web: texto, botones, imágenes, etc.

- Cada **etiqueta HTML** es un “nodo” en ese árbol.
- El nodo principal es `document`, y desde ahí accedemos a todo lo demás.

---


## 🧪 Acceder a Elementos HTML

### Sintaxis Básica:

```js
const nombreElemento = document.getElementById("id_del_elemento");
```

### Ejemplo:

```js
let mDiv = document.getElementById("datos");
mDiv.innerHTML = "<p> Contenido del div </p>";
```

Esto busca un elemento con `id="datos"` y le coloca un párrafo de texto dentro.

---


## **➕ Crear y Añadir Elementos (como botones)**

### ** Sintaxis Básica:**

```js
const nuevoElemento = document.createElement("tipo");
nuevoElemento.textContent = "Texto del botón";
padre.appendChild(nuevoElemento);
```

### ** Ejemplo real:**

```js
let button = document.createElement("button");
button.textContent = "Botón";
document.body.appendChild(button);
```
  
---


## **🧪 Proyecto básico en Electron**

  
Creamos un proyecto con estos archivos:

- `main.js`: arranca la ventana de Electron.
- `index.html`: contiene el HTML con `<div id="datos">`.
- `functions.js`: se encarga de manipular el DOM.  

### Código básico del `main.js`

```js
const { app, BrowserWindow } = require("electron");

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.setMenu(null);
  mainWindow.loadFile("index.html");
}

app.whenReady().then(createWindow);
```
  
---


## **⚙️ Introducción a Eventos**

> Cuando haces clic en un botón, o presionas una tecla, eso se llama **evento**.
> Para que tu código reaccione a esos eventos, debes decirle qué hacer cuando ocurran.

### Sintaxis Básica:

```js
elemento.addEventListener("evento", () => {
  // acción que queremos ejecutar
});
```

### Ejemplo con evento 

### **click:**

```js
let mDiv = document.getElementById("datos");
mDiv.innerHTML = "<p> Contenido del div </p>";

let button = document.createElement("button");
button.textContent = "Button";
document.body.appendChild(button);

button.addEventListener("click", () => {
  alert("¡Has hecho clic en el botón!");
});
```

---


## **📦 Ejecutar el proyecto:**

1. Inicializa el proyecto:
```js
npm init
```

2. Instala Electron:

```js
npm install --save electron
```

3. En `package.json`, añade este script:

```js
"scripts": {
  "start": "electron ."
}
```

4. Ejecuta el proyecto:

```js
npm start
```

---


## **✅ Resumen**

- El **DOM** es la estructura que representa tu HTML.
    
- Puedes **acceder** a elementos con getElementById().
    
- Puedes **crear elementos** con createElement() y **añadirlos** con appendChild().
    
- Puedes **escuchar eventos** como clics usando addEventListener().