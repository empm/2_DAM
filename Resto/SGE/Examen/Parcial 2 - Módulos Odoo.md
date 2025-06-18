> Entregar todas las hojas numeradas y con nombre

> Todos los ejercicios deberán de ser entregados en orden (en el caso de no realizarse algún ejercicio, poner el número del ejercicio y dejarlo en blanco).

> Realizar las clases para ODOO13 en el framework de OpenObject cumpliendo los estándares indicados durante el curso.

> El modulo se llamará de la siguiente forma: apellido1 del alumno y las Clases de OpenObject apellido1.clase. El modulo esta basado en el boceto dibujado.

> Como mínimo cada clase en python deberá de tener al menos 7 campos.

# 1) Código python de la clase bomberocamion

> **Hasta 1 punto**


# 2) Clase bombero, en la cual debemos tener al menos cinco de los campos de tipos diferentes:

- ﻿﻿Comprobar que el DNI sea único, y obligatorio
- ﻿﻿Un campo deberá de ser la fecha de nacimiento.
- ﻿﻿Un campo de selección, que indique cual sería el puesto que ocupa en el camion  
    (conductor, copiloto, capitan, bomberoRaso).
- ﻿﻿Por defecto poner el campo puesto como bomberoRaso
- ﻿﻿Ordenar por apellido1
- ﻿﻿Poder ver de alguna forma el camion o camiones en los que ha estado asignado

> **Hasta 1,5 puntos**


# 3) Vista de calendar de la clase bomberocamion.

> **Hasta 1,5 puntos**

- El la cual se marque el evento que simboliza el tiempo que esta en un camión el bombero.
- Recordar que puede haber un inicio y un fin del evento.
- Mostrando, tanto el bombero como el camión al pulsar el ratón sobre el evento


# 4) En vista de calendar de la clase bomberocamion, deseamos que se muestre: 

- El nombre del camión concatenado con el bombero, y no los ids.
- ¿Qué debe de realizarse y cómo?

> **Hasta 1,5 puntos**


# 5) Vista de formulario de clase bombero, de tal forma que se añadan cuantos más elementos de xml mejor (por ejemplo: notebook, y separator, att...)

- ﻿﻿La clase bombero tendrá un campo booleano que diga si tiene carnet de camión, y en tal caso en la *vista de formulario*, habrá un **campo** que será el **número del carnet**, pero que solo será visible si tiene dicho carnet

> **Hasta 1,5 puntos**


# 6) Método en la clase bombero. Tenemos la fecha de nacimiento del bombero. Deseamos tener un campo calculado que nos muestre la edad del bombero.

- Mejorarlo, con un decorador, para que en el formulario se capte que al modificar la fecha cambia también al momento la edad.

> **Hasta 1,5 puntos**

![[Pasted image 20250215113753.png]]


# 7) Mediante herencia de clase, crear la siguiente estructura. 

- El modulo que hereda se llamará apellido1_2
- Código xml de la clase parque de referente al modulo apellido1_2
- Tanto la vista form, como su action y los menuitem
- Indicar, explicar los conceptos

> **Hasta 2 puntos**

![[Pasted image 20250215113735.png]]