# 🚀 Roadmap y Plan de Estudio – Tema 4: Servicios en red

---

## 📅 Plan de estudio (5 días)

---

### 🟩 Día 1 – Transferencia de objetos por sockets (TCP)

- Entender qué es la interfaz `Serializable`.
- Usar `ObjectOutputStream` y `ObjectInputStream`.
- Crear una clase simple (`Persona`, `Producto`, etc.) y enviarla desde un cliente TCP a un servidor.

🧪 **Ejercicio**:

- Cliente crea objeto `Persona`, el servidor le añade texto en el nombre y lo devuelve.  
    (Práctica: **He estat al servidor**)

---

### 🟩 Día 2 – Transferencia de objetos por UDP

- Repasar conversión objeto ↔ array de bytes.
- Usar `ByteArrayOutputStream` y `ByteArrayInputStream`.

🧪 **Ejercicio**:

- Cliente UDP envía objeto serializado al servidor, este lo modifica y responde.

---

### 🟨 Día 3 – Crear un servidor multihilo

- Crear un `ServerSocket` que escuche.
- Generar un hilo por cada cliente (`FilServidor`).
- Cada hilo debe leer mensajes y responder.

🧪 **Ejercicio**:

- Servidor recibe cadenas de texto y las devuelve en mayúsculas.
- Ampliar lógica para manejar varios clientes simultáneamente.

---

### 🟨 Día 4 – Servidor multicliente con lógica

- El hilo del servidor debe leer, procesar y responder datos.
- Usar ficheros para guardar datos en servidor.

🧪 **Ejercicio**:

- Servidor pregunta un quiz al cliente y evalúa respuestas.
- Guarda nombre y puntuación en un archivo.  
    (Práctica: **Quiz Magic**)

---

### 🟦 Día 5 – Cliente-Servidor TCP/UDP con difusión

- Revisar sockets TCP multicliente (lista de sockets).
- Aprender `MulticastSocket`, `joinGroup()` y `send()`.

🧪 **Ejercicio**:

- Crear servidor UDP que recibe mensajes de clientes y los redistribuye por multicast.
- Cliente recibe y muestra mensajes + historial.  
    (Práctica: **Xat Multicast UDP**)

---

## ✅ Lista de mini-retos prácticos

### 🔸 Nivel básico

-  Serializar objeto y guardarlo en fichero.
-  Enviar objeto desde cliente TCP al servidor.

### 🔸 Nivel medio

-  Servidor TCP que gestiona múltiples clientes.
-  Cliente que responde a preguntas y servidor evalúa.

### 🔸 Nivel avanzado

-  Chat UDP multicast con historial.
-  Simulación de alta de vehículos con persistencia.

---

# Carpeta Modelo para los proyectos

---

### 🟩 Carpeta 1: **Chat Multicliente TCP**

**Estructura del proyecto:**

```
/ChatTCP/
├── ServidorChat.java
├── FilServidor.java
├── ClientChat.java
```

#### 🧩 Contenido:

- `ServidorChat.java`: crea un `ServerSocket`, acepta clientes, y lanza un `FilServidor` por cada uno.
- `FilServidor.java`: recibe mensajes de un cliente y los reenvía a todos los conectados.
- `ClientChat.java`: cliente con consola que se conecta y envía mensajes.

---

### 🟦 Carpeta 2: **Servidor Multicliente con lógica personalizada (ej. Quiz)**

**Estructura del proyecto:**

```
/ServidorMulticliente/
├── Servidor.java
├── FilServidor.java
├── ClientQuiz.java
├── PreguntesRespostes.txt
├── Puntuacions.txt
```

#### 🧩 Contenido:

- `Servidor.java`: lanza el servidor y acepta múltiples conexiones.
- `FilServidor.java`: atiende a cada cliente, envía preguntas, evalúa respuestas y guarda puntuación.
- `ClientQuiz.java`: se conecta, recibe preguntas, responde y muestra resultado.
- `PreguntesRespostes.txt`: preguntas y respuestas (formato simple).
- `Puntuacions.txt`: archivo donde se guarda nombre + puntuación del cliente.

---
Perfecto. Aquí tienes los dos proyectos **listos para copiar y pegar** en tu IDE Java.

