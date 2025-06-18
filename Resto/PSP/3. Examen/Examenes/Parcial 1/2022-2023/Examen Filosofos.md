> Implementación clásica del **problema de los filósofos comensales** en Java, que muestra un **paradigma de sincronización de hilos** para evitar condiciones de carrera y _deadlocks_.

---

## **🧠 Enunciado resumen**

Cinco filósofos están sentados alrededor de una mesa circular. Cada uno necesita **dos palillos (izquierdo y derecho)** para comer. Solo pueden tener acceso a los palillos que tienen a su izquierda y derecha.

### **Problema:**

- Todos intentan coger palillos al mismo tiempo → **riesgo de interbloqueo**.
- Necesitamos sincronizar correctamente.

---

## **✅ Solución: usar un objeto por palillo + orden de adquisición**
  

### **Clase Palillo**

```java
public class Palillo {
    private final int id;

    public Palillo(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }
}
```


### **Clase Filosofo**

```java
public class Filosofo extends Thread {
    private final int id;
    private final Palillo izquierdo;
    private final Palillo derecho;

    public Filosofo(int id, Palillo izquierdo, Palillo derecho) {
        this.id = id;
        this.izquierdo = izquierdo;
        this.derecho = derecho;
    }

    private void pensar() throws InterruptedException {
        System.out.println("Filósofo " + id + " está pensando...");
        Thread.sleep((long) (Math.random() * 2000));
    }

    private void comer() throws InterruptedException {
        synchronized (izquierdo) {
            synchronized (derecho) {
                System.out.println("🍽️ Filósofo " + id + " está comiendo.");
                Thread.sleep((long) (Math.random() * 2000));
                System.out.println("🧠 Filósofo " + id + " termina de comer.");
            }
        }
    }

    public void run() {
        try {
            while (true) {
                pensar();
                comer();
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
```

### **Clase Main**

```java
public class Main {
    public static void main(String[] args) {
        Palillo[] palillos = new Palillo[5];
        for (int i = 0; i < 5; i++) {
            palillos[i] = new Palillo(i);
        }

        Filosofo[] filosofos = new Filosofo[5];
        for (int i = 0; i < 5; i++) {
            Palillo izquierdo = palillos[i];
            Palillo derecho = palillos[(i + 1) % 5];

            // Para evitar deadlocks, el último filósofo toma primero el palillo derecho
            if (i == 4) {
                filosofos[i] = new Filosofo(i, derecho, izquierdo);
            } else {
                filosofos[i] = new Filosofo(i, izquierdo, derecho);
            }

            filosofos[i].start();
        }
    }
}
```

---

## **💡 Claves del paradigma:**

|**Concepto Java**|**Aplicación en el código**|
|---|---|
|Thread|Cada filósofo es un hilo.|
|synchronized|Controla el acceso a los palillos.|
|deadlock|Evitado cambiando el orden en un hilo (filósofo 4).|
|sleep()|Simula pensar/comer con pausas aleatorias.|
