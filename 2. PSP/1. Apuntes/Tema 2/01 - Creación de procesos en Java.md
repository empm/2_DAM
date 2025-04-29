## 1. Clases importantes: `Runtime` y `Process`

- **`Runtime`** representa el entorno de ejecución de una aplicación Java.
    
- Para trabajar con procesos:
    
    - `Runtime.getRuntime()` → devuelve el objeto `Runtime`.
        
    - `Runtime.exec(String comando)` → ejecuta un comando externo (nuevo proceso) y devuelve un objeto `Process`.

## 2. Ejecutar programas externos

- **Ejemplo sencillo**: ejecutar el **Notepad** en Windows o **gedit** en Linux.
    
- Se crea el proceso con `exec()`.


```java
Runtime r = Runtime.getRuntime();
Process p = r.exec("notepad");
```

- Si el comando no es un programa gráfico, como `dir` o `ls`, no veremos su salida directamente.


## 3. Leer la salida de un proceso

- Usamos `getInputStream()` del `Process` para capturar lo que el proceso escribe en pantalla:

```java
InputStream is = p.getInputStream();
BufferedReader br = new BufferedReader(new InputStreamReader(is));

String linea;
while ((linea = br.readLine()) != null) {
    System.out.println(linea);
}
```

- **waitFor()** hace que nuestro programa espere hasta que el proceso externo termine.

## 4. Leer errores del proceso

- Si hay errores (por ejemplo, comando mal escrito), se pueden capturar con `getErrorStream()`:

```java
InputStream errores = p.getErrorStream();
BufferedReader brErrores = new BufferedReader(new InputStreamReader(errores));
```

Así podemos mostrar los mensajes de error que produzca el proceso.

## 5. Redireccionar la salida a un archivo

- `exec()` no permite directamente redirigir como en un terminal (`>`).
    
- Para guardar resultados en archivos, usamos:    

```java
FileOutputStream fos = new FileOutputStream("salida.txt");
PrintWriter pw = new PrintWriter(fos);
pw.println("texto");
pw.close();
```

- Se puede modificar el flujo de salida del proceso usando programación en Java.


## 6. Enviar datos a un proceso

- `getOutputStream()` permite **escribir** en el proceso externo.
    
- Ejemplo:
    
    - Ejecutar `date` en Windows.
        
    - Cambiar contraseña con `passwd` en Linux.


```java
OutputStream os = p.getOutputStream();
PrintWriter pw = new PrintWriter(os);
pw.println("datos a enviar");
pw.flush();
```

## 7. Actividades propuestas

- **T2S1P1Quasibash**: programa que ejecuta cualquier comando introducido por el usuario.
    
- **T2S1P2tasklistGuarda**: guardar los procesos en ejecución (`ps -ef` en Linux o `tasklist /v` en Windows) en un fichero `procesos.txt`.
    
- **T2S1P3CridaLectura**: programa que llama a otro y le envía una cadena de texto (por ejemplo, "Hola mundo").