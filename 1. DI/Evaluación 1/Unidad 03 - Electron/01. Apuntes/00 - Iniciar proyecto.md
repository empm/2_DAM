# 📦 Crear archivos del proyecto:

1. `index.html`
2. `main.js`
3. `functions.js`

## Main.js (electron)

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

# 🚀 Ejecutar el proyecto:

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
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "electron ."
  },
```

4. Ejecuta el proyecto:

```js
npm start
```

