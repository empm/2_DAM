En programación de sistemas, muchas veces necesitamos que **dos procesos** se comuniquen entre sí para compartir información o coordinarse. Existen varias formas de hacerlo:

- **Pipes (tuberías)**
    
- **Colas**
    
- **Semáforos**
    
- **Memoria compartida**


  

### **Pipes**

> Un **Pipe** (o tubería) es un mecanismo que permite que **un proceso escriba información** y **otro la lea**. Aunque parece un fichero, en realidad es algo temporal que conecta a los procesos.

**Importante**: un Pipe normal solo funciona **entre procesos padre e hijo**.

#### **Crear un Pipe en C**

```
#include <unistd.h>

int fd[2];
pipe(fd);
```

- fd[0] es para **leer**.
    
- fd[1] es para **escribir**.

#### **Leer y escribir con Pipe**

```c
read(fd[0], buffer, cantidad);   // Leer del pipe
write(fd[1], buffer, cantidad);  // Escribir en el pipe
```

**Ejemplo sencillo**:

1. El **padre** escribe un mensaje.
    
2. El **hijo** lee ese mensaje.
 

Pero ojo: los dos comparten los mismos descriptores (fd[0] y fd[1]), así que hay que **cerrar** el que no uses en cada proceso para evitar errores:

- Si **escribes**, cierra fd[0].
    
- Si **lees**, cierra fd[1].
  

Esto también resuelve el problema de que los Pipes **solo permiten comunicación en un sentido**: de padre a hijo o de hijo a padre, pero no ambos a la vez con el mismo Pipe.

---

### **Pipes con nombre:** 

### **FIFOs**

Cuando necesitas que **dos procesos que no son padre e hijo** se comuniquen, usas **FIFOs** (también llamados Pipes con nombre).

> Un FIFO es **un archivo especial en el sistema de archivos**. Se puede abrir, leer y escribir como un fichero normal, pero la comunicación sigue siendo como una tubería: se escribe por un lado y se lee por otro, y **los datos desaparecen al ser leídos**.

#### **Crear un FIFO desde terminal**

```c
mknod FIFO1 p   # Crear un FIFO llamado FIFO1
```

Después puedes usar comandos como:

```c
cat FIFO1       # Espera leyendo del FIFO
```

en una ventana, y en otra:

```c
ls > FIFO1      # Escribe la salida del comando ls en el FIFO
```

#### **Crear un FIFO desde C**

```c
#include <sys/types.h>
#include <sys/stat.h>

mknod("FIFO1", S_IFIFO | 0644, 0);
```

- "FIFO1": nombre del archivo.
    
- S_IFIFO | 0644: indica que es un FIFO y los permisos.
    
- 0: parámetro que se ignora en este caso.

---

### **Problema de comunicación bidireccional**

Tanto en Pipes normales como en FIFOs, la comunicación es **unidireccional** por defecto. Si quieres que dos procesos **se envíen mensajes en ambos sentidos**, necesitas **dos Pipes**: uno para cada dirección.

---

## Comunicación entre procesos (Resumen general)

### Formas de comunicación entre procesos en Linux

- **Pipes**: permiten comunicación entre procesos (normalmente padre-hijo) como si fueran archivos.
    
- **FIFOs**: similar a los Pipes, pero permiten comunicación entre procesos independientes.
    
- **Colas de mensajes, semáforos y memoria compartida**: otros métodos (no se detallan aquí).
    

---

## 1. Pipes (Tuberías)

Un **Pipe** actúa como un archivo temporal:

- Un proceso **escribe** en un extremo.
    
- Otro proceso **lee** del otro extremo.
    
- Normalmente usado **entre procesos padre e hijo**.


### Crear un Pipe en C

```c
#include <unistd.h>

int fd[2];
pipe(fd);
```

- `fd[0]` es para **leer**.
    
- `fd[1]` es para **escribir**.
    

### Leer y escribir en el Pipe

```c
read(fd[0], buffer, tamaño);
write(fd[1], buffer, tamaño);
```

**Importante**:

- Cada proceso debe **cerrar** el descriptor que no va a usar.
    
- La comunicación es **unidireccional**.
    

---

### Ejemplo simple de comunicación padre ↔ hijo

**Proceso hijo escribe** "Hola papi" → **Proceso padre lee** el mensaje:

```c
pipe(fd);
pid = fork();

if (pid == 0) { // Hijo
    close(fd[0]);
    write(fd[1], "Hola papi", 10);
} else { // Padre
    close(fd[1]);
    read(fd[0], buffer, 10);
    printf("Mensaje: %s\n", buffer);
}
```

---

## 2. FIFOs (Pipes con nombre)

Un **FIFO** es un archivo especial que permite a **cualquier proceso** abrirlo para leer o escribir, aunque **no sean padre e hijo**.

### Crear un FIFO

Desde terminal:

```bash
mknod FIFO1 p
```

Desde C:

```c
#include <sys/types.h>
#include <sys/stat.h>

mknod("FIFO1", S_IFIFO | 0644, 0);
```

### Funcionamiento

- Un proceso puede **esperar leyendo** del FIFO.
    
- Otro proceso puede **escribir** en el FIFO.

### Ejemplo sencillo

Terminal 1:

```bash
cat FIFO1
```

Terminal 2:

```bash
ls > FIFO1
```

(El primer terminal mostrará el resultado del comando `ls`.)

---

## 3. Comunicación en ambos sentidos (avi, pare, net)

Cuando se necesita comunicación **en ambas direcciones**, hacen falta **dos Pipes**:

- Uno para enviar de **padre a hijo**.
    
- Otro para enviar de **hijo a padre**.
    

En un ejemplo más avanzado, se creó una estructura con **abuelo, padre y nieto**, donde cada uno enviaba y recibía mensajes usando dos Pipes (`fd1` y `fd2`).

---

## 4. Ejercicios prácticos (creación y sincronización de procesos)

**Práctica 6**:  
Programa en C donde:

- El hijo escribe "Soy el hijo" 10 veces.
    
- El padre escribe "Soy el padre" 10 veces.
    
- El padre espera al hijo y muestra "Mi hijo ha terminado".

**Práctica 7**:  
Crear un proceso padre que genera **tres hijos**.  
Cada hijo imprime:

> "Soy el hijo X, mi padre es PID=Y, yo soy PID=Z"

**Práctica 8**:  
Parecido al anterior, pero:

- El padre genera dos hijos.
    
- Uno de esos hijos genera a su vez un "nieto".
    

**Práctica 9**:  
Programa donde puedes **elegir desde el teclado** qué proceso se ejecuta primero:

- Si eliges `1`, primero proceso 1 y luego proceso 2.
    
- Si eliges `2`, primero proceso 2 y luego proceso 1.


