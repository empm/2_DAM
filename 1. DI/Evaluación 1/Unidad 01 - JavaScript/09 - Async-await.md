> Async/await es una forma de escribir código asíncrono de manera que se parezca a un código síncrono, facilitando la lectura y el manejo de resultados.
### Concepto General

- **Función asíncrona (async function):**  
    Una _función_ declarada con la palabra clave `async` siempre devuelve una _promesa_ (promise). Esto significa que, sin importar lo que haga la función, su valor devuelto se encapsula en una promesa.
    
- **Esperar (await):**  
    La palabra `await` se utiliza dentro de una función asíncrona para "pausar" la ejecución de esa _función_ hasta que se resuelva una _promesa_. Durante ese tiempo, la ejecución de la función se suspende, pero el resto del programa continúa ejecutándose.
    

---

### Sintaxis Genérica

**Definición de una función asíncrona:**

```javascript
async function nombreDeLaFuncion(valor) {
  // La función siempre retorna una promesa
  let variable = await promesa; // 'await' espera a que 'promesa' se resuelva y asigna el valor resultante a 'variable'
  return variable; // El valor retornado se envuelve automáticamente en una promesa
}
```

---

### Ejemplo 1: Código Básico con Async/Await

Imagina que tienes una _función_ que simula una operación asíncrona (por ejemplo, un cálculo o una llamada a una API). La función retornará un _valor_ después de un tiempo simulado.

```javascript
function operacionAsincrona(valor) {
  return new Promise((resolve, reject) => {
    // Simula una demora de 1 segundo
    setTimeout(() => {
      // Si el valor es par, resuelve la promesa con valor/2, de lo contrario la rechaza
      if (valor % 2 === 0) {
        resolve(valor / 2);
      } else {
        reject("El valor no es par");
      }
    }, 1000);
  });
}

async function ejecutarOperacion() {
  try {
    // 'await' suspende la ejecución hasta que 'operacionAsincrona' se resuelva y asigna el resultado a 'resultado'
    let resultado = await operacionAsincrona(4);
    console.log("Resultado:", resultado); // Muestra 2
  } catch (error) {
    console.error("Error:", error);
  }
}

ejecutarOperacion();
```

- Otra forma de escribirlo:

```js
let half = (num) => {
  return new Promise((resolve, reject) => {
    if (num % 2 == 0) {
      resolve(num / 2);
    } else {
      reject("no es par");
    }
  });
};

half(5).then(result => console.log(result)).catch(err => console.log(err));
```


**Explicación:**

- **operacionAsincrona(valor):**  
    Una función que retorna una _promesa_. Usa `setTimeout` para simular una demora y, según una condición, llama a `resolve(valor / 2)` o `reject("El valor no es par")`.
    
- **ejecutarOperacion():**  
    Una _función asíncrona_ que utiliza `await` para esperar a que se resuelva la promesa de `operacionAsincrona`. Se utiliza un bloque `try/catch` para manejar posibles errores.
    

---

### Ejemplo 2: Uso de Async/Await con Fetch

Cuando haces una llamada a un servidor, la API `fetch` retorna una _promesa_. Con `await` puedes esperar a que esa promesa se resuelva y obtener los datos.

```javascript
async function obtenerDatos(url) {
  try {
    // Espera a que se complete la llamada a 'fetch'
    let respuesta = await fetch(url);
    // Espera a que se convierta la respuesta en JSON
    let datos = await respuesta.json();
    console.log("Datos recibidos:", datos);
  } catch (error) {
    console.error("Error al obtener datos:", error);
  }
}

// Ejemplo de llamada (asegúrate de usar una URL válida)
obtenerDatos("https://api.example.com/data");
```

**Explicación:**

- **fetch(url):**  
    Realiza una petición a una _URL_ y retorna una _promesa_.
    
- **await fetch(url):**  
    La ejecución de la función se detiene hasta que fetch se resuelva.
    
- **await respuesta.json():**  
    Convierte la respuesta a un objeto _JSON_ de manera asíncrona y espera a que se complete.
    

---

### Resumen

- **async:**  
    Marca una función para que siempre retorne una promesa.
    
- **await:**  
    Se usa dentro de funciones asíncronas para esperar a que se resuelva una promesa, asignando su resultado a una variable.
    
- **try/catch:**  
    Permite manejar los errores que pueden surgir al usar `await`, similar a como se manejan excepciones en funciones sincrónicas.
    

