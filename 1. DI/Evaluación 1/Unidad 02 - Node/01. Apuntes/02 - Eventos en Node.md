# **Sintaxis Básica**

```js
const modulo = require("nombre_modulo");
const emisor = new modulo.EventEmitter();
```

# **1. Eventos en Node**
  
**Concepto:**

En Node.js, muchos objetos pueden emitir “eventos”. 
Un evento es como un aviso o señal que dice “¡Ocurrió algo!”

- Imagina que tienes una campana: cada vez que alguien toca la campana, suena un “ping”.
    
- De forma similar, un objeto en Node puede emitir un evento para notificar que algo sucedió, por ejemplo, cuando se abre un archivo o se establece una conexión.
  

# **2. Módulo de Eventos**

**Concepto:**

Para trabajar con eventos en Node, usamos un módulo especial llamado “events”.

- Con este módulo, creamos objetos llamados _emisor de eventos_ que pueden enviar avisos.
    
- Usamos require("events") para cargar este módulo en nuestro código.
  

**Sintaxis Básica del módulo de eventos:**

```js
const events = require("events");
const EmisorEventos = events.EventEmitter;
```


# **3. Definir un Evento**

**Concepto:**

Definir un evento es como decir “cuando ocurra X, quiero hacer algo”.

- Se crea un objeto emisor a partir de la clase EventEmitter.
    
- Con el método `on()` (o `addEventListener()`), le decimos al objeto qué hacer cuando ocurra un evento.
    
- Cuando ocurre el evento, se ejecuta una función (llamada `callback` o manejador de eventos).
  

**Sintaxis de definir un evento:**

```js
const miEmisor = new EmisorEventos();
// Para escuchar un evento llamado "eventoX":
miEmisor.on("eventoX", (valor) => {
	// Código a ejecutar cuando ocurra el evento
});

// Para emitir (lanzar) el evento "eventoX":
miEmisor.emit("eventoX", "valor_o_dato");
```


# **4. Asociación de Eventos a Objetos**

**Concepto:**

No solo podemos emitir eventos desde objetos simples, sino que también podemos crear objetos (por ejemplo, una persona o un servidor) que tengan su propio “sensor” de eventos.

- Esto se hace mediante la herencia: el objeto se “hereda” la capacidad de emitir y responder a eventos.
    
- De esta forma, cada objeto puede avisar cuando algo importante sucede, y podemos asociar funciones específicas para manejar esos avisos


**Idea general:**

- Piensa en un objeto como un robot que puede tener botones para avisar de cosas. Cada vez que presionas un botón, el robot envía un aviso (evento) y se activa una acción especial (callback).