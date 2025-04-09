> Distintas formas de declarar array

## Como objeto `new`

```js
let array = new Array(); // Declara un nuevo array vacio
array[0] = 10; // Asigna valor al indice 0
console.log(a[0]); // Imprime 10
```

## Con corchetes

```js
let array = [1, 2, 3]  // Declaración y asignación
console.log(array) // Imprime "1, 2, 3"
```

## Propiedad lenght

> Indica cuantos elementos tiene dicho array

```js
let array = new Array(10) // Crea un array de tamaño 10
console.log(a.length) // Imprime 10
```

```js
let array = ["a", "b", "c"] // Inicializamos con 3 valores
console.log(array.length) // Imprime 3
```

## Insertar valores

### Insertar al inicio `unshift`

```js
let a = [];
a.unshift("A", "B", "C"); // Inserta valores al inicio
console.log(a) // Imprime "["A", "B", "C"]"
```

### Insertar al final `push`

```js
a.push("a", "b", "c"); // Inserta valores al final
console.log(a); // Imprime "["A", "B", "C", "a", "b", "c"]"
```

## Eliminar valores

### Eliminar al inicio  `shift()`

> Elimina el primer elemento e imprime qué elemento ha eliminado

```js
console.log(a.shift()); 
// Elimina el primer elemento e imprime "A"
```

### Eliminar al final `pop()`

> Elimina el último elemento e imprime qué elemento fue

```js
console.log(a.pop());
// Elimina el último elemento e imprime "c"
```

## Imprimir vectores

### `toString()`

```js
let a = [1, 2 ,3];
console.log(a.toString()); // Imprime "1,2,3"
```

### `join()`

> Devuelve un string con todos los elementos separados por coma.
> **Podemos definir el separador**

```js
let a = [1, 2, 3];
console.log(a.join()); // Default: "1,2,3" (Como toString())
console.log(a.join(" - ")); // Imprime: "1 - 2 - 3"
```

## Concatenar valores `concat`

```js
let a = ["a", "b", "c"];
let b = ["d", "e", "f"];
let c = a.concat(b);
console.log(c); // Imprime "["a", "b", "c", "d", "e", "f"]"
```

> Si imprimimos `a` el array no se ha modificado


## Trocear vectores

### `slice()`

> Nos devuelve un nuevo array a partir de posiciones de otro

```js
let a = ["a", "b", "c", "d", "e", "f"];

let b = a.slice(1, 3); 
// Creamos array con posición de inicio y de fin (incluidas)
console.log(b); // Imprime "["b", "c"]"

console.log(a.slice(3)); 
// Devuelve desde la posición 3 hasta el final
```
#### Slice con un parámetro
> Coge desde la posición (índice) indicada hasta el final
#### Slice con dos parámetros
> Lee posición índice inicial y final (ambas incluídas)


### `splice()`

> Elimina elementos del array original y devuelve los elementos eliminados. Puede también insertar nuevos valores

```js
let a = ["a", "b", "c", "d", "e", "f"];
a.splice(1, 3); 
// Elimina 3 elementos desde la posición 1 hasta la 3
console.log(a); // Imprime "[ 'a', 'e', 'f' ]"
```

#### Insertar sin eliminar
```js
let a = ["a", "b", "c", "d", "e", "f"];
a.splice(1, 0, "g", "h"); 
// Inserta "g" y "h" en la posición 1
```

#### Insertar eliminando
```js
let a = ["a", "b", "c", "d", "e", "f"];
a.splice(1, 1, "g", "h"); 
// Elimina "b" e inserta "g" y "h" en la posición 1
```

## Ordenar vectores

### `reverse()`

```js
let a = ["a", "b", "c", "d", "e", "f"];
a.reverse(); // Hace el reverse del array original
console.log(a); // Imprime ["f", "e", "d", "c", "b", "a"]
```

### `sort()`

```js
let a = ["f", "e", "d", "c", "b", "a"];
a.sort(); // Ordena
console.log(a); // Imprime "['a', 'b', 'c', 'd', 'e', 'f']"
```

#### Ordenar otro tipos de datos

> Esto los ordena "lexicográficamente"

```js
let a = [20, 6, 100, 51, 28, 9]; a.sort(); 
// Ordena el array original 
console.log(a); // Imprime [100, 20, 28, 51, 6, 9]
```

#### Función para ordenar números
```js
a.sort(function(n1, n2) { return n1 - n2; }); console.log(a); // Imprime [6, 9, 20, 28, 51, 100]
```

#### Función para ordenar clave numérica JSON
```js
let datos = [
  { nombre: "Nacho", telefono: "966112233", edad: 40 },
  { nombre: "Ana", telefono: "911223344", edad: 35 },
  { nombre: "Mario", telefono: "611998877", edad: 15 },
  { nombre: "Laura", telefono: "633663366", edad: 17 },
];

datos.sort((a, b) => a.edad - b.edad);
```

#### Función para ordenar clave String en JSON
```js
datos.sort((a, b) => {
    let nA = a.nombre.toLowerCase();
    let nB = b.nombre.toLowerCase();

    if (nA > nB) return 1;
    if (nA < nB) return -1;
    return 0;
});

console.log(datos);
```
## Buscar elementos

### `indexOf()`

> Permite conocer si el valor que le pasamos se encuentra en el array

- Imprime 2: Si encuentra el valor
- Imprime -1: Si no lo encuentra

