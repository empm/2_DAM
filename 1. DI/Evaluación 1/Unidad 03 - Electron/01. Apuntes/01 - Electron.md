# Instalar Electron de manera local

```js
npm install electron
```

# Instalar Electron de manera global

```js
npm install electron -g
```

# Arquitectura básica

![[Pasted image 20250417073110.png]]

**Main Process** 
Este proceso es el punto de entrada de Electron y se encarga de manejar las páginas web que vamos a mostrar de nuestra aplicación desplegándolas en ventanas de navegador.

**Renderer Process**
Es la instancia que muestra el contenido de nuestra aplicación web. Por tanto posee acceso a la API de nuestro DOM y el navegador.
