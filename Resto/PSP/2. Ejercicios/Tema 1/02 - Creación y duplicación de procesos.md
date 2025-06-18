# Tres generaciones `T1S2P2TresGeneracions.c`

> Abuelo --- fork () --> Hijo --- fork() --> Nieto

- Realiza un programa llamado `UD1P1TresGeneracions.c`en el que el árbol cubra tres generaciones y la salida deberá tener el orden: Nieto, padre, abuerlo.

- Se ejecutará con:

```shell
$ gcc T1S2P2TresGeneracions.c -o T1S2P2TresGeneracions
$ ./T1S2P2TresGeneracions
"Soc el net (15565, fill de 15564)"
"Soc el pare (15564, fill de 15563)"
"Soc l'avi (15563, fill de 15471)"
$ pgrep bash
15471
```

## Solución

```c
/* 
Realitza un programa anomenat T1S2P2TresGeneracions.c en el qual l'arbre cobrisca tres generacions 
i l'eixida ha de ser contranatura, és a dir, sempre tindrà l'ordre: net, pare, avi. 

L'eixida en executar-ho ha de ser la següent:

	pau:~$ ./*T1S2P2TresGeneracions
	Soc el net (15565, fill de 15564)
	Soc el pare (15564, fill de 15563)
	Soc l'avi (15563, fill de 15471)
	pau:~$ pgrep bash
	15471
*/

#include <sys/types.h> 
#include <unistd.h> 
#include <stdio.h> 
#include <sys/wait.h>
 
int main(int argc, char *argv[]) 
{ 
    pid_t pid1, pid2; 
    int status1, status2; 
    pid1=fork(); 
    if ( pid1== 0 ) { /* PARE */ 
        pid2=fork(); 
        if ( pid2== 0 ) { /* NET */ 
            printf("Soc el net (%d, fill de %d)\n", getpid(), getppid()); 
        }
        else { /* PARE */ 
            waitpid(pid2, &status2, 0);
            printf("Soc el pare (%d, fill de %d)\n",    getpid(), getppid()); 
        }
    } 
    else { /* AVI */ 
         /* Esperem al fill {pare del net} acabe, status 0 */ 
        waitpid(pid1, &status1, 0); 
        printf("Soc l'avi (%d, fill de %d)\n", getpid(), getppid()); 
    }
    return 0; 
} 
```

---

# `T1S2P2Variable.c

- Realitza un programa en C anomenat `T1S2P2Variable.c` que cree un procés (tindrem 2 processos: un pare i un fill). 
- El programa definirà una variable sencera i li donarà el valor 6. 
- El procés pare incrementarà aquest valor en 5 i el fill restarà 5. 
- S'han de mostrar els valors en pantalla. 
- A continuació es mostra exemple de l'execució.

```shell
$ gcc T1S2P2Variable.c -o T1S2P2Variable
$ ./T1S2P2Variable
"Soc el Pare. Valor variable és 11"
"Soc el Fill. Valor variable és 1"
```

 > Explica el resultat del programa (recorda els canvis de contextos explicats en la teoria).
 
## Solución 

```c
/* 
Realitza un programa en C anomenat T1S2P3Variable.c que cree un procés (tindrem 2 processos: un pare i un fill). El programa definirà una variable sencera i li donarà el valor 6. El procés pare incrementarà aquest valor en 5 i el fill restarà 5. S'han de mostrar els valors en pantalla. A continuació es mostra exemple de l'execució.

	pau~/$ ./T1S2P3Variable
	Soc el Pare. Valor variable és 11
	Soc el Fill. Valor variable és 1
*/

#include <sys/types.h> 
#include <unistd.h> 
#include <stdio.h> 
#include <sys/wait.h>
 
int main(int argc, char *argv[]) 
{ 
    pid_t pid;
    int sencer=6;
	pid=fork();
    if ( pid == 0 ) { /* FILL */ 
        sencer = sencer - 5;
		printf("Soc el Pare. Valor variable és %d\n", sencer);
    } 
    else { /* PARE */ 
		sencer = sencer + 5;
        printf("Soc el Fill. Valor variable és %d\n", sencer); 
    } 
    return 0; 
}
```