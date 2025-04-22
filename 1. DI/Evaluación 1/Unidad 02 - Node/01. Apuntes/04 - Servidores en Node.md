
# **Sintaxis Básica**

```js
const http = require("http");
const fs = require("fs");
```

_Explicación:_

- Declaramos una variable (por ejemplo, **http**) que carga un módulo con require("nombre_modulo").
- Esto nos da acceso a herramientas para, por ejemplo, crear un servidor o manejar archivos

  
# **1. Servidores en Node**

**Concepto:**

Un servidor es como una tienda que está siempre abierta esperando pedidos de sus clientes.

- Cuando un cliente (como un navegador) hace una petición, el servidor la recibe y le devuelve una respuesta.
- La comunicación se hace usando reglas llamadas protocolos (por ejemplo, TCP) y mediante “canales” (puertos).
  

**Sintaxis básica para crear un servidor:**

```js
const servidor = http.createServer((peticion, respuesta) => {
  // Aquí va el código que maneja lo que se hace cuando llega un pedido
});
servidor.listen(puerto, "IP");
```

_Explicación:_

- **http.createServer((peticion, respuesta) => { … })**: Crea la tienda (servidor) y le dice lo que debe hacer cuando llega un pedido.

- **servidor.listen(puerto, “IP”)**: Hace que el servidor esté “abierto” en un número de puerto y una dirección IP (por ejemplo, 3000 y 127.0.0.1).

  

**Ejemplo simple de servidor:**

```js
const http = require("http");

const servidor = http.createServer((peticion, respuesta) => {
  respuesta.writeHead(200, { "Content-Type": "text/plain" });
  respuesta.end("Hola, este es mi servidor!");
});

servidor.listen(3000, "127.0.0.1");
```

_Explicación:_

- Cuando visitas http://127.0.0.1:3000, el servidor responde con el mensaje “Hola, este es mi servidor!”.
  

# **2. Sirviendo JSON**

**Concepto:**

> JSON es una manera de escribir datos en forma de “caja de mensajes” fácil de entender.

- Se usa para enviar datos entre el servidor y el cliente, como enviar la lista de tus juguetes favoritos.
- Para que el navegador sepa qué hacer, el servidor cambia el tipo de contenido en la respuesta.  


**Sintaxis básica para servir JSON:**

```js
respuesta.writeHead(200, { "Content-Type": "application/json" });
respuesta.end(JSON.stringify(objeto));
```


_Explicación:_

- **“Content-Type”: “application/json”**: Le dice al cliente que el contenido es un JSON.
- **JSON.stringify(objeto)**: Convierte un objeto (la caja de datos) en una cadena de texto para enviarla.
  

**Ejemplo simple de servidor sirviendo JSON:**

```js
const http = require("http");

const datos = { mensaje: "Hola, soy JSON", numero: 123 };

const servidor = http.createServer((peticion, respuesta) => {
  respuesta.writeHead(200, { "Content-Type": "application/json" });
  respuesta.end(JSON.stringify(datos));
});

servidor.listen(3000, "127.0.0.1");
```

_Explicación:_

- Cuando visitas la dirección del servidor, el navegador recibe la caja de datos con el mensaje y el número, y puede interpretarlos correctamente.  


# **Resumen Final**

- **Módulos:** Usamos require("nombre_modulo") para cargar herramientas como http o fs.

- **Servidores en Node:** Son “tiendas” que esperan pedidos de clientes y responden usando métodos como createServer y listen.

- **Sirviendo JSON:** Permite enviar datos estructurados en forma de “caja de mensajes” al cliente, usando JSON.stringify y ajustando los encabezados.