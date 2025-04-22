# **Sintaxis Básica**

```js
const fs = require("fs");
```

_Explicación:_

- Declaramos una variable llamada **fs** que carga (require) el módulo “fs”, el cual nos da herramientas para trabajar con archivos.

---

# **Lectura de Archivos JSON**

**Concepto:**

Imagina que tienes un libro lleno de datos (un archivo JSON) y quieres leer sus páginas. Para leerlo, usamos funciones que nos permiten abrir el libro, leer su contenido y convertirlo en algo que nuestro programa pueda entender.


**Pasos Básicos:**

1. **Leer el archivo:**
	- Usamos una función (por ejemplo, `readFileSync`) para abrir el libro y leer todo su contenido.

2. **Convertir el contenido:**

	- El contenido leído es solo un texto. Utilizamos una función (por ejemplo, `JSON.parse`) para transformar ese texto en una lista (array) de datos que nuestro programa puede usar.



**Sintaxis Genérica:**

```js
// Leer el archivo y guardar el contenido en una variable
const contenidoFichero = fs.readFileSync("ruta/al/archivo.json", "utf8");

// Convertir el contenido en un array de objetos
let datos = JSON.parse(contenidoFichero);
```

**Ejemplo Explicado:**

- **función:** fs.readFileSync abre y lee el archivo.
- **variable:** contenidoFichero guarda el texto del archivo.
- **función:** JSON.parse convierte ese texto en un valor (por ejemplo, un array).
- **variable:** datos es el resultado final (la lista de datos).

  
**Nota Adicional:**

También puedes cargar un archivo JSON de forma directa usando require así:

```js
const datos = require("./clientes.json");
```

Pero esto solo funciona para lectura, no para escribir cambios en el archivo.

---


# **Escritura en Archivos JSON**
 

**Concepto:**

Escribir en un archivo JSON es como reescribir o actualizar el libro con nueva información. Primero, preparamos los datos en nuestro programa y luego los convertimos en una cadena de texto que se guarda en el archivo.

  
**Pasos Básicos:**

1. **Preparar los datos:**
    
    Por ejemplo, modificar un array de datos.

2. **Convertir los datos a texto:**
    
    Usamos una función (por ejemplo, JSON.stringify) para transformar nuestros datos en una cadena que se pueda escribir en el archivo.

3. **Escribir en el archivo:**
    
    Usamos una función (por ejemplo, writeFileSync) para guardar ese texto en el archivo.



**Sintaxis Genérica:**

```js
const fs = require("fs");

// leemos archivo
const contenidoLibro = fs.readFileSync("../data/books.json", "utf8");
// convertir a array
const convertirArray = JSON.parse(contenidoLibro);
// convertir a texto
let convertirTexto = JSON.stringify(convertirArray);
// guardar fichero
fs.writeFileSync("nuevo.json", datos, "utf8"); 
```

**Ejemplo Explicado:**

- **función:** JSON.stringify toma la variable **datos** y la convierte en un texto (cadena).
    
- **variable:** textoDatos contiene esa cadena.
    
- **función:** fs.writeFileSync escribe ese texto en el archivo.


---

# **Resumen Final**

- **Lectura de JSON:**
    
    - Usamos fs.readFileSync para leer el archivo.
        
    - Convertimos el texto leído a datos con JSON.parse.
        
    
- **Escritura de JSON:**
    
    - Convertimos nuestros datos a una cadena con JSON.stringify.
        
    - Guardamos la cadena en el archivo con fs.writeFileSync.
  