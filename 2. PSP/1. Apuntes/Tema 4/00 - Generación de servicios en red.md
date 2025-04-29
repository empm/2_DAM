---

# 🧩 Tema 4: Generación de servicios en red

---
**Mapa Mental - Tema 4: Generación de servicios en red**

# Tema 4: Servicios en red

## 1. Transferencia de objetos por sockets (Bloque 1)

### Fundamentos

- Uso de la interfaz `Serializable`
- Serialización convierte objetos Java en secuencias de bytes
- Se usa en sockets para transferir objetos completos

### TCP

- Clases clave: `ObjectInputStream` y `ObjectOutputStream`
- Métodos: `writeObject(obj)`, `readObject()`
- Ejemplo: cliente envía `Persona`, servidor la modifica y responde

### UDP

- Conversión manual del objeto a bytes
- Clases: `ByteArrayOutputStream`, `ByteArrayInputStream`

### Prácticas

- **He estat al servidor**: ida y vuelta de objeto `Persona`
- **Concessionari**: cliente da de alta vehículo, servidor guarda objeto

---

## 2. Servidor multihilo (Bloque 2)

### Fundamentos

- El servidor crea un hilo por cliente usando `Thread`
- Hilo gestiona el `Socket` recibido del `accept()`

### Patrón básico

1. `ServerSocket` escucha
2. Cliente se conecta
3. Se crea `FilServidor(socket)` y se lanza con `start()`

### Lógica del hilo

- Lee del cliente
- Procesa datos
- Responde y finaliza

### Práctica destacada

- **Quiz Magic**: servidor manda preguntas y evalúa, guarda resultados en fichero

---

## 3. Cliente-servidor TCP/UDP (Bloque 3)

### TCP: Xat multicliente

- Servidor mantiene lista de sockets
- Cada hilo difunde mensaje recibido a todos

### UDP: Multicast

- `MulticastSocket` para enviar a un grupo de clientes
- Cliente se une al grupo con `joinGroup()`
- Servidor redistribuye mensajes a todo el grupo

### Práctica

- **Xat Multicast UDP**: cliente manda mensaje al servidor, este reenvía al grupo con historial
