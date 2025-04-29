# 🚀 Roadmap de estudio – Tema 3: Comunicaciones en red (TCP y UDP)

---

## 📅 Plan de estudio (5 días)

### 🟩 Día 1 – Fundamentos y Sockets TCP

- Leer resumen y mapa mental.
- Entender qué es una IP, un puerto y cómo funciona un socket.
- Estudiar clases `Socket` y `ServerSocket`.

🧪 **Ejercicio**:

- Crear un servidor que reciba un mensaje y lo imprima.
- Crear un cliente que se conecte al servidor y envíe “Hola servidor”.

---

### 🟩 Día 2 – Comunicación Cliente-Servidor TCP

- Implementar `InputStream` y `OutputStream`.
- Aprender a usar `DataInputStream`, `DataOutputStream`, `PrintStream`.

🧪 **Ejercicio**:

- Simular una conversación: cliente envía 3 frases, el servidor responde.
- Añadir cierre con mensaje “Adeu” → servidor responde “Fins després”.

---

### 🟩 Día 3 – Práctica Teatro (Servidor multicliente)

- Repasar cómo mantener al servidor siempre en espera.
- Implementar lógica para comandos personalizados.

🧪 **Ejercicio**:

- Crear un servidor que maneje reservas de butacas por tipo.
- El cliente puede consultar “veure butaques”, reservar o salir.

---

### 🟦 Día 4 – Introducción a UDP

- Aprender sobre `DatagramSocket` y `DatagramPacket`.
- Diferencias entre TCP y UDP.

🧪 **Ejercicio**:

- Crear un cliente que envía un texto y servidor que lo devuelve en mayúsculas.
- Añadir control de errores por si el mensaje no llega.

---

### 🟦 Día 5 – Práctica avanzada con UDP

- Practicar el envío y recepción de paquetes con datos estructurados.
- Validar entradas desde cliente.

🧪 **Ejercicio**:

- Crear cliente que pide día, mes y año → servidor responde con día de la semana.
- Validar entradas (día entre 1-31, mes 1-12, año > 1800).

---

# ✅ Lista de ejercicios prácticos por nivel

### 🔸 Nivel básico

-  Cliente TCP dice “Hola”, servidor responde.
-  Cliente TCP envía “Adeu”, servidor responde “Fins després”.

### 🔸 Nivel medio

-  Cliente TCP interactúa con servidor tipo chatbot.
-  Cliente UDP que envía y recibe frases por consola.

### 🔸 Nivel avanzado

-  Sistema de reservas de butacas (TCP).
-  Día de la semana desde una fecha (UDP).
-  Servidor eterno que maneja múltiples clientes (TCP).
