- **Ventaja**: Aprovecha mejor los recursos del sistema ejecutando tareas en paralelo.
- **Proceso**:
    - Tiene su propio espacio de memoria.
- **Hilo**:
    - Ejecuta tareas dentro de un proceso.
    - Comparte el espacio de memoria del proceso.

- **En Java**:
    - Al iniciar el programa, Java crea automáticamente un **hilo principal** que ejecuta `main()`.
    - Se crean nuevos hilos con la clase `Thread` o implementando `Runnable`.
- **Métodos importantes**:
    - `start()`, `isAlive()`, `join()`, `sleep()`, `getState()`, `interrupt()`, `currentThread()`, etc.
- **Actividad práctica**:
    - Programa "TicTac": dos hilos que imprimen "TIC" y "TAC" cada segundo de forma infinita.

---
