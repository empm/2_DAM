## 🔹 Bloque 3: Cliente-Servidor TCP/UDP

### ✅ Chat TCP multicliente

- Cada cliente se conecta y se gestiona con un hilo.
- El servidor mantiene un **vector de sockets**.
- Cada mensaje de un cliente se difunde a todos los demás.

### ✅ Multicast UDP

- Se usa `MulticastSocket` para que los clientes se unan a un grupo.
- El servidor recibe mensajes por UDP (normal) y los redistribuye por **multicast**.
- Todos los miembros del grupo reciben el mensaje, incluso si se conectaron más tarde (si se añade historial).

### 🧰 Clases clave

- `MulticastSocket`, `DatagramPacket`, `DatagramSocket`
- `joinGroup()`, `leaveGroup()`, `send()`, `receive()`

### 🧪 Práctica destacada

- **T4S3P4. Xat Multicast UDP**:
    - Cliente se une al grupo.
    - Envía mensajes al servidor.
    - Servidor redistribuye mensajes + historial a todos los clientes del grupo.
