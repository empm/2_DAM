# Dependencias

```xml
<dependency>
<groupId>org.mongodb</groupId>
<artifactId>mongodb-driver-sync</artifactId>
<version>4.11.1</version>
</dependency>
```

# **🔗 Conectando con MongoDB en Java**

## 1. ¿Cómo conectar con MongoDB?

 La conexión básica se hace con:

```java
MongoClient client = MongoClients.create();
```

Si no pasamos argumentos, se conecta automáticamente a **mongodb://localhost:27017**, que es el puerto estándar de MongoDB en nuestra máquina.


## 2. Personalizando la Conexión

Podemos configurar la conexión con diferentes opciones, como:

• **Otra dirección** (cuando el servidor está en otra máquina o en la nube).
• **Autenticación** (si la base de datos requiere usuario y contraseña).
• **Configuraciones avanzadas** (como tiempo de espera o número de conexiones).

Ejemplo de conexión con URL personalizada:

```java
MongoClient client = MongoClients.create("mongodb://usuario:contraseña@servidor:puerto");
```


## 3. Cerrar la Conexión

Cuando terminamos de usar la base de datos, **siempre** debemos cerrar la conexión para liberar recursos:

```
client.close();
```

Esto es importante porque si dejamos conexiones abiertas sin usarlas, podríamos afectar el rendimiento del sistema.


---

# 🔍 Trabajando con Bases de Datos y Colecciones en MongoDB con Java

En este apartado aprenderemos cómo manejar bases de datos y colecciones en MongoDB usando Java. Vamos a desglosar cada punto de manera clara y sencilla.

## 1. Obtener los nombres de las bases de datos disponibles

Para listar todas las bases de datos en un servidor MongoDB, usamos:

```java
MongoIterable<String> dbNames = client.listDatabaseNames();
for (String name : dbNames) {
    System.out.println(name);
}
```

#### 🔹 **¿Qué es `MongoIterable<String>`?**

> Es una estructura iterable de MongoDB que nos permite recorrer los resultados de una consulta.


## 2. Obtener una base de datos específica  

Para acceder a una base de datos en MongoDB, usamos:

```
String dbName = "sample_mflix";
MongoDatabase db = client.getDatabase(dbName);
```

Una vez tenemos la base de datos, podemos usar varios métodos útiles:

| **Método**                | **Descripción**                        |
| ------------------------- | -------------------------------------- |
| db.getName()              | Obtiene el nombre de la base de datos. |
| db.getCollection(colName) | Obtiene una colección específica.      |
| db.getCollectionNames()   | Obtiene toda la colección.             |
| db.drop()                 | Elimina la base de datos.              |

⚠️ **Importante**: MongoDB **no crea la base de datos** hasta que insertamos un documento en alguna colección.


## 3. Obtener una colección
 
Para acceder a una colección dentro de una base de datos:

```
MongoCollection<Document> col = db.getCollection("movies");
```

>[! Dato clave:] 
>Si la colección no existe, **MongoDB la creará automáticamente** cuando insertes el primer documento.


## 4. Operaciones CRUD en una colección

La clase `MongoCollection<Document>` nos permite realizar operaciones **CRUD** (Create, Read, Update, Delete):

|**Método**|**Descripción**|
|---|---|
|col.insertOne(doc)|Inserta un solo documento.|
|col.insertMany(docs)|Inserta múltiples documentos.|
|col.find(filter)|Busca documentos según un filtro.|
|col.updateOne(filter, updateDoc)|Modifica un documento.|
|col.updateMany(filter, updateDoc)|Modifica múltiples documentos.|
|col.deleteOne(filter)|Elimina un documento.|
|col.deleteMany(filter)|Elimina varios documentos.|
|col.drop()|Borra la colección.|
|col.countDocuments()|Cuenta la cantidad de documentos en la colección.|


## 5. Trabajando con Documentos (org.bson.Document)

Un documento en MongoDB es similar a un objeto JSON. Para crearlo:

```java
import org.bson.Document;

Document doc = new Document()
        .append("titulo", "El Padrino")
        .append("genero", Arrays.asList("Aventura", "Fantasia"))
        .append("año", 1972)
        .append("director", "Francis Ford Coppola");
```

#### 🔹 Resultado

```json
{
	"titulo": "El Padrino",
	"genero": [
		"Aventura",
		"Fantasia"
	],
	"año": 1972,
	"director": "Francis Ford Coppola"
}
```

#### **🔍 Obtener valores de un documento**

Podemos recuperar valores con get() o los métodos getXXX():

```java
String titulo = doc.getString("titulo");
int año = doc.getInteger("año");
System.out.println("Título: " + titulo + ", Año: " + año);
```


## 6. Convertir Documento a Texto

Para imprimir el documento en formato JSON:

```java
System.out.println(doc.toJson());
```

---
## **🛠 Ejemplo Completo**

Ejemplo de cómo conectar con MongoDB, obtener una base de datos, una colección y agregar un documento:

```java
import com.mongodb.client.*;
import org.bson.Document;

public class MongoDBExample {
    public static void main(String[] args) {
        // Conectar a MongoDB
        MongoClient client = MongoClients.create("mongodb://localhost:27017");

        // Obtener una base de datos
        MongoDatabase db = client.getDatabase("cine");

        // Obtener una colección
        MongoCollection<Document> col = db.getCollection("peliculas");

        // Crear un documento
        Document doc = new Document()
                .append("titulo", "El Padrino")
                .append("año", 1972)
                .append("director", "Francis Ford Coppola")
                .append("genero", "Drama");

        // Insertar el documento
        col.insertOne(doc);

        // Imprimir el documento insertado
        System.out.println("Documento insertado: " + doc.toJson());

        // Cerrar la conexión
        client.close();
    }
}
```

🔹 **Recordatorio**: MongoDB no crea la base de datos o la colección hasta que insertamos el primer documento.

---

# **🚀 Inserción y Consulta de Datos en MongoDB con Java**

## 1. Insertar Documentos en MongoDB

Para agregar datos en una colección, usamos `insertOne` (para un solo documento) o `insertMany` (para varios).

📌 Insertar una Película en la Base de Datos mflix

```java
import com.mongodb.client.*;
import org.bson.Document;
import java.util.Arrays;

public class MongoInsertExample {
    public static void main(String[] args) {
        MongoClient client = MongoClients.create("mongodb://localhost:27017");
        MongoDatabase db = client.getDatabase("mflix");
        MongoCollection<Document> col = db.getCollection("movies");

        // Insertar un solo documento
        Document movie1 = new Document()
                .append("title", "Inception")
                .append("year", 2010)
                .append("director", "Christopher Nolan")
                .append("genre", Arrays.asList("Action", "Sci-Fi"));

        col.insertOne(movie1);
        System.out.println("Película insertada con éxito.");

        client.close();
    }
}
```

📌 Insertar Múltiples Películas

``` java
Document movie2 = new Document()
        .append("title", "Interstellar")
        .append("year", 2014)
        .append("director", "Christopher Nolan")
        .append("genre", Arrays.asList("Adventure", "Drama", "Sci-Fi"));

Document movie3 = new Document()
        .append("title", "The Dark Knight")
        .append("year", 2008)
        .append("director", "Christopher Nolan")
        .append("genre", Arrays.asList("Action", "Crime", "Drama"));

col.insertMany(Arrays.asList(movie2, movie3));
System.out.println("Múltiples películas insertadas.");
```


## 2. Buscar Documentos con find()

Para recuperar datos, usamos find(). Si no pasamos parámetros, devuelve **todos los documentos**.

**📌 Obtener Todas las Películas**

```java
FindIterable<Document> result = col.find();
for (Document doc : result) {
    System.out.println(doc.toJson());
}
```

**📌 Buscar una Película Específica**

```java
import com.mongodb.client.model.Filters;

Document jurassicWorld = col.find(Filters.eq("title", "Jurassic World")).first();
System.out.println(jurassicWorld.toJson());
```

## 3. Aplicando Filtros en las Consultas

Podemos hacer consultas más avanzadas con **filtros** (Filters).

| **Filtro**               | **Descripción**                                                 |
| ------------------------ | --------------------------------------------------------------- |
| eq("campo", valor)       | Busca documentos con un campo que tenga cierto valor.           |
| gte("campo", valor)      | Busca documentos donde el campo sea **mayor o igual** al valor. |
| lte("campo", valor)      | Busca documentos donde el campo sea **menor o igual** al valor. |
| exists("campo", false)   | Busca documentos que **no** tengan un campo.                    |
| regex("campo", "patrón") | Busca documentos que coincidan con una expresión regular.       |
| and(filtro1, filtro2)    | Combinación de filtros con **Y**.                               |
| or(filtro1, filtro2)     | Combinación de filtros con **O**.                               |
|                          |                                                                 |

#### **📌 Ejemplos de Búsquedas Avanzadas**

1️⃣ **Películas del año 2016**

```java
FindIterable<Document> result = col.find(Filters.eq("year", 2016));
result.forEach(doc -> System.out.println(doc.toJson()));
```

2️⃣ **Películas entre 2015 y 2016 (inclusive)**

```java
FindIterable<Document> result = col.find(Filters.and(
    Filters.gte("year", 2015),
    Filters.lte("year", 2016)
));
result.forEach(doc -> System.out.println(doc.toJson()));
```

3️⃣ **Películas donde year es un string**

```java
FindIterable<Document> result = col.find(Filters.type("year", "string"));
result.forEach(doc -> System.out.println(doc.toJson()));
```

4️⃣ **Películas sin el campo plot**

```java
FindIterable<Document> result = col.find(Filters.exists("plot", false));
result.forEach(doc -> System.out.println(doc.toJson()));
```

5️⃣ **Películas rodadas en España**

```java
FindIterable<Document> result = col.find(Filters.eq("countries", "Spain"));
result.forEach(doc -> System.out.println(doc.toJson()));
```

6️⃣ **Películas con un solo actor y del género “Biography”**

```java
FindIterable<Document> result = col.find(Filters.and(
    Filters.size("cast", 1),
    Filters.eq("genre", "Biography")
));
result.forEach(doc -> System.out.println(doc.toJson()));
```

7️⃣ **Películas en inglés y español**

```java
FindIterable<Document> result = col.find(Filters.all("languages", Arrays.asList("English", "Spanish")));
result.forEach(doc -> System.out.println(doc.toJson()));
```

8️⃣ **Películas dirigidas por Spielberg (búsqueda con regex)**

```java
FindIterable<Document> result = col.find(Filters.regex("director", "Spielberg"));
result.forEach(doc -> System.out.println(doc.toJson()));
```

9️⃣ **Películas dirigidas por Spielberg O Kubrick**

```java
FindIterable<Document> result = col.find(Filters.or(
    Filters.regex("director", "Spielberg"),
    Filters.regex("director", "Kubrick")
));
result.forEach(doc -> System.out.println(doc.toJson()));
```

🔟 **Películas con más de 7 premios y al menos 9 en IMDB**

```java
FindIterable<Document> result = col.find(Filters.and(
    Filters.gt("awards.wins", 7),
    Filters.gte("imdb.rating", 9)
));
result.forEach(doc -> System.out.println(doc.toJson()));
```


## 4. Proyección: Seleccionar Campos Específicos


Por defecto, find() devuelve todos los campos. Podemos usar **proyección** para elegir qué mostrar.

  

**📌 Solo título, año y directores, ocultando _id**

```java
Document proj = new Document("title", 1)
        .append("year", 1)
        .append("director", 1)
        .append("_id", 0);

FindIterable<Document> result = col.find().projection(proj);
result.forEach(doc -> System.out.println(doc.toJson()));
```

**📌 Mostrar todo excepto directors y fullplot**

```java
Document proj = new Document("directors", 0)
        .append("fullplot", 0);

FindIterable<Document> result = col.find().projection(proj);
result.forEach(doc -> System.out.println(doc.toJson()));
```


## **✅ Resumen**

1. **Insertar datos** con insertOne() y insertMany().
2. **Recuperar documentos** con find().
3. **Filtrar datos** con Filters (búsquedas avanzadas).
4. **Usar proyecciones** para seleccionar qué campos mostrar.
