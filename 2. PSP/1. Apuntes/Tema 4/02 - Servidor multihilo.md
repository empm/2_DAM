## 🔹 Bloque 2: Servidor multihilo

### ✅ Conceptos clave

- Cuando hay múltiples clientes, el servidor crea **un hilo por cada conexión**.
- Cada hilo se encarga de gestionar el socket de un cliente.
- Patrón básico:
    1. `ServerSocket server = new ServerSocket(puerto);`
    2. `Socket socket = server.accept();`
    3. `new Thread(new FilServidor(socket)).start();`

### 🧰 Tareas del hilo

- Leer del cliente.
- Responder.
- Finalizar comunicación.

### 🧪 Práctica destacada

- **T4S2P3. Quiz Magic**:
    - Cliente responde preguntas enviadas desde el servidor.
    - Servidor evalúa respuestas y guarda puntuaciones.
    - Cada cliente es atendido por un hilo distinto.

