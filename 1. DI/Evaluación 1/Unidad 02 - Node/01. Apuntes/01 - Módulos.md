## 1. Los módulos en Node

**Concepto:**

- Un módulo es como una caja de herramientas que contiene funciones, variables y objetos que puedes reutilizar en tu proyecto.
- Node.js está dividido en muchos módulos para que solo uses lo que necesites.

**Ejemplo sencillo:**
- Imagina que tienes una caja (módulo) con herramientas para sumar o restar. Si solo necesitas sumar, “abres” la caja y usas solo esa herramienta.

---

## 2. Módulos de núcleo de Node

**Concepto:**

- Los módulos de núcleo son parte del "cerebro" de Node.js. Vienen incluidos cuando instalas Node.js.

- Algunos ejemplos son:
    - **fs:** para trabajar con archivos (leer, escribir, etc.).
    - **http/https:** para crear servidores web.
    - **utils:** que incluyen funciones útiles.

**Sintaxis Básica:**

- Para usar un módulo, usas la función `require` y le pasas una cadena de texto que es el nombre del módulo.

- **Sintaxis genérica:**

```javascript
const modulo = require("nombre_modulo");
```

**Ejemplo:**

```javascript
const fs = require("fs"); // 'fs' es el módulo para archivos
// Usamos una función del módulo fs para leer un archivo
let contenido = fs.readFileSync("archivo.txt", "utf8");
console.log(contenido);
```

---

## 3. Utilizando nuestros propios módulos

**Concepto:**

- Si tu proyecto es grande, es buena idea separar el código en diferentes archivos (módulos).
- Puedes escribir funciones o variables en un archivo y luego exportarlas para usarlas en otro.

**Sintaxis Básica:**

- En el módulo fuente (por ejemplo, _utilidades.js_), usas:
```javascript
// Dentro de utilidades.js
let sumar = (valor1, valor2) => valor1 + valor2;
let restar = (valor1, valor2) => valor1 - valor2;

module.exports = {
	sumar: sumar,
	restar: restar
};
```

- En el módulo donde quieres usar estas funciones (por ejemplo, _principal.js_), importas el módulo:
    
```javascript
// Dentro de principal.js
const utilidades = require("./utilidades");
console.log(utilidades.sumar(3, 2)); // Imprime 5
```


**Explicación sencilla:**

- En _utilidades.js_ defines la función (la herramienta), la asignas a una variable y luego la exportas usando `module.exports`.
- Luego, en _principal.js_ se "abre" la caja usando `require` para poder usar la función.

---

## 4. Módulos de terceros: NPM

**Concepto:**

- NPM es un gestor de paquetes que te permite descargar módulos (o librerías) que otros han creado y que pueden hacer tareas específicas.
- Con NPM puedes agregar fácilmente nuevas herramientas a tu proyecto sin escribirlas tú mismo.


**Ejemplo:**

- Imagina que necesitas una herramienta para ordenar números. En vez de escribir la función, puedes instalar un módulo llamado “lodash” que la tiene.

- **Sintaxis básica para instalar un módulo:**

```bash
npm install nombre_modulo
```

Por ejemplo:

```bash
npm install lodash
```

- Luego, en tu código:

```javascript
const _ = require("lodash");
console.log(_.difference([1, 2, 3], [1])); // Imprime [2, 3]
```


---

## 5. Instalar módulos locales a un proyecto

**Concepto:**

- Cuando instalas un módulo con NPM, se agrega en la carpeta del proyecto llamada **node_modules** y también se registra en un archivo llamado _package.json_.
- _package.json_ actúa como una lista de ingredientes (dependencias) de tu proyecto.

**Pasos básicos:**

1. Inicia tu proyecto con:
```bash
npm init
```

Esto crea el archivo _package.json_ y te pide valores como nombre, versión, etc.

2. Instala un módulo localmente:

```bash
npm install nombre_modulo
```

---

## 6. Instalar módulos globales al sistema

**Concepto:**

- Algunos módulos se usan en la línea de comandos (terminal) y deben estar disponibles en todo el sistema, no solo en un proyecto.
- Para instalarlos de forma global se usa un flag especial.

**Sintaxis Básica:**

```bash
npm install -g nombre_modulo
```

- **-g** significa “global” (para todo el sistema).


**Ejemplo:**
- Por ejemplo, para instalar un comprobador de sintaxis llamado JSHint:
```bash
npm install -g jshint
```

**Nota importante:**

- Los módulos instalados globalmente NO se pueden requerir con `require` en un proyecto, a menos que también se instalen localmente.

---
### Resumen

- **Módulos en Node:** Son cajas de herramientas con funciones y variables.

- **Módulos de núcleo:** Vienen incluidos con Node.js (usamos `require("nombre")` para acceder).

- **Propios módulos:** Se crean tus propios archivos para organizar el código y se exportan usando `module.exports`.

- **Módulos de terceros y NPM:** Puedes descargar herramientas creadas por otros para ayudarte en el proyecto.

- **Instalación local y global:** Instalar localmente añade dependencias a _package.json_; instalar globalmente es para herramientas de terminal.
