# Promesas

**Concepto:**  
Las promesas permiten manejar operaciones asíncronas devolviendo un resultado exitoso (resolve) o un error (reject).

> Se emplean para definir la finalización (exitosa o no) de una operación asíncrona.

**Ejemplo de Creación y Consumo de Promesa:**

```javascript
let datos = [
  { nombre: "Nacho", telefono: "966112233", edad: 40 },
  { nombre: "Ana", telefono: "911223344", edad: 35 },
  { nombre: "Mario", telefono: "611998877", edad: 15 },
  { nombre: "Laura", telefono: "633663366", edad: 17 }
];

let promesaMayoresDeEdad = new Promise((resolve, reject) => {
  let resultado = datos.filter(persona => persona.edad >= 18);
  if (resultado.length > 0) {
    resolve(resultado);
  } else {
    reject("No hay resultados");
  }
});

promesaMayoresDeEdad
  .then(result => {
    console.log("Coincidencias encontradas:");
    console.log(result);
  })
  .catch(error => {
    console.log("Error:", error);
  });
```

> **Anotación:** Se filtran datos y, si hay coincidencias, se llama a _resolve_; si no, a _reject_. Se utilizan `.then()` y `.catch()` para manejar el resultado o error.

---

## Crear una promesa.

> En el caso de que queramos o necesitemos crear una promesa, se creará un objeto de tipo `Promise`. 

A dicho objeto se le pasa como parámetro una función con dos parámetros:
- La función callback a la que llamar si todo ha ido correctamente
- La función callback a la que llamar si ha habido algún error 

Estos dos parámetros se suelen llamar, respectivamente, `resolve y reject`. 

Por lo tanto, un esqueleto básico de promesa, empleando `arrow functions` para definir la función a ejecutar, sería así: 

```js
let nombreVariable = new Promise((resolve, reject) => { 
// Código a ejecutar 
// Si todo va bien, llamamos a "resolve" 
// Si algo falla, llamamos a "reject" 
});
```

---

## Consumir una promesa

> En el caso de querer utilizar una promesa previamente definida (o creada por otros en alguna librería), simplemente llamaremos a la función u objeto que desencadena la promesa, y recogemos el resultado. 

- Para recoger un resultado satisfactorio `resolve` empleamos la cláusula `then`.
- Para recoger un resultado erróneo `reject` empleamos la cláusula `catch`.

```js
promesaMayoresDeEdad(datos).then(resultado => { 
// Si entramos aquí, la promesa se ha procesado bien 
// En "resultado" podemos acceder al resultado obtenido 
	console.log("Coincidencias encontradas:");
	console.log(resultado); 
}).catch(error => { 
// Si entramos aquí, ha habido un error al procesar la promesa 
// En "error" lo podemos consultar 
	console.log("Error:", error); 
});
```

---

# Utilidad de una promesa

> Una promesa en JavaScript representa un valor que puede estar disponible ahora, en el futuro o nunca. 

Su utilidad se nota especialmente en operaciones asíncronas. 
Por ejemplo, cuando haces una petición a un servidor o lees un archivo, no sabes cuánto tiempo tardará en completarse la operación. En vez de bloquear el programa esperando el resultado, una promesa te permite “prometer” que, cuando la operación termine, se ejecutará una función para manejar el éxito (resolve) o el fallo (reject).  

Aunque en el ejemplo de la moneda parezca que solo imprimes un resultado (cara o cruz), el uso de promesas permite:

- **Encadenar operaciones:** Puedes usar .then() para procesar el resultado y luego encadenar otras tareas sin anidar callbacks.    
- **Manejo centralizado de errores:** Usas .catch() para atrapar cualquier fallo, lo que facilita el manejo de errores de manera uniforme.    
- **No bloquear el hilo principal:** La promesa se ejecuta en segundo plano, permitiendo que el programa siga funcionando mientras esperas el resultado.  

La promesa es una abstracción que te ayuda a gestionar procesos asíncronos de forma más limpia y escalable, algo muy útil en aplicaciones reales donde muchas operaciones dependen de respuestas de recursos externos (como servidores, archivos, etc.).