
# **1. Lectura del Fichero y Conversión a Vector**

  **Concepto:**

Leer un fichero JSON es como abrir un libro y convertir su contenido (texto) en una lista (array) de datos que el programa puede usar.

  
**Sintaxis Básica:**

```js
const contenidoFichero = fs.readFileSync("ruta/al/fichero.json", "utf8");
const vectorDatos = JSON.parse(contenidoFichero);
```

**Función de Lectura:**

```js
function leerFichero(ruta) {
  // 'contenido' es el texto leído del fichero
  const contenido = fs.readFileSync(ruta, "utf8");
  // Convertimos el texto en un vector (array) de objetos
  return JSON.parse(contenido);
}

// Comprobación:
let vectorBooks = leerFichero("./data/books.json");
console.log("Vector de libros:", vectorBooks);
```

  

---

# **2. Guardar Fichero**

  
**Concepto:**

Guardar el fichero es como escribir o actualizar el libro con la lista de datos. 
Primero, convertimos el vector (array) a una cadena y luego lo escribimos en el fichero.
  

**Sintaxis Básica:**

```js
const textoDatos = JSON.stringify(vectorDatos);
fs.writeFileSync("ruta/al/fichero.json", textoDatos, "utf8");
```

**Función de Guardado:**

```js
function guardarFichero(ruta, vectorDatos) {
  const textoDatos = JSON.stringify(vectorDatos, null, 2); // con formato legible
  fs.writeFileSync(ruta, textoDatos, "utf8");
  console.log("Fichero guardado correctamente.");
}

// Comprobación:
guardarFichero("./data/books.json", vectorBooks);
```

  

---

# **3. Añadir, Eliminar y Modificar**

  

**Concepto:**

- **Añadir:** Agregar un nuevo objeto al vector.
    
- **Eliminar:** Quitar un objeto del vector (por ejemplo, utilizando una propiedad única como “title”).
    
- **Modificar:** Cambiar datos de un objeto existente, buscándolo por un criterio.
    

  

**Funciones de Ejemplo:**

  

_Añadir:_

```js
function anadirElemento(vector, nuevoElemento) {
  // Si queremos que el teléfono (o cualquier otro campo) no se repita, podemos comprobarlo.
  // Aquí se añade sin validación.
  vector.push(nuevoElemento);
  console.log("Elemento añadido:", nuevoElemento);
  return vector;
}
```

_Eliminar (por título):_

```js
function eliminarElemento(vector, titulo) {
  // Filtramos el vector quitando el elemento cuyo campo "title" coincida con el título dado.
  const nuevoVector = vector.filter((elemento) => elemento.title !== titulo);
  console.log("Elemento eliminado con título:", titulo);
  return nuevoVector;
}
```

_Modificar (por título):_

```
function modificarElemento(vector, titulo, nuevosDatos) {
  // Buscamos el elemento cuyo "title" es igual al título dado
  let modificado = false;
  vector.forEach((elemento) => {
    if (elemento.title === titulo) {
      // Para cada propiedad en nuevosDatos, actualizamos el elemento
      for (let propiedad in nuevosDatos) {
        elemento[propiedad] = nuevosDatos[propiedad];
      }
      modificado = true;
      console.log("Elemento modificado con título:", titulo);
    }
  });
  if (!modificado) {
    console.log("No se encontró el elemento con título:", titulo);
  }
  return vector;
}
```

**Comprobación Ejemplo:**

```
// Ejemplo de nuevo libro a añadir
const nuevoLibro = {
  title: "La magia del orden",
  author: "Marie Kondo",
  price: "20",
  img: "mk.jpg",
  eslibro: true
};

// Añadir el nuevo libro
vectorBooks = anadirElemento(vectorBooks, nuevoLibro);
console.log(vectorBooks);

// Eliminar un libro (por ejemplo, "Watchmen" se considera cómic)
vectorBooks = eliminarElemento(vectorBooks, "Watchmen");
console.log(vectorBooks);

// Modificar un elemento (cambiar precio de "Q")
vectorBooks = modificarElemento(vectorBooks, "Q", { price: "25" });
console.log(vectorBooks);

// Guardar cambios en el fichero
guardarFichero("./data/books.json", vectorBooks);
```

  

---

# **4. Ver Libros**

  

**Concepto:**

Ver libros implica filtrar el vector y mostrar solo aquellos elementos que son libros.

Normalmente, se usa una propiedad como “eslibro” o “libro” para indicar si es un libro (true) o no (false).

En este ejemplo, consideraremos que un elemento es libro si tiene la propiedad eslibro igual a true o, si no existe, si la propiedad libro es true.

  

**Función para Ver Libros:**

```
function verLibros(vector) {
  const libros = vector.filter((elemento) => {
    if (typeof elemento.eslibro !== "undefined") {
      return elemento.eslibro === true;
    } else if (typeof elemento.libro !== "undefined") {
      return elemento.libro === true;
    }
    return false; // Si no tiene ninguna de estas propiedades, no lo consideramos
  });
  console.log("Libros:", libros);
  return libros;
}

// Comprobación:
verLibros(vectorBooks);
```

  

---

# **5. Ver Cómics**

  

**Concepto:**

Ver cómics es similar a ver libros, pero se filtra para obtener aquellos elementos en que la propiedad indica que NO son libros.

En este ejemplo, se supone que un cómic es aquel en que eslibro es false.

  

**Función para Ver Cómics:**

```
function verComics(vector) {
  const comics = vector.filter((elemento) => {
    if (typeof elemento.eslibro !== "undefined") {
      return elemento.eslibro === false;
    }
    return false; // Si no tiene la propiedad, no lo consideramos cómic
  });
  console.log("Cómics:", comics);
  return comics;
}

// Comprobación:
verComics(vectorBooks);
```

  

---

# **Resumen Final**

- **Lectura de fichero:** Con fs.readFileSync y JSON.parse convertimos el fichero a un vector (array).
    
- **Guardar fichero:** Con JSON.stringify y fs.writeFileSync escribimos el vector en el fichero.
    
- **Añadir, eliminar y modificar:** Creamos funciones para agregar un nuevo elemento, quitar uno según un criterio (por ejemplo, título) o modificar datos de un elemento.
    
- **Ver libros y cómics:** Filtramos el vector usando propiedades (como eslibro) para mostrar únicamente libros o cómics.
    

  

Estos apuntes usan un lenguaje natural y ejemplos sencillos, con nombres genéricos (función, variable, valor, retorno), para que se entienda fácilmente incluso a un niño. Puedes copiar y pegar estos apuntes en Obsidian para tenerlos siempre a mano.

5. Ficheros JSONconNode.pdf](file-service://file-WUfJHe9joFKJqBbq7PSp8D)