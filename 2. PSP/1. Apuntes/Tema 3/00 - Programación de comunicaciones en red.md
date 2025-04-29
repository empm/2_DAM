**Mapa Mental - Tema 3: Programación de comunicaciones en red**

# Tema 3: Comunicaciones en red

## 1. Programación en red con TCP (Bloque 1)

### Fundamentos

- Uso de sockets TCP (orientados a conexión).
    
- Cliente se conecta al servidor usando dirección IP y puerto.
    
- Protocolo fiable: asegura orden y entrega.

### Java: Clases

- `Socket` (cliente)
- `ServerSocket` (servidor)
- `DataInputStream` / `DataOutputStream`
- `PrintStream`

### Flujo básico

1. Servidor crea `ServerSocket` y espera
    
2. Cliente conecta con `Socket`
    
3. Se crean streams de entrada y salida
    
4. Se intercambian mensajes
    
5. Se cierran flujos y sockets

### Prácticas

- **T3P1**: Servidor perpetuamente disponible
- **T3P2-T3P3**: Comunicación con mensajes (cliente lee teclado)
- **T3P5**: Teatro con reservas y respuestas personalizadas
 
---

## 2. Programación en red con UDP (Bloque 2)

### Fundamentos

- No requiere conexión previa (no orientado a conexión)
    
- No garantiza entrega ni orden
    
- Ideal para rapidez y bajo volumen

### Java: Clases

- `DatagramSocket`
- `DatagramPacket`

### Flujo básico

1. Cliente crea socket
    
2. Envía `DatagramPacket` con mensaje
    
3. Servidor recibe y responde con `DatagramPacket`

### Prácticas

- **T3P4**: Cliente UDP desde teclado
- **T3P6**: Cliente envía fecha y servidor responde con día semana

---

## 3. Ejercicios integradores (Bloque 3)

### Ejemplos prácticos

- Servidor TCP multicliente (reserva butacas)
    
- Cliente TCP que consulta información desde teclado
    
- Cliente/servidor UDP interactivo
    
- Servidor "eterno" disponible siempre
