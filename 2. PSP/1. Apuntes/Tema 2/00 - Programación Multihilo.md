**Mapa Mental Completo - Tema 2: Programación Multihilo**

# Tema 2: Programación Multihilo

## 1. Conceptos básicos de procesos y hilos (Semana 2)

- **Proceso**: Programa en ejecución con su propio espacio de memoria.
    
- **Hilo**: Unidad ligera dentro de un proceso. Comparte memoria.

### Hilos en Java

- `Thread` o `Runnable` para crear hilos.
    
- Métodos importantes:
    
    - `start()`, `isAlive()`, `join()`, `sleep()`, `getState()`, `interrupt()`, `currentThread()`.

### Actividad

- Programa **TIC-TAC** usando 2 hilos que imprimen "TIC" y "TAC" alternativamente.

---

## 2. Sincronización con `synchronized` (Semana 4)

- **Problema**: Acceso concurrente a recursos compartidos.
    
- **Solución**: Usar bloques o métodos `synchronized`.

### synchronized

- Bloquea el acceso a zonas críticas:

```java
synchronized (objeto) { /* Zona crítica */ }
```

- También se puede sincronizar un método completo:

```java
public synchronized void metodo() { /* ... */ }
```

### Actividad

- Simular una cuenta bancaria compartida, donde personas hacen ingresos y retiradas.

---

## 3. Coordinación avanzada con `wait()` y `notify()` (Semana 5)

- **Problema**: El Productor debe esperar que haya espacio. El Consumidor debe esperar que haya datos.
    
- **Solución**:
    
    - `wait()`: Poner un hilo en espera liberando el bloqueo.
        
    - `notify()`: Despertar un hilo en espera.
        
    - `notifyAll()`: Despertar a todos los hilos en espera.
        

### Actividad

- Implementar el modelo **Productor-Consumidor**.

---

## 4. Prácticas avanzadas

### Compte2

- Simulación realista de gestión de saldo bancario.
    
- Control de errores en ingresos/reintegros.
    
- Personas operando sobre un mismo objeto `Compte` compartido.
    

### Problema del Barbero

- Simulación concurrente de una barbería:
    
    - Sala de espera limitada.
        
    - Barber duerme si no hay clientes.
        
    - Clientes se van si no hay sillas libres.
        
    - Sincronización de butaca y sillas de espera.

---

# Ejemplos de código relacionados con cada bloque

## 1. Hilos básicos: TIC-TAC

```java
class Tic extends Thread {
    public void run() {
        while (true) {
            System.out.println("TIC");
            try { Thread.sleep(1000); } catch (InterruptedException e) {}
        }
    }
}

class Tac extends Thread {
    public void run() {
        while (true) {
            System.out.println("TAC");
            try { Thread.sleep(1000); } catch (InterruptedException e) {}
        }
    }
}

public class TicTac {
    public static void main(String[] args) {
        new Tic().start();
        new Tac().start();
    }
}
```

## 2. Uso de `synchronized` para acceso a saldo compartido

```java
class Compte {
    private int saldo;

    public Compte(int saldoInicial) {
        this.saldo = saldoInicial;
    }

    public synchronized void ingresar(int cantidad) {
        saldo += cantidad;
    }

    public synchronized boolean retirar(int cantidad) {
        if (cantidad <= saldo) {
            saldo -= cantidad;
            return true;
        } else {
            System.out.println("Saldo insuficiente.");
            return false;
        }
    }

    public synchronized int getSaldo() {
        return saldo;
    }
}
```

## 3. Modelo Productor-Consumidor con `wait()` y `notify()`

```java
class Cua {
    private int valor;
    private boolean disponible = false;

    public synchronized int get() {
        while (!disponible) {
            try { wait(); } catch (InterruptedException e) {}
        }
        disponible = false;
        notifyAll();
        return valor;
    }

    public synchronized void put(int valor) {
        while (disponible) {
            try { wait(); } catch (InterruptedException e) {}
        }
        this.valor = valor;
        disponible = true;
        notifyAll();
    }
}
```

## 4. Esquema para el problema del Barbero

```java
class ButacaBarber {
    private boolean ocupada = false;

    public synchronized void ocupar(int idCliente) {
        while (ocupada) {
            try { wait(); } catch (InterruptedException e) {}
        }
        ocupada = true;
        System.out.println("Cliente " + idCliente + " ocupa la butaca");
    }

    public synchronized void liberar() {
        ocupada = false;
        notifyAll();
    }
}

class Barber extends Thread {
    private ButacaBarber butaca;

    public Barber(ButacaBarber butaca) { this.butaca = butaca; }

    public void run() {
        while (true) {
            butaca.liberar();
            System.out.println("Barbero corta cabello");
            try { Thread.sleep(2000); } catch (InterruptedException e) {}
        }
    }
}
```