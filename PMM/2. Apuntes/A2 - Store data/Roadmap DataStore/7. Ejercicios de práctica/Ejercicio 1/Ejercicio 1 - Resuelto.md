## **✅ Ejercicio 1: Guardar y leer un valor booleano**

📌 **Objetivo:**  
Crear un DataStore para guardar y leer el **estado del modo avión** (`airplane_mode`).

### **📍 Paso 1: Crear la clase `AirplaneModeDataStore`**

```kotlin
class AirplaneModeDataStore(private val context: Context) {
```

📌 **Explicación:**

- Definimos una clase `AirplaneModeDataStore` que recibe un `Context` para acceder a DataStore.

---

### **📍 Paso 2: Definir una clave para almacenar la preferencia**

```kotlin
companion object {
    private val AIRPLANE_MODE_KEY = booleanPreferencesKey("airplane_mode")
}
```

📌 **Explicación:**

- **`companion object`** permite definir una constante estática.
- **`booleanPreferencesKey("airplane_mode")`** crea una clave de tipo `Boolean`.

---

### **📍 Paso 3: Implementar el método `saveAirplaneMode()`**

```kotlin
suspend fun saveAirplaneMode(isEnabled: Boolean) {
    context.dataStore.edit { preferences ->
        preferences[AIRPLANE_MODE_KEY] = isEnabled
    }
}
```

📌 **Explicación:**

- `suspend fun`: La función es **suspendida** porque `edit {}` debe ejecutarse en una corrutina.
- `edit {}` abre una transacción atómica y almacena el valor en DataStore.

---

### **📍 Paso 4: Implementar el `Flow` para leer la preferencia**

```kotlin
val airplaneModeFlow: Flow<Boolean?> = context.dataStore.data.map { preferences ->
    preferences[AIRPLANE_MODE_KEY] ?: false // evita null y pone false
}
```

📌 **Explicación:**

- `context.dataStore.data` devuelve un **Flow** con las preferencias almacenadas.
- `map {}` extrae el valor asociado a la clave `AIRPLANE_MODE_KEY`.

✅ **Con esto, el DataStore está listo para guardar y leer el estado del modo avión.**

---
### **🚀 Conclusión**

✔ **Ejercicio 1:** Aprendiste a guardar un booleano en DataStore.  