---

## 🟩 Proyecto 1: Chat Multicliente TCP

### 🔹 `ServidorChat.java`

```java
import java.net.*;
import java.io.*;
import java.util.*;

public class ServidorChat {
    static Vector<Socket> clientes = new Vector<>();

    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(5000);
        System.out.println("Servidor de chat en marcha...");

        while (true) {
            Socket cliente = server.accept();
            clientes.add(cliente);
            new FilServidor(cliente, clientes).start();
        }
    }
}
```

### 🔹 `FilServidor.java`

```java
import java.io.*;
import java.net.*;
import java.util.*;

public class FilServidor extends Thread {
    private Socket socket;
    private Vector<Socket> clientes;

    public FilServidor(Socket socket, Vector<Socket> clientes) {
        this.socket = socket;
        this.clientes = clientes;
    }

    public void run() {
        try {
            BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter salida;

            String missatge;
            while ((missatge = entrada.readLine()) != null) {
                System.out.println("Missatge rebut: " + missatge);
                for (Socket s : clientes) {
                    if (!s.isClosed()) {
                        salida = new PrintWriter(s.getOutputStream(), true);
                        salida.println(missatge);
                    }
                }
            }
        } catch (IOException e) {
            System.out.println("Client desconnectat");
        }
    }
}
```

### 🔹 `ClientChat.java`

```java
import java.io.*;
import java.net.*;

public class ClientChat {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 5000);
        BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter salida = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader teclat = new BufferedReader(new InputStreamReader(System.in));

        new Thread(() -> {
            try {
                String resposta;
                while ((resposta = entrada.readLine()) != null) {
                    System.out.println(">> " + resposta);
                }
            } catch (IOException e) {
                System.out.println("Desconnectat del servidor.");
            }
        }).start();

        String missatge;
        while ((missatge = teclat.readLine()) != null) {
            salida.println(missatge);
        }
    }
}
```

---

## 🟦 Proyecto 2: Servidor Multicliente con lógica (Quiz)

### 🔹 `Servidor.java`

```java
import java.io.*;
import java.net.*;

public class Servidor {
    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(6000);
        System.out.println("Servidor Quiz actiu...");

        while (true) {
            Socket socket = server.accept();
            new FilServidor(socket).start();
        }
    }
}
```

### 🔹 `FilServidor.java`

```java
import java.io.*;
import java.net.*;

public class FilServidor extends Thread {
    private Socket socket;

    public FilServidor(Socket socket) {
        this.socket = socket;
    }

    public void run() {
        try (
            BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter sortida = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader fitxer = new BufferedReader(new FileReader("PreguntesRespostes.txt"));
            FileWriter puntuacions = new FileWriter("Puntuacions.txt", true);
        ) {
            String nom = entrada.readLine();
            int punts = 0;
            String linia;
            while ((linia = fitxer.readLine()) != null) {
                String[] parts = linia.split(";");
                sortida.println(parts[0]); // envia pregunta
                String respostaUsuari = entrada.readLine();
                if (respostaUsuari.equalsIgnoreCase(parts[1])) {
                    punts++;
                }
            }
            sortida.println("Puntuació final: " + punts);
            puntuacions.write(nom + ": " + punts + "\n");
        } catch (IOException e) {
            System.out.println("Error amb client.");
        }
    }
}
```

### 🔹 `ClientQuiz.java`

```java
import java.io.*;
import java.net.*;

public class ClientQuiz {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 6000);
        BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter sortida = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader teclat = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Nom d'usuari: ");
        String nom = teclat.readLine();
        sortida.println(nom);

        String missatge;
        while ((missatge = entrada.readLine()) != null) {
            System.out.println(missatge);
            if (missatge.startsWith("Puntuació final")) break;
            String resposta = teclat.readLine();
            sortida.println(resposta);
        }
    }
}
```

### 🔹 `PreguntesRespostes.txt` (en el mismo directorio)

```
Capital de França?;paris
5 + 5?;10
Color del cel?;blau
```

---

¿Quieres que ahora te prepare algo parecido para UDP multicast o lo dejamos aquí de momento?