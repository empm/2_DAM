# 1. Agregar dependencias
Agregas **mongodb-driver** a las dependencias (**pom.xml**):
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>

<!-- Este apartado depende de cada proyecto -->
<groupId>pruebaMongo</groupId>
<artifactId>pruebaMongo</artifactId>
<version>0.0.1-SNAPSHOT</version>

<!--Esto es lo importante -->
<dependencies>
	<dependency>
		<groupId>org.mongodb</groupId>
		<artifactId>mongodb-driver-sync</artifactId>
		<version>4.11.1</version>
	</dependency>
</dependencies>

</project>
```
# 2. Conectar con mongo  en la clase

- Conectamos con el servidor, si no se especifican los argumentos, conecta con localhost.
- Al finalizar siempre debemos cerrar
- MongoIterable se usa para iterar por los resultados de las peticiones:
```java
package pruebaMongo;

import java.util.Arrays;
import org.bson.Document;
import org.bson.conversions.Bson;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoIterable;
import com.mongodb.client.model.Filters;

public class principal {
	public static void main(String[] args) {
	
		// CONEXION MONGO
		String connectionString = "mongodb://localhost:27017"; // por defecto
		MongoClient client = MongoClients.create(connectionString);
		
		// MUESTRA DBS
		MongoIterable<String> names = client.listDatabaseNames();
		String res = "Available Databases: ";
		for (String name : names) {
			res += name + "; ";
		}
		System.out.println(res);
		
		// CONECTA DB
		MongoDatabase db = client.getDatabase("mflix");
		
		// MUESTRA COLLECTIONS
		System.out.println("Database name: " + db.getName());
		MongoIterable<String> collections = db.listCollectionNames();
		for (String col : collections) {
			System.out.println("Collection: " + col);
		}
		// Obtener coleccion "movies"
		MongoCollection<Document> movies = db.getCollection("movies");
		// Mostrar todos los documentos de la colección de forma legible
		System.out.println("Primer show:");
		for (Document doc : movies.find()) {
		System.out.println(doc.toJson()); // Imprime el documento en formato JSON
		}
		// Crear nuevo documento (append añade campos a un doc)
		Document newMovie = new Document()
			.append("title", "Data access")
			.append("genere", "drama");
		Document newMovie2 = new Document()
			.append("title", "Data access2")
			.append("genere", "drama");
		Document newMovie3 = new Document()
			.append("title", "Data access3")
			.append("genere", "drama");
			
		// INSERT
		movies.insertOne(newMovie);
		System.out.println("Segundo show:");
		for (Document doc : movies.find()) {
			System.out.println(doc.toJson()); // Imprime los documentos después del insert
		}
		movies.insertMany(Arrays.asList(newMovie2, newMovie3));
		System.out.println("Tercer show:");
		for (Document doc : movies.find()) {
			System.out.println(doc.toJson()); // Imprime los documentos después de insertar múltiples
		}
		// FIND y SORT
		Document sortDoc = new Document("year", 1);
		FindIterable<Document> res2 = movies.find().sort(sortDoc); // todos
		System.out.println("Sort (Primer resultado): " + res2.first().toJson()); // Imprime el primer documento después de ordenar
		// Filtro: documentos sin "year"
		Bson filterDoc = Filters.exists("year", false);
		FindIterable<Document> res3 = movies.find(filterDoc);
		System.out.println("Filtros (Documentos sin 'year'):");
		for (Document doc : res3) {
			System.out.println(doc.toJson()); // Imprime los documentos que coinciden con el filtro
		}
		
		// DELETE (Borrar documentos sin "year")
		Bson filterDoc3 = Filters.exists("year", false); // borrar peliculas sin año
		movies.deleteMany(filterDoc3);
		System.out.println("Ultimo show:");
		for (Document doc : movies.find()) {
			System.out.println(doc.toJson()); // Imprime los documentos después de eliminar
		}
		client.close(); // Cierre explícito del cliente
	}
}
```
