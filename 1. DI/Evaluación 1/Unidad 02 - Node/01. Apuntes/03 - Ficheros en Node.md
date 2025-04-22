# **Sintaxis Básica**

```js
const fs = require("fs");
```

Esta sintaxis significa:

- **const fs**: Declaramos una variable llamada “fs”.
- **require(“fs”)**: Cargamos un módulo llamado “fs” (File System), que es una caja de herramientas para trabajar con archivos.

---


# **1. Archivos y Directorios**
  
**Concepto:**
- El módulo “fs” nos permite leer, escribir y modificar archivos y carpetas en el ordenador. 

**Ideas clave:**

- **Lectura síncrona:** El programa se detiene hasta que se termina de leer el archivo.
- **Lectura asíncrona:** El programa sigue trabajando mientras se lee el archivo en segundo plano, y al terminar se ejecuta una función que se pasa como parámetro.

---


# **2. Streams y Buffers**

**Concepto:**

- **Buffer:** Es un espacio temporal donde se guarda una pequeña parte de datos.
- **Stream:** Es como una corriente o canal por donde viajan los datos en partes pequeñas en lugar de enviarlos todos de una sola vez.


**Explicación sencilla:**

Imagínate que quieres ver una película en Internet.

- **Buffer:** Es el pequeño trozo de la película que se descarga primero.
- **Stream:** Es el flujo constante de datos que te permite ver la película mientras se descarga, sin tener que esperar a que se descargue completa.
  

**Ideas clave:**

- Los streams permiten trabajar con datos grandes de forma rápida y eficiente, ya que no se carga todo en memoria de una sola vez.
- Esto es muy útil para leer archivos largos o transmitir datos en tiempo real.

---


# **3. Pipes**

**Concepto:**

- El método **pipe()** conecta dos streams. Es decir, permite que los datos que se leen desde una fuente se dirijan automáticamente a un destino.
  

**Explicación sencilla:**

Piensa en un tubo de agua.

- Cuando abres un grifo, el agua sale de una tubería y llega a otro lugar sin que tengas que hacerlo manualmente.
- De la misma manera, **pipe()** toma la “corriente” de datos (stream de lectura) y la envía directamente a otro lugar (stream de escritura), sin que tú tengas que “escuchar” cada fragmento de dato y mandarlo uno por uno.

---

# **Resumen teoría**

- **Módulo fs:** Es la herramienta que te permite trabajar con archivos y carpetas.
- **Buffers y Streams:** Son formas inteligentes de manejar datos que llegan en pequeños trozos, perfectos para trabajar con información grande o para ver vídeos sin esperar a que se descargue todo.
- **Pipes:** Funcionan como tuberías que conectan flujos de datos, facilitando el traslado automático de información de un lugar a otro.

---

# **Ejemplos**:

## **Lectura de Archivos**
---
### Ejemplo Síncrono de Lectura

**Descripción:**
- Se usa la función de lectura sincrona para obtener el contenido de un archivo. La ejecución se bloquea hasta que la operación finaliza.

```js
const fs = require("fs"); // Importamos el módulo fs

try {
  // 'readFileSync' lee el archivo de forma síncrona, devolviendo un valor (el contenido del archivo).
  const contenido = fs.readFileSync("archivo.txt", "utf8");
  console.log("Contenido (síncrono):", contenido);
} catch (error) {
  console.error("Error al leer el archivo (síncrono):", error);
}
```

**Explicación sencilla:**

- Se crea una variable llamada contenido que almacena el valor (texto) leído de “archivo.txt”. Si ocurre un error, se captura y se imprime.

---

### Ejemplo Asíncrono de Lectura

**Descripción:**

- Se usa la función asíncrona para leer el archivo sin bloquear el resto del código. Se pasa una función (callback) para manejar el resultado cuando la operación termine.

```js
const fs = require("fs"); // Importamos el módulo fs

// 'readFile' lee el archivo de forma asíncrona y ejecuta la función callback al finalizar.
fs.readFile("archivo.txt", "utf8", (error, datos) => {
  if (error) {
    console.error("Error al leer el archivo (asíncrono):", error);
  } else {
    console.log("Contenido (asíncrono):", datos);
  }
});
```



**Explicación sencilla:**

- La función readFile toma el nombre del archivo, la codificación y una función callback. Cuando se termina de leer, se invoca el callback y se le pasan un error (si lo hay) y el valor leído, que se muestra por consola.


---

## **Escritura de Archivos**

  

### Ejemplo Síncrono de Escritura

**Descripción:**
Se escribe en un archivo de forma síncrona. La ejecución del programa se pausa hasta que la escritura se completa.


**Código:**

```js
const fs = require("fs"); // Importamos el módulo fs

const texto = "Este es el contenido a escribir de forma síncrona.";

try {
  // 'writeFileSync' escribe en el archivo y bloquea la ejecución hasta terminar.
  fs.writeFileSync("archivo-escrito.txt", texto, "utf8");
  console.log("Archivo escrito (síncrono) con éxito.");
} catch (error) {
  console.error("Error al escribir en el archivo (síncrono):", error);
}
```



**Explicación sencilla:**

Se crea una variable llamada texto con el valor que queremos escribir. La función writeFileSync guarda ese valor en “archivo-escrito.txt”. Si ocurre un error, se muestra en consola.


---

### Ejemplo Asíncrono de Escritura

**Descripción:**

Se escribe en un archivo de forma asíncrona, permitiendo que el programa siga ejecutándose mientras se guarda el archivo. Se utiliza una función callback para confirmar o manejar errores una vez finalizada la escritura.


 **Código:**

```js
const fs = require("fs"); // Importamos el módulo fs

const mensaje = "Este es el contenido a escribir de forma asíncrona.";

// 'writeFile' escribe en el archivo de manera asíncrona y ejecuta una función callback al terminar.
fs.writeFile("archivo-escrito-async.txt", mensaje, "utf8", (error) => {
  if (error) {
    console.error("Error al escribir el archivo (asíncrono):", error);
  } else {
    console.log("Archivo escrito (asíncrono) con éxito.");
  }
});
```



**Explicación sencilla:**

Se usa la función writeFile que escribe el contenido de mensaje en “archivo-escrito-async.txt”. El callback se encarga de mostrar un mensaje o un error una vez que la operación termina.

---

## **Resumen Final**

- **Síncrono:**
    - Las funciones como `readFileSync` o `writeFileSync` bloquean la ejecución del programa hasta que completan su tarea.
    - Se usan cuando el orden es esencial o el archivo es pequeño.

- **Asíncrono:**
    - Las funciones asíncronas como `readFile` o `writeFile` permiten que el programa siga ejecutándose mientras la operación se realiza en segundo plano.
    - Se usan en operaciones que pueden tardar, como leer archivos grandes o acceder a datos remotos.
