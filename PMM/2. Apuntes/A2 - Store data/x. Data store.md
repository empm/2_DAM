
El componente DataStore de Jetpack es una excelente forma de almacenar conjuntos de datos pequeños y simples con baja sobrecarga. 

DataStore tiene dos implementaciones diferentes: `Preferences DataStore` y `Proto DataStore`

- `Preferences DataStore` almacena pares clave-valor. Los valores pueden ser los tipos de datos básicos de Kotlin, como `String`, `Boolean` y `Integer`. No almacena conjuntos de datos complejos. No requiere un esquema predefinido. El caso de uso principal de `Preferences Datastore` es almacenar las preferencias del usuario en su dispositivo.
- `Proto DataStore` almacena tipos de datos personalizados. Requiere un esquema predefinido que asigne definiciones de proto con estructuras de objetos.

### Dependencias

```kotlin
implementation("androidx.datastore:datastore-preferences:1.0.0")
```


