## 🔹 Bloque 1: Programación en red TCP

### ✅ Conceptos importantes

- La comunicación en red se basa en direcciones IP y puertos.
    
- Se usa una arquitectura **Cliente-Servidor**.
    
- **Sockets TCP**:
    - Garantizan que los datos lleguen en orden y sin pérdida.
    - Se utiliza cuando se necesita **fiabilidad**.
    - Java usa: `Socket` (cliente) y `ServerSocket` (servidor).

### 🧪 Flujo básico de conexión

1. El servidor abre un puerto (`ServerSocket`).
2. El cliente se conecta al host y puerto (`Socket`).
3. Ambos intercambian datos con `InputStream` / `OutputStream`.

### 🧰 Clases clave en Java

```java
Socket socket = new Socket("localhost", 5000);
ServerSocket server = new ServerSocket(5000);
DataInputStream in = new DataInputStream(socket.getInputStream());
DataOutputStream out = new DataOutputStream(socket.getOutputStream());
```

### 🧪 Prácticas destacadas

- **T3P1. Servidor etern**:
    - Servidor que siempre está activo y espera conexiones.

- **T3P2 y T3P3. Comunicación Cliente/Servidor I y II**:
    - Cliente envía mensajes hasta escribir “Adeu”.
    - El servidor responde con mensajes personalizados.
    - En T3P3, el cliente lee desde teclado.

- **T3P5. Teatro municipal**:
    - El cliente puede reservar butacas por tipo.
    - Comandos: “Hola”, “Veure butaques”, “Fi”.
    - El servidor controla el stock y responde adecuadamente.
