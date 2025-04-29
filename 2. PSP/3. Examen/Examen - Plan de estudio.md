- [ ] Ejercicios de entrega
- [ ] pedirle a Jaime examen
- [ ] todo
- [ ] tener ejemplos ya que repite lo mismo 
- [ ] c: estructura y anidar if else, le importa que sepamos la estructura
---

# 📋 Diagnóstico y enfoque para tu preparación

|Tema|¿Importante?|¿Por qué?|
|:--|:--|:--|
|**Programación multihilo básica**|✅ Imprescindible|Aparece en ejercicios de Robots, Cinta, Filósofos.|
|**Sincronización (`wait()`, `notifyAll()`)**|✅ Imprescindible|Necesario en Robots y problemas de acceso a recursos compartidos (filósofos, cinta).|
|**Sockets TCP Cliente/Servidor multicliente**|✅ Imprescindible|Examen de cadenas TCP multicliente (`Socket`, `ServerSocket`, hilos por cliente).|
|**Ordenación de listas de cadenas**|✅ Imprescindible|Ejercicio de examen de ordenar cadenas alfabéticamente (`Collections.sort()`).|
|**Sockets UDP Multicast**|❌ Opcional|Solo aparece en teoría, no en los exámenes prácticos de ahora.|

---

# 🚀 Plan de estudio de 2 semanas (para aprobar)

## 📅 Semana 1: Dominar la base técnica

|Día|Objetivo|Actividades|
|:--|:--|:--|
|1|**Repasar multihilos en Java**|Crear y lanzar hilos (`Thread`), `run()` y `start()`.|
|2|**Sincronización en objetos**|Aprender a usar `synchronized`, `wait()`, `notifyAll()`.|
|3|**Practicar robots sobre cinta**|Resolver caso RobotA/RobotB que trabajan sobre una cinta (`Cinta`, `RobotA`, `RobotB`).|
|4|**Resolver problema de filósofos**|Programar filósofos con `palillos[]`, `synchronized`, control de recursos.|
|5|**Sockets TCP - Cliente/Servidor básico**|Enviar texto desde cliente a servidor usando `Socket` y `ServerSocket`.|
|6|**Sockets TCP - Servidor multicliente**|Crear servidor que maneje múltiples clientes con hilos (`Thread` por cliente).|
|7|**Ordenar cadenas en Java**|Practicar `Collections.sort()` en listas de `String`.|

---

## 📅 Semana 2: Preparación específica para el examen

|Día|Objetivo|Actividades|
|:--|:--|:--|
|8|**Proyecto: Simular examen TCP de cadenas**|Cliente envía cadenas; servidor las ordena y responde.|
|9|**Crear varios clientes conectándose simultáneamente**|Ejecutar múltiples instancias de cliente TCP.|
|10|**Practicar sincronización avanzada**|Mejorar código de Robots/Filósofos para asegurar que `wait()` y `notifyAll()` se usan correctamente.|
|11|**Mini-examen 1**|Resolver en 1h40min: Robots + Cinta + TCP + Ordenar cadenas.|
|12|**Repasar errores comunes**|Fallos típicos en TCP, ordenación, hilos bloqueados, `wait()` mal usado.|
|13|**Mini-examen 2**|Resolver problema de TCP multicliente completo de nuevo.|
|14|**Simulacro examen**|Proyecto completo en condiciones de examen: Robots, TCP, ordenar cadenas, hilos.|

---

# ✅ Resumen de habilidades que debes asegurar:

- Crear hilos (`Thread`), controlar ejecución (`run`, `sleep`).
- Usar `synchronized`, `wait()`, `notifyAll()` para evitar problemas de concurrencia.
- Programar comunicación TCP básica (`Socket`, `ServerSocket`).
- Implementar servidor TCP multicliente (un hilo por cliente).
- Ordenar cadenas alfabéticamente (`Collections.sort(List)`).
- Gestionar flujos de entrada/salida (`BufferedReader`, `PrintWriter`).

---