```js
let a = [3, 21, 15, 61, 9, 15]; 
console.log(a.indexOf(15)); // Imprime 2 
console.log(a.indexOf(56)); // Imprime -1. No encontrado
```

### `lastIndexOf()`

> Nos devuelve la posición de la primera ocurrencia encontrada empezando desde el final. 

```js
let a = [3, 21, 15, 61, 9, 15]; console.log(a.lastIndexOf(15)); // Imprime 5
```

### `every()`

> Devuelve un booleano si todos los elementos del array cumplen cierta condición.

```js
let a = [3, 21, 15, 61, 9, 54]; console.log(a.every(function(num) { 
	return num < 100; })); // Imprime true 
// Comprueba si cada número es menor a 100 

console.log(a.every(function(num) { 
	return num % 2 == 0; })); // Imprime false
// Comprueba si cada número es par 
```

### `some()`

> Devuelve cierto si uno de los elementos cumple la condición

```js
let a = [3, 21, 15, 61, 9, 54]; console.log(a.some(function(num) { 
	return num % 2 == 0; })); // Imprime true
// Comprueba si algún elemento del array es par 
```


## Iterar Array

> Usamos el método **forEach**

> Es importante saber que, si se modifican los elementos de un array en un **forEach** los cambios no se guardan en el array, es decir, no podemos modificar el propio array dentro de un **forEach**.

```js
let a = [3, 21, 15, 61, 9, 54];
let sum = 0;
a.forEach(function (num) {
  sum += num;
});
console.log(sum); // Imprime 163

a.forEach(function (num, indice, array) {
  // índice y array son parámetros opcionales
  console.log("Índice " + indice + " en [" + array + "] es " + num);
});
// Imprime -> Índice 0 en [3,21,15,61,9,54] es 3, Índice 1 en [3,21,15,61,9,54] es 21, ...
```


## Modificar todos los elementos `map()`

> El método **map** recibe una función que transforma cada elemento y lo devuelve. Este método devolverá al final un nuevo array del mismo tamaño conteniendo todos los elementos resultantes.

```js
let a = [4, 21, 33, 12, 9, 54]; console.log(a.map(function(num) { 
	return num*2; 
})); // Imprime [8, 42, 66, 24, 18, 108]
```

## Filtrar los elementos `filter()`

> Filtra los elementos de un array y obtiene como resultado un array que contiene sólo los elementos que cumplan cierta condición.

```js
let a = [4, 21, 33, 12, 9, 54];
console.log(
  a.filter(function (num) {
    return num % 2 == 0;
// Si devuelve true, el elemento se queda en el array
  })
); // Imprime [4, 12, 54]
```

### Crear a partir de otro array filtrando mayores de 18
```js
let datos = [
  { nombre: "Nacho", telefono: "966112233", edad: 40 },
  { nombre: "Ana", telefono: "911223344", edad: 35 },
  { nombre: "Mario", telefono: "611998877", edad: 15 },
  { nombre: "Laura", telefono: "633663366", edad: 17 },
];

let datosFiltrados = datos.filter((a) => a.edad > 30);
console.log(datosFiltrados);
```
## Acumular valores

### `reduce()`

> Usa una función que acumula un valor, procesando cada elemento (segundo parámetro) con el valor acumulado (primer parámetro)

```js
let a = [4, 21, 33, 12, 9, 54]; console.log(a.reduce(function(total, num) { 
// Suma todos los elementos del array 
	return total + num; }, 0)); // Imprime 133 
	console.log(a.reduce(function(max, num) { 
	// Obtiene el número máximo del array 
	return num > max? num : max; }, 0)); // Imprime 54
```

### `reduceRight()`

> Hace lo mismo que reduce pero al revés

``` js
let a = [4, 21, 33, 12, 9, 154]; console.log(a.reduceRight(function(total, num) { 
// Comienza con el último número y resta todos los otros números 
	return total - num; })); 
// Imprime 75 (Si no queremos enviarle un valor inicial, empezará con el valor de la última posición del array
```

## Dividir cadenas `split()`

> Separar string usando un caracter delimitador y creando un array.


```js
let frutas = "manzana,banana,naranja,pera";
let arrayFrutas = frutas.split(","); 
// Divide la cadena en cada coma
console.log(arrayFrutas); 
// Imprime ["manzana", "banana", "naranja", "pera"]
```

> También admite un segundo parámetro opcional que indica cuántos elementos queremos que nos devuelva.

```js
let numeros = "uno,dos,tres,cuatro,cinco";
let primerosTres = numeros.split(",", 3); 
// Separa la cadena en cada coma, pero solo devuelve los primeros 3 elementos
console.log(primerosTres); // Imprime ["uno", "dos", "tres"]
```

## JSON

> El formato JSON nos permite definir objetos y array de objetos en JavaScript.

```js
let datos = [
  { nombre: "Nacho", telefono: "966112233", edad: 40 },
  { nombre: "Ana", telefono: "911223344", edad: 35 },
  { nombre: "Mario", telefono: "611998877", edad: 15 },
  { nombre: "Laura", telefono: "633663366", edad: 17 },
];
```

> Tenemos un array llamado datos con 4 posiciones. 

- Para acceder a una posición del array: `datos[0]`. 
- Para acceder a una propiedad concreta dentro de una posición: `datos[0].edad`. 
- Además podemos usar cualquier método de los vistos anteriormente con array en formato json