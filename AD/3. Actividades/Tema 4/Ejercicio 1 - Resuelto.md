1. Crear en MySQL esta base de datos

```sql
CREATE TABLE departamentos (dept_NO INT NOT NULL PRIMARY KEY, dnombre VARCHAR(15),loc VARCHAR(15));
```

```sql
CREATE TABLE empleados (Emp_no INT NOT NULL PRIMARY KEY, apellido VARCHAR(20), oficio VARCHAR(15), dir INT, fecha_alta DATE, salario FLOAT(6,2), comision FLOAT(6,2), dept_NO INT, FOREIGN KEY (dept_NO) REFERENCES departamentos (dept_NO));
```

2. Create the project hiberExample and map the following database with Hibernate persistent classes.
- Añadir dependencias

```xml

```



4. The main program should show all departments with its employees