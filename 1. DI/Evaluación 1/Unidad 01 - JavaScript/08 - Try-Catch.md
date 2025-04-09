# Manejo de Excepciones (Try/Catch)

**Concepto:**  
El manejo de excepciones permite controlar errores en tiempo de ejecución mediante el uso de _throw_ para lanzar excepciones y _try/catch_ para capturarlas.

**Ejemplo en una función tradicional:**

```javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error("División por cero");
  }
  return a / b;
}

try {
  let resultado = divide(10, 0);
  console.log("Resultado:", resultado);
} catch (error) {
  console.error("Error:", error.message);
}
```

**Ejemplo en una función asíncrona con try/catch y async/await:**

```javascript
async function fetchData(url) {
  try {
    let response = await fetch(url);
    if (!response.ok) {
      throw new Error("Error en la solicitud");
    }
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error al obtener datos:", error.message);
  }
}

fetchData("https://api.example.com/data");
```

> **Anotación:**
> 
> - En el primer ejemplo, la función _divide_, lanza un error si se intenta dividir por cero, que se captura con _try/catch_.
>     
> - En el segundo, se usa _async/await_ para manejar operaciones asíncronas y se controla cualquier error en la solicitud usando _try/catch_.