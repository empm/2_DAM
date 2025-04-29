# 🔹 Bloque 2: Generar y verificar firma digital

### ✅ Conceptos clave

- **Message Digest**:
    - Es un resumen único de datos generado con funciones hash (`SHA-1`, `SHA-256`, `MD5`).
    - Java usa la clase `MessageDigest` para crear resúmenes:

```java
MessageDigest md = MessageDigest.getInstance("SHA-256");
byte[] resumen = md.digest(datos);
```

- **Firma digital**:
    - Utiliza **criptografía de clave pública** (par clave privada / clave pública).
    - **Proceso de firma**:
        1. Crear hash del mensaje.
        2. Cifrar el hash con la **clave privada** → Firma.
        3. Enviar mensaje + firma.

    - **Proceso de verificación**:
        1. Recalcular hash del mensaje recibido.
        2. Descifrar firma usando **clave pública**.
        3. Comparar ambos hashes.

- **Clases Java utilizadas**:
    - `KeyPairGenerator` para generar claves (`DSA` en el ejemplo).
    - `SecureRandom` para aleatoriedad.
    - `Signature` para firmar y verificar:

```java
Signature sign = Signature.getInstance("SHA256withDSA");
sign.initSign(clavePrivada);
sign.update(datos);
byte[] firma = sign.sign();
```


### 🧪 Prácticas destacadas

- **T5S1P1**:
    - Crear resúmenes de mensajes y comprobar integridad de datos.

- **T5S2P2**:
    - Generar y verificar firmas digitales en mensajes usando claves DSA.