
- **Problema**: Cuando dos o más hilos acceden al mismo objeto (por ejemplo, a un contador), se producen errores de concurrencia.
- **Solución**: Uso de **synchronized** para proteger las operaciones críticas.
- **synchronized**:
    - Asegura que **solo un hilo** puede ejecutar un bloque de código o método sincronizado a la vez.
    - Si otro hilo intenta entrar, se queda **esperando**.
- **Ejemplo**:
    - Dos hilos accediendo a un contador compartido incrementando y decrementando su valor.
- **Métodos sincronizados**:
    - Se declara así:

```java
public synchronized void metodo() {
 // Código crítico
}
```

- **Actividad práctica**:
    - Gestionar saldo de una cuenta bancaria controlando accesos simultáneos (ingresos y retiradas).
