1. Crear en MySQL esta base de datos

```sql
CREATE TABLE departamentos (dept_NO INT NOT NULL PRIMARY KEY, dnombre VARCHAR(15),loc VARCHAR(15));
```
```sql
CREATE TABLE empleados (Emp_no INT NOT NULL PRIMARY KEY, apellido VARCHAR(20), oficio VARCHAR(15), dir INT, fecha_alta DATE, salario FLOAT(6,2), comision FLOAT(6,2), dept_NO INT, FOREIGN KEY (dept_NO) REFERENCES departamentos (dept_NO));
```

2. Crear proyecto de Maven con JAVA 17
3. Añadir dependencias. 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
             
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

4. Create the Hibernate Configuration File (cfg.xml)
- File > New > Other > Hibernate > Hibernate
- Name: Nombre proyecto + config
- Main > Type: Anotations (jdk)
- Main > Hibernate version: lower 5.0
- Main > Proyect: Nombre proyecto
- Main > Database Connection: Hibernate configure connection
- Main > Configuration file: proyect/src/main/java/
- Option > Database Dialect: MySQL

5. Create Reverse Engineering file (reveng.xml)
- File > New > Other > Hibernate > Hibernate Reverse
	- Engineering File (hibernate.reveng.xml)
- Hibernate Reverse Engineering Editor
- Table Filters Tab > Refresh
- Database schema > Choose Tables to include (biblio/books)
- Source: Puedes ver el archivo

6. Create the Hibernate Code Generations Configurations
- Run > Hibernate code generation
- Click New Configuration
- Put name
- Main > 
	- Output directory: root of the code
	- Choose package: as convention package of persistent classes is called entity
	- Choose reveng.xml file
- Exporters > General settings Generate EJB3 annotations: generates annotations
- Exporters > Exporters > 
	- Domain code (.java): generates class code
	- Hibernate XML Configuration: modifies .cfg.xml to include the mappings

7. Fix bugs and warnings in persistent classes
- Replace javax by jakarta or viceversa
- Solve Serializable warning: Add default serial version ID
- Declare type for Set
- Check cfg.xml file is mapping the classes and the path is correct
- Pay attention to relations between classes
	- Authors contains a Set`<Books>` 
	- Books contains an Author object
- FK is solved and all objects are related using Object Oriented paradigm

8. JPA Annotation
- Automatic generation writes annotations before getters and setters
	- It is recommended to move annotations near attributes declaration
	- t is easier to read and detect errors
9. Check mappings with classes in Hibernate Configuration File
10. Create the functionalities of your project

# Many to Many Relations

1. Create a New Project
2. Map the tables to persistent classes with Hibernate
3. When reverse engineering, select 3 tables
4. In Code Generation Configuration: ensure Detect many-to-many tables is selected