> [!NOTE]
> Object-Relational Mapping (ORM) is a tool that translates from relational logic to object logic and viceversa.

# Hibernate

- ORM tool for Java (also available for .NET)
- Mapping between tables and objects using:
	- XML files
	- Annotations in classes
- Data from database is mapped in POJOs (Plain Old Java Objects):
	- Simple classes independent from frameworks

## Instalación de JBoos Tool
1. Desde Eclipse > Help > Marketplace Client, se puede buscar también.
2. Buscar e Instalar `Jboss` 
3. Dejar marcada las casillas por default y completar el proceso de instalación.
4. Reiniciar eclipse
5. Añadir dependencias a `pom.xml`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>com.eperez</groupId>
	<artifactId>Actividad01</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>actividad01</name>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <dependencies>
	<!-- https://mvnrepository.com/artifact/org.hibernate.orm/hibernate-core -->
	<dependency>
   	 <groupId>org.hibernate.orm</groupId>
    	<artifactId>hibernate-core</artifactId>
    	<version>6.5.0.Final</version>
	</dependency>

	<!-- https://mvnrepository.com/artifact/com.mysql/mysql-connector-j -->
	<dependency>
    	<groupId>com.mysql</groupId>
    	<artifactId>mysql-connector-j</artifactId>
    	<version>8.4.0</version>
	</dependency>
    </dependencies>

</project>
```



## Ejercicio 1 Ejemplo

1. Ir a MySQL y crear la tabla biblio.
2. Crear una archivo nuevo dentro de `src/main/java` y con click derecho añadimos un archivo de configuración de hibernate:
	- Nuevo > Otros > Hibernate > HibernateConfigurationFile
3. Rellenar los datos como en el PDF de ejemplo
4. Crear una clase main en `src/main/java` 

```java
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class MainClass {
	public static void main(String[] args) {		
		SessionFactory sf = new Configuration().configure().buildSessionFactory();
		Session session = sf.openSession();
		
		if (session != null) {
			System.out.println("Sesion abierta");
		}
		else {
			System.out.println("Error abriendo sesion");
		}
		System.out.println("END");
	}
}
```
