
- **Problema clásico**: **Productor-consumidor**.
    - Productor crea datos.
    - Consumidor los consume.
- **Problema**:
    - Si el consumidor consume más rápido que el productor, puede fallar.
- **Solución**:
    - Coordinación usando `wait()` y `notify()`:
        - `wait()`: el hilo espera y libera el bloqueo.
        - `notify()`: despierta un hilo esperando.
        - `notifyAll()`: despierta a todos los hilos esperando.
- **Clase `Cua`**:
    - Tiene métodos sincronizados `put()` y `get()` controlados con `wait()` y `notify()`.

---
## Semana 5: Proyecto Compte2

- **Objetivo**:
    - Gestionar un saldo de cuenta bancaria de forma segura.
- **Cuenta (`Compte`)**:
    - Métodos sincronizados para:
        - Ingresar dinero.
        - Retirar dinero.
        - Consultar saldo.
    - Control de errores si:
        - El ingreso supera el máximo permitido.
        - El reintegro no puede realizarse por saldo insuficiente.
- **Personas (`Persona`)**:
    - Cada una es un hilo que realiza ingresos y retiradas aleatorias en la cuenta.