# 🧠 Plan de Repaso - Tema 2: Programación Multihilo

## Objetivo general

- Entender **qué son** hilos, procesos, sincronización y coordinación en Java.
- **Saber programarlos** de forma correcta (controlando problemas de concurrencia).


---

## 📅 Plan de Repaso en 5 Días

**Día 1: Conceptos básicos**

- Leer el mapa mental completo.
- Repasar qué son proceso vs hilo.
- Programar un ejemplo sencillo con dos hilos (`Thread`, `Runnable`).

**Día 2: Métodos de los hilos**

- Practicar `start()`, `isAlive()`, `sleep()`, `join()`, `interrupt()`.
- Modificar los ejemplos TIC-TAC para experimentar.

**Día 3: Sincronización básica**

- Repasar `synchronized` en métodos y bloques.
- Programar un pequeño banco con dos personas retirando dinero del mismo objeto `Compte`.

**Día 4: `wait()`, `notify()`, `notifyAll()`**

- Leer bien cómo funcionan.
- Programar el clásico problema **Productor-Consumidor**.
- Entender cuándo un hilo espera y cuándo otro hilo lo despierta.

**Día 5: Prácticas reales**

- Resolver el problema del **barbero**.
- Resolver una variante del **banco** con personas ingresando/retirando hasta que el saldo llegue a 0.

---

# 🛠️ Roadmap sencillo para practicar programación multihilo

### 1. Crear y gestionar hilos

-  Crear un hilo extendiendo `Thread`.
-  Crear un hilo implementando `Runnable`.
-  Usar `start()`, `sleep()`, `isAlive()`, `join()`.

### 2. Sincronizar acceso a recursos

-  Proteger métodos críticos con `synchronized`.
-  Simular accesos a una cuenta bancaria.

### 3. Coordinar hilos (`wait()` y `notify()`)

-  Implementar un productor que pone datos.
-  Implementar un consumidor que espera datos.

### 4. Resolver problemas reales

-  Simular una barbería.
-  Ampliar el problema del banco con ingresos y reintegros bloqueantes.