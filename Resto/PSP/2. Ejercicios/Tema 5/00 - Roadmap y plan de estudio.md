# 🚀 Roadmap y Plan de Estudio – Tema 5: Programación segura

---

## 📅 Plan de estudio (5 días)

---

### 🟩 Día 1 – Fundamentos de programación segura

- Leer buenas prácticas de programación segura.
- Comprender qué tipos de fallos son comunes (validaciones, contraseñas, datos sensibles).

🧪 **Ejercicio**:

- Lista de errores: Escribir 10 errores que quieres evitar en tus futuros programas.
- Hacer un pequeño programa que valide correctamente una entrada de usuario (por ejemplo, un número entre 1 y 100).

---

### 🟩 Día 2 – Validar y proteger datos

- Prácticas de validación de entradas desde teclado, ficheros y formularios.
- Protección de contraseñas: nunca guardar en texto plano.

🧪 **Ejercicio**:

- Crear un pequeño programa que:
    - Solicite usuario y contraseña.
    - Encripte la contraseña (puedes usar hash SHA-256).
    - Guarde el usuario y contraseña en un archivo seguro.

---

### 🟨 Día 3 – Introducción al resumen de mensajes (hash)

- Estudiar qué es un message digest (función hash).
- Usar `MessageDigest` en Java (`SHA-256`, `MD5`).

🧪 **Ejercicio**:

- Programa que pida texto por teclado y muestre su hash.
- Opcional: Crear el hash de un archivo completo.

---

### 🟨 Día 4 – Firma digital: teoría y generación de claves

- Entender criptografía de clave pública/privada.
- Crear claves con `KeyPairGenerator`.

🧪 **Ejercicio**:

- Programa Java que genere un par de claves (`DSA`) y las imprima o guarde en ficheros.

---

### 🟦 Día 5 – Firma y verificación de mensajes

- Firmar un mensaje con la clave privada.
- Verificar la firma usando la clave pública.

🧪 **Ejercicio**:

- Programa Java que:
    - Genere una firma digital de un texto.
    - Verifique si la firma es correcta al recibir el mensaje.

---

# ✅ Lista de mini-retos prácticos

### 🔸 Nivel básico

-  Validar entradas de usuario de forma segura.
-  Guardar contraseñas en archivos utilizando hashing (`SHA-256`).

### 🔸 Nivel medio

-  Crear un resumen de un texto y verificar que no ha cambiado.

### 🔸 Nivel avanzado

-  Generar firma digital y verificar autenticidad de mensajes.