## 🔹 Bloque 1: Transferencia de objetos a través de sockets

### ✅ Conceptos clave

- **Serialización**: proceso por el cual un objeto se convierte en una secuencia de bytes para ser enviado por red o almacenado.
- La clase debe implementar `Serializable` para ser enviada.
- Se usan:
    - `ObjectOutputStream` → `writeObject(obj)`
    - `ObjectInputStream` → `readObject()`

### 🧰 TCP

- Cliente y servidor se comunican enviando objetos Java completos por sockets.
- Ejemplo: clase `Persona` con atributos simples (`nombre`, `edad`, etc).

### 🧰 UDP

- Como UDP no gestiona objetos, se usan:
    - `ByteArrayOutputStream`
    - `ByteArrayInputStream`
- Se convierte el objeto a un array de bytes y luego se transmite.

### 🧪 Prácticas destacadas

- **T4S1P1. He estat al servidor**: el cliente envía una `Persona`, el servidor la modifica y la devuelve.
- **T4S1P2. Concessionari**: cliente envía un objeto `Vehiculo` al servidor, que lo guarda en un archivo.