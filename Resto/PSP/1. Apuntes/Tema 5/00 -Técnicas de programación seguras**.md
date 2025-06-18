**Mapa Mental - Tema 5: Técnicas de programación seguras**

# Tema 5: Programación segura

## 1. Técnicas de programación segura (Bloque 1)

### Buenas prácticas

- **Formación continua**:
    - Aprender de errores comunes.
    - Consultar foros y artículos.

- **Tratamiento de datos**:
    - Validar entradas.
    - Comprobar límites.
    - No confiar en datos de URL ni campos ocultos.

- **Protección de información**:
    - No enviar contraseñas en claro.
    - No guardar datos sensibles sin cifrar.

- **Mantenimiento seguro**:
    - Documentar correctamente.
    - Eliminar código obsoleto.

- **Reutilización y revisión**:
    - Reutilizar código comprobado.
    - Revisiones de código (pair review).

- **Listas de control**:
    - Comprobar seguridad en sesiones y almacenamiento.

### Errores a evitar

- Invocar comandos de shell sin control.
- Confiar en éxito de operaciones sin verificar.
- Guardar contraseñas sin protección.

---

## 2. Generación y verificación de firma digital (Bloque 2)

### Message Digest

- **Hash de datos** (SHA-1, SHA-256, MD5).
- Se usa `MessageDigest` en Java.

### Firma Digital

- Basada en criptografía de clave pública/privada.

### Proceso de firma

1. Crear resumen (hash) del mensaje.
2. Cifrar resumen con **clave privada**.
3. Enviar mensaje + firma.

### Proceso de verificación

1. Recalcular resumen del mensaje recibido.
2. Descifrar firma con **clave pública**.
3. Comparar ambos resúmenes.

### Clases Java usadas

- `KeyPairGenerator`, `SecureRandom`, `Signature`.

### Prácticas

- **Crear resúmenes de mensajes**.
- **Generar y verificar firmas digitales**.
