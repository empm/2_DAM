# Hola Mundo en C

```c
#include <stdio.h>
int main( int argc, char *argv[] )
{
printf( "Hola, món!\n");
return 0;
}
```

## Compilar 

```shell
gcc T1S2Exemple1HolaMon.c -o T1S2Exemple1HolaMon
```

## Ejecutar

```shell
./T1S2Exemple1HolaMon
```

## Posibles dependencias

```shell
sudo aptitude install libc-dev g++ build-essential
```


# Creación y duplicación

## `fork()`

```c
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
int main(int argc, char *argv[])
{
	pid_t pid;
	pid=fork();
	if ( pid == 0 ){
	 /* fill */
		printf("Soc el fill (%d, fill de %d)\n", getpid(), getppid());
	}
	else { 
		/* pare */
		printf("Soc el pare (%d, fill de %d)\n", getpid(), getppid());
	}
	return 0;
}
```

- Se diferencia un padre de un hijo porque el hijo recibe un PID con valor 0.

``` bash
Soc el pare (569, fill de 314)
Soc el fill (570, fill de 569)

$ pgrep bash
314
```

- La salida de imprimir por pantalla, es asíncrona, podría haberse ejecutado antes el proceso del padre.

- El padre, es hijo del PID de la shell en la que está corriendo `314`.

- Es posible que la ejecución del padre termine antes de que el hijo sepa quien es su padre. Para que no ocurra:

```c
pid_t wait(int *status)
pid_t waitpid(pid_t pid, int *status, int options);
```

### Ejemplo dos hijos

```c
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
	pid_t pid1, pid2;
	int status1, status2;
	pid1=fork();
	if ( pid1== 0 )
	{ /* fill */
		printf("Soc el primer fill (%d, fill de %d )\n", getpid(), getppid());
	}
	else
	{ /* pare */
		pid2=fork();
		if ( pid2 == 0 )
		{ /* segon fill */
			printf("Soc el segon fill (%d, fill de %d )\n", getpid(), getppid());
		}
		else
		{ /* pare */
			/* Esperem al primer fill acabe, status 0*/
			waitpid(pid1, &status1, 0);
			/* Esperem al segon fill acabe, status 0 */
			waitpid(pid2, &status2, 0);
			printf("Soc el pare (%d, fill de %d)\n", getpid(), getppid());
		}
	}
	return 0;
}
```


Salida:

```bash
Soc el primer fill (15503, fill de 15502)
Soc el segon fill (15504, fill de 15502)
Soc el pare (15502, fill de 15471)
$ pgrep bash
15471
```

- Con `waitpid` nos aseguramos de que el padre esperará a sus dos hijos antes de continuar.
- Si ejecutamos varias veces el código, el segundo hijo podría terminar antes que el primero.