# 📅 Lista de ejercicios diarios (2 semanas)

---

## 📅 Semana 1 - Fundamentos sólidos

| Día | Ejercicio                            | Descripción                                                                                                | Tiempo recomendado |
| :-- | :----------------------------------- | :--------------------------------------------------------------------------------------------------------- | :----------------- |
| 1   | **Crear y lanzar hilos**             | Crear una clase `MiHilo` que imprima 10 números y otra que imprima 10 letras en paralelo.                  | 30 min             |
| 2   | **Sincronización básica**            | Crear dos hilos que suman a una misma variable sincronizadamente (`synchronized`).                         | 40 min             |
| 3   | **Proyecto Robots Cinta**            | Crear `RobotA` que añade kilos y `RobotB` que retira kilos de una `Cinta` usando `wait()` y `notifyAll()`. | 1h                 |
| 4   | **Proyecto Filósofos**               | Simular 5 filósofos que comparten palillos usando array de booleanos.                                      | 1h 20min           |
| 5   | **TCP básico: Eco cliente/servidor** | Cliente envía un mensaje, servidor lo repite. Usar `Socket` y `ServerSocket`.                              | 1h                 |
| 6   | **TCP multicliente**                 | Adaptar el servidor anterior para aceptar varios clientes (un `Thread` por cliente).                       | 1h                 |
| 7   | **Ordenar cadenas**                  | Crear una lista `List<String>`, añadir palabras y ordenarlas con `Collections.sort()`.                     | 40 min             |

---

## 📅 Semana 2 - Foco total en el examen

|Día|Ejercicio|Descripción|Tiempo recomendado|
|:--|:--|:--|:--|
|8|**Proyecto examen TCP**|Cliente recoge cadenas de teclado y las manda al servidor; servidor las ordena.|1h 30min|
|9|**Multiples clientes TCP**|Lanzar 3 clientes simultáneamente para comprobar que cada uno recibe su respuesta ordenada.|1h|
|10|**Refinamiento sincronización**|Mejorar proyecto Robots/Filósofos: asegúrate que siempre se respetan las condiciones de `wait()` y `notifyAll()`.|1h|
|11|**Mini-examen 1**|Hacer Robots Cinta + TCP Eco + Ordenar cadenas como si fuera examen (máximo 1h40min).|1h 40min|
|12|**Errores comunes revisión**|Revisar: fallos de cerrar sockets, problemas de sincronización, `ConcurrentModificationException`.|30 min|
|13|**Mini-examen 2**|Repetir todo: cliente TCP multicliente enviando cadenas, servidor ordenando. Sin mirar apuntes.|1h 40min|
|14|**Simulacro completo**|Resolver todo el escenario real (Robots sincronizados + TCP cadenas ordenadas) como examen real.|1h 40min|

---

# ✅ Checklist rápida de lo que debes lograr al final:

- [ ]  Sé crear y lanzar hilos correctamente.
- [ ]  Sé sincronizar operaciones compartidas usando `synchronized`, `wait()`, `notifyAll()`.
- [ ]  Sé programar cliente y servidor TCP que aceptan múltiples conexiones.
- [ ]  Sé ordenar listas de cadenas en Java (`Collections.sort()`).
- [ ]  Sé gestionar errores básicos: `IOException`, `InterruptedException`, `SocketException`.