# Procesos del sistema - `ps` 

> Muestra la lista de procesos del sistema

```bash
ps [-Opciones]
```

## Opciones
- `-a` : Procesos de cualquier usuario asociados a terminal
- `-l` : Formato largo
- `-u [uid]`: Formato usuario 
- `-U` : Formato recursos sistema
- `-x` : Procesos no asociados a ningún usuario
- `axu`

# `pstree`

> Muestra la jerarquía de los procesos en estructura de árbol.

```bash
pstree
```

## Opciones

- -a Inclou en l'arbre de processos la línia de comandos que s'use per a iniciar el procés.
- -c Deshabilita la unió de processos fills amb el mateix nom (repliques d'un mateix procés).
- -G Usa els caràcters de línia per a dibuixar l'arbre. La representació de l'arbre és més
- clara, però no funciona en redirigir l'eixida.
- -h Remarca la jerarquia del procés actual (normalment el terminal). No funciona en
- redirigir l'eixida.
- -n Per defecte els processos amb mateix pare s'ordenen pel nom. Aquesta opció força a
- ordenar els processos pel seu PID.
- -p Inclou el PID dels processos en l'arbre.

# `top`

> Lista de procesos live

```bash
top
```

## Opciones
- `top -i`: Ignora los procesos no activos

# `kill`

> Matar procesos

```bash
kill [PID]
kill -SIGKILL [PID]
```

# Ejecutar en primer plano

## Ejemplo:

```bash
firefox
```

# Ejecutar en segundo plano

## Ejemplo:

```bash
firefox &
```
# `nice`

> Darle prioridad a un proceso


# `sleep`

```bash
sleep [segundos]
```

## Ejemplo en primer plano:

```bash
sleep 5; ls
```
## Ejemplo en segundo plano:

```bash
(sleep 60; ls /home/eperez) &
```

