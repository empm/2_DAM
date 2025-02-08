> [!NOTE]
> Object-Relational Mapping (ORM) is a tool that translates from relational logic to object logic and viceversa.

# Hibernate

- ORM tool for Java (also available for .NET)
- Mapping between tables and objects using:
	- XML files
	- Annotations in classes
- Data from database is mapped in POJOs (Plain Old Java Objects):
	- Simple classes independent from frameworks

## Instalación de JBoss Tools
1. Desde Eclipse > Help > Marketplace Client, se puede buscar también.
2. Buscar e Instalar `Jboss` 
3. Dejar marcada las casillas por default y completar el proceso de instalación.
4. Reiniciar eclipse
5. Añadir dependencias a `pom.xml` (se forma cuando se crea el proyecto)

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

Este es el de JORGE

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.4.1</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.example</groupId>
    <artifactId>SpringProyecto</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>SpringProyecto</name>
    <description>Demo project for Spring Boot</description>
    <url/>
    <licenses>
        <license/>
    </licenses>
    <developers>
        <developer/>
    </developers>
    <scm>
        <connection/>
        <developerConnection/>
        <tag/>
        <url/>
    </scm>
    <properties>
        <java.version>17</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.hibernate</groupId>
            <artifactId>hibernate-core</artifactId>
            <version>6.6.4.Final</version>
        </dependency>
        <dependency>
            <groupId>org.hibernate.common</groupId>
            <artifactId>hibernate-commons-annotations</artifactId>
            <version>6.0.0.Final</version> <!-- Asegúrate de que la versión sea compatible -->
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>com.mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```



## Ejercicio 1 Ejemplo

1. Ir a MySQL y crear la tabla biblio.
2. Creas tu proyecto maven en eclipse.
3. Añadir dependencias a `pom.xml` (se forma cuando se crea el proyecto).
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
4.  Crear una archivo nuevo dentro de `src/main/java` y con click derecho añadimos un archivo de configuración de hibernate:
	- Nuevo > Otros > Hibernate > **HibernateConfigurationFile**
5. Rellenar los datos como en el PDF de ejemplo:
	1. Database dialect: MySQL
	2. Driver: com.mysql.jdbc.Driver
	3. Connection URL: jdbc:mysql://*hostname*/*database*
	4. Username: root
	5. Password: root
6. Crear una clase main en `src/main/java` 

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

# POJOS (Persistent Classes)
Cómo crearlas desde Hibernate?
## 1. Console Configuration
1. File > New > Other > Hibernate > **Hibernate Console Configuration**
	1. En Main: 
		1. Version de Hibernate 4.3
		2. DB connections: configured connection (la Configuration file que creamos antes cfg.xml)
	2. En Options: Db dialect MySQL
## 2. Reverse Engineering file
1. File > New > Other > Hibernate > Hibernate  Reverse Engineering File
2. Refresh **Table Filters**
3. Selecciona las tablas que quieras incluir
4. Finish, puedes ver el codigo con el editor simple
## 3. Code Generation Configuration
1. Run : Hibernate Code Generation Configuration
2. New Configuration (name: HibernateAnnotations).
3. Main:
	1. Output dir: src/main/java/
	2. Check reverse engineer
	3. Package: name_project.**entity**
	4. proyecto/src/main/java/**hibernate.reveng.xml** file. Este archivo  ya esta creado.
4. Exporters
	1. Generate EJB3 annotations
	2. Domain code
	3. HIbernate XML configuration
## 4. Correct errors
En los archivos del paquete .entity:
1. Reemplazar JAVAX por JACKARTA
2. Serializable warning: add default serial version ID
3. Declare type for Set.
4. Check cfg.xml file is mapping the classes and the path is correct *(a mi me sale entity y a el le sale model)*.

## Comprobar que funciona bien
Añadir funciones Show y llamarlas desde el main.
Importaciones para realizar las querys:
```java
import org.hibernate.query.Query;
```

# SUMMARY
1. Build the database
2. Create Maven project and change to Java 17
3. Add the dependencies to the pom file
4. Create the Hibernate Configuration File cfg.xml
5. Create the Hibernate Console Configuration
6. Create the Hibernate Reverse Engineering File reveng.xml
7. Create the Hibernate Code Generations Configurations
8. Fix bugs and warnings in persistent classes
9. Check mappings with classes in Hibernate Configuration File
10. Create the functionalities of your project