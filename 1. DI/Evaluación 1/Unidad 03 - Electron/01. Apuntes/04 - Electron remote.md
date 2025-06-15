```bash
npm install @electron/remote
```

## Main:
```js
require('@electron/remote/main').initialize()
require('@electron/remote/main').enable(mainWindow.webContents)
```

## Functions

```js
const {dialog} = require('@electron/remote')

dialog.showMessageBox({
	type: '',
	title: '',
	message: ''
})
```

Para que no bloquee la ejecución al mostrar un dialog y lo puedas hacer mas de una vez