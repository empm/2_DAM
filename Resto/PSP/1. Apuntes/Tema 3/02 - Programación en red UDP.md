### ✅ Conceptos importantes

- **Sockets UDP**:
    
    - No hay conexión previa.
        
    - No se garantiza que los datos lleguen ni el orden.
        
    - Más rápido y útil para tiempo real (ej. streaming).
        
- Java usa:
    
    - `DatagramSocket` → para enviar/recibir.
        
    - `DatagramPacket` → representa un paquete de datos.
        

### 🧰 Sintaxis UDP en Java

```java
DatagramSocket socket = new DatagramSocket();
byte[] data = "mensaje".getBytes();
DatagramPacket packet = new DatagramPacket(data, data.length, inetAddress, port);
socket.send(packet);
```

### 🧪 Prácticas destacadas

- **T3P4. UDP Cliente/Servidor desde teclado**:
    
    - El cliente envía mensajes desde teclado al servidor UDP.
        
- **T3P6. Quin dia va ser**:
    
    - Cliente pide una fecha y la envía.
        
    - Servidor responde con el día de la semana.
        
    - Usa `GregorianCalendar` y `SimpleDateFormat`.
        
