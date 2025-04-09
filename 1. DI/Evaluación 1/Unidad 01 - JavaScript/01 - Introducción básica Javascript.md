# Frameworks

> Un framework es un **conjunto de software (librerías, funciones, módulos,…)** que funcionan con un determinado lenguaje de programación. Existen frameworks para java, c, etc. Por supuesto también para node. Es conveniente aclarar que todo puede ser hecho sin framewoks y partir de cero pero permiten que la programación sea más productiva. 

JavaScript tiene multitud de frameworks que facilitan la creación de aplicaciones de muchos tipos. Algunos muy usados:
- **Express**: permite crear servidores y servicios web.
- **Ionic**: para crear aplicaciones móviles híbridas.
- **Electron**: para desarrollar aplicaciones de escritorio que
se puedan ejecutar en windows, OS o linux.
- **Framework** del lado **cliente**: para diseñar la parte cliente
de una aplicación web, hay muchos: angular, vue, etc.

# Electron

>Electron lo que hace es envolver aplicaciones desarrolladas con tecnologías web para que se pueden ejecutar como app de escritorio multiplataforma.

## Instalación

Electrón se instala como un módulo mediante **npm**. 
Como todos los módulos de node, para trabajar con electron podemos usar dos vías: 
- instalarlo globalmente en el ordenador
- instalarlo localmente en la carpeta de un proyecto node
  (se instala en la carpeta `node-modules`). 

Vamos instalarlo de forma local, dentro de nuestra carpeta de proyecto se usa el comando:

```javascript
npm install electron
````

Reconstruir la carpeta `node-modules`.

```JavaScript
npm install
```

# Crear aplicaciones ejecutables

Bajamos desde github: https://github.com/electron/electron-quick-start

# Integrar JavaScript en HTML

## 1. Integrarlo dentro de HTML por etiqueta `<script/>`

```html
<html>
<head>
    <title>Document</title>
</head>
<body>
    <p>Hola Mundo!</p>
    <script>
        console.log("Hola Mundo!");
    </script>
</body>
</html>
```

## 2. Un archivo separado

```html
<!-- index.html -->
<html>
<head>
    <title>Document</title>
</head>
<body>
    <p>Hola Mundo!</p>
    <script src="ejemplo.js"></script>
</body>
</html>
```

```js
// ejemplo.js
console.log("Hola Mundo!");
```

# JavaScript con node

> Node.js es un entorno de ejecución en el lado del servidor construido utilizando el motor Javascript de Google Chrome, llamado V8.

Lo que se hace es **utilizar de manera externa** el mismo **motor de ejecución** que emplea Google **Chrome** para c**ompilar y ejecutar Javascript** en el navegador: el motor V8.
Dicho motor se encarga de compilar y ejecutar el código Javascript, transformándolo en código más rápido (código máquina).

También se encarga de colocar los elementos necesarios en memoria, eliminar de ella los elementos no utilizados (garbage collection), etc.

## Instalar node

Node puede descargarse desde la web: https://nodejs.org/es/

## Ejecutar node

Desde terminal, situándonos sobre un archivo `.js` ejecutamos:

```bash
node ejemplo1.js
```

> Nos ejecuta  el contenido en la terminal


# Proyectos con node

## NPM

> npm es el sistema de gestión de paquetes por defecto para Node.js

## Iniciar un proyecto en node

> Lo habitual cuando se trabaja con node es tener una **carpeta que contendrá el proyecto.** 

Para **iniciar un proyecto** usaremos **npm**: 
1. Crea una carpeta en la ubicación que desees, dale un nombre sin espacios en blanco. 
2. Después accede a la carpeta desde tu consola o terminal y ejecuta el siguiente comando: 

```bash
   npm init
   ```

> El comando anterior genera un archivo package.json personalizado para cada proyecto node.

En el apartado de `scripts` podemos añadir `"start": "node ."`para que al ejecutar el comando `npm start` nos ejecute el proyecto.

```json
{
  "name": "ej1",
  "version": "1.0.0",
  "description": "Primer proyecto",
  "license": "ISC",
  "author": "",
  "type": "commonjs",
  "main": "ejemplo1.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node ."
  }
}
```


## Ejecutar un proyecto en node

```bash
npm start
```

