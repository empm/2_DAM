# 1. Crear clases
Crea las clases que se correspondan con los documentos de Mongo y añade sus campos.
- lowerCamelCase
- Los atributos deben ser privados
```java 
public class movies {
	private ObjectId id;
	private String titulo;
	private int anio;
	private String plot;
```
# 2. Generar Automaticamente
Ir al menú Source y que eclipse nos genere automaticamente:
- Getters y setters
- ToString
- Constructor con fields (no olvidar crear nosotros el constructor vacío)
![[Pasted image 20250208113452.png]]

```java 
import org.bson.codecs.pojo.annotations.BsonProperty;
import org.bson.types.ObjectId;

public class movie {
	private ObjectId id;
	private String titulo;
	private int anio;
	private String plot;

	// constructor
	public movie() {
		this.id = new ObjectId(); // para que nos genere el id automaticamente
	}

	public movie(String titulo, int anio, String plot) {
		this.id = new ObjectId(); // para que nos genere el id automaticamente
		this.titulo = titulo;
		this.anio = anio;
		this.plot = plot;
	}

@Override
public String toString() {
return "movies [id=" + id + ", titulo=" + titulo + ", anio=" + anio + ", plot=" + plot + "]";
}

	// getters and setters
	public ObjectId getId() {
		return id;
	}
	
	public void setId(ObjectId id) {
		this.id = id;
	}
	
	public String getTitulo() {
		return titulo;
	}
	
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	
	public int getAnio() {
		return anio;
	}
	
	public void setAnio(int anio) {
		this.anio = anio;
	}
	
	public String getPlot() {
		return plot;
	}
	
	public void setPlot(String plot) {
		this.plot = plot;
	}

}

```

==Importante== 
- `@BsonProperty` Mapea un campo con su equivalente en Mongo si su nombre en Java es dsitinto.
```java
public class Movie { 
	private ObjectId id; 
	private String title; 
	// Aquí usamos @BsonProperty para mapear 'release_year' de la base de datos // al campo 'releaseYear' en el POJO Java. 
	@BsonProperty("release_year") 
	private int releaseYear;
	 private String plot;
``` 
# 3. Codec Registry
En una **clase Main**: 
- El codec permite la traducción entre documentos BSON y clases POJO y viceversa.
```java
package pruebaMongoEntidad; 

import com.mongodb.MongoClientSettings;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.codecs.configuration.CodecRegistry;
import org.bson.codecs.pojo.PojoCodecProvider;

import static org.bson.codecs.configuration.CodecRegistries.fromRegistries;
import static org.bson.codecs.configuration.CodecRegistries.fromProviders;


public class Main {
	public static void main(String[] args) {
		// Registro del codec para mapear POJOs
		CodecRegistry pojoCodecRegistry = fromRegistries(
		MongoClientSettings.getDefaultCodecRegistry(),
		fromProviders(PojoCodecProvider.builder().automatic(true).build())
		);
		
		// Conectamos la base de datos con el CODEC
		MongoClient client = MongoClients.create();
		MongoDatabase db = client.getDatabase("mflix").withCodecRegistry(pojoCodecRegistry);
		
		// Usamos el codec con la db
		db = db.withCodecRegistry(pojoCodecRegistry);
		// Asociar a la clase que has creado para guardar los documentos
		MongoCollection<movie> movies = db.getCollection("movies", movie.class);
		
		// Ahora las operaciones las haremos con los pojo class
		// Insertar un POJO
		movie newMovie = new movie("Matrix Reloaded", 2003, "Action-packed sci-fi thriller");
		movies.insertOne(newMovie);

		// Consultar y mostrar películas
		for (movie m : movies.find()) {
			System.out.println(m);
		}
		// FindIterable<movie> findRes = movies.find();
		client.close();
	}
}
```
