
### **1. ¿Qué protocolo garantiza la entrega de los paquetes?**

  

✅ **Respuesta: a) TCP**

  

**Explicación:**

TCP (Transmission Control Protocol) es un protocolo orientado a la conexión que garantiza la entrega ordenada y sin errores de los datos.

---

### **2. Para la transmisión de audio y video en tiempo real se usa:**

  

✅ **Respuesta: c) UDP**

  

**Explicación:**

UDP (User Datagram Protocol) es ideal para tiempo real porque es rápido y no espera confirmaciones, a diferencia de TCP. Prefiere velocidad sobre fiabilidad.

---

### **3. Cuando un emisor quiere enviar un paquete UDP a un grupo multicast:**

  

✅ **Respuesta: a) No tiene por qué estar en el grupo**

  

**Explicación:**

El emisor puede enviar a un grupo multicast **sin pertenecer** a él. Solo los receptores deben haberse unido al grupo multicast para recibirlo.

---

### **4. Cuando un emisor quiere enviar un paquete UDP a un grupo multicast tiene que enviarlo a una dirección de clase:**

  

✅ **Respuesta: c) D (rango 224.0.0.0 – 239.255.255.255)**

  

**Explicación:**

Las direcciones de clase D son las reservadas para **multicast** en IPv4.

---

### **5. Los algoritmos de resúmenes de mensajes (funciones hash) se usan para:**

  

✅ **Respuesta: c) Comprobar la integridad de los datos del mensaje y la identidad del emisor si se acompaña de firma digital.**

  

**Explicación:**

Un hash no cifra, solo genera un resumen único del mensaje. Si se firma, puede usarse para verificar autenticidad.

---

### **6. En la criptografía de clave asimétrica (pública/privada):**

  

✅ **Respuesta: a) El emisor encripta con la clave pública del receptor y el receptor desencripta con su clave privada.**

  

**Explicación:**

Esto asegura que **solo el receptor** (que tiene la clave privada) pueda leer el mensaje cifrado.

---

### **Pregunta de desarrollo: ¿Cómo implementamos un servidor TCP concurrente?**

  

**Respuesta:**

Para aceptar múltiples clientes en TCP:

1. Creamos un ServerSocket.
    
2. Usamos un bucle while (true) para aceptar conexiones (accept()).
    
3. Cada vez que se acepta una conexión, se lanza un nuevo Thread (o usamos un ExecutorService) para gestionar ese cliente individualmente.
    

```
ServerSocket server = new ServerSocket(5000);
while (true) {
    Socket cliente = server.accept();
    new Thread(() -> manejarCliente(cliente)).start();
}
```

---

### **Pregunta de desarrollo: ¿Qué es una autoridad de certificación?**

  

**Respuesta:**

Una **autoridad de certificación (CA)** es una entidad confiable que:

- Emite certificados digitales.
    
- Verifica la identidad del titular de la clave pública.
    
- Garantiza que una clave pública realmente pertenece a quien dice.
    

  

Ejemplo de CA: Let’s Encrypt, DigiCert, etc.

---

¿Quieres que lo pase todo a un formato de plantilla para estudiar o tipo test interactivo?