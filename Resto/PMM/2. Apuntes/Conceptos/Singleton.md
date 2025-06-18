### **📌 ¿Qué es un Singleton en Kotlin?**

Un **Singleton** es un patrón de diseño que **garantiza que una clase tenga una única instancia** en toda la aplicación.

📌 **¿Por qué usar un Singleton?**  
✔ Evita crear múltiples instancias innecesarias.  
✔ Optimiza el uso de memoria.  
✔ Permite compartir datos globalmente dentro de la app.

---

## **📍 Ejemplo 1: Singleton básico en Kotlin**

```kotlin
object MiSingleton {
    var contador = 0

    fun incrementar() {
        contador++
    }
}
```

📌 **Explicación:**

- `object` en Kotlin crea un **Singleton automáticamente**.
- `contador` es una variable global que se comparte en toda la app.
- `incrementar()` aumenta el contador cada vez que se llama.

### **Ejemplo de uso:**

```kotlin
fun main() {
    MiSingleton.incrementar()
    println(MiSingleton.contador) // Salida: 1

    MiSingleton.incrementar()
    println(MiSingleton.contador) // Salida: 2
}
```

✔ **No importa cuántas veces accedamos a `MiSingleton`, siempre usa la misma instancia.**

---

## **📍 Ejemplo 2: Singleton en Android para manejar DataStore**

📌 **Caso práctico:**  
Queremos una clase Singleton para gestionar **DataStore** sin necesidad de crear múltiples instancias.

📂 `com.tuapp.data.UserPreferences.kt`

```kotlin
package com.tuapp.data

import android.content.Context
import androidx.datastore.preferences.preferencesDataStore
import androidx.datastore.preferences.core.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

private val Context.dataStore by preferencesDataStore(name = "user_prefs")

object UserPreferences {

    private val THEME_KEY = booleanPreferencesKey("dark_mode")

    suspend fun saveTheme(context: Context, isDarkMode: Boolean) {
        context.dataStore.edit { preferences ->
            preferences[THEME_KEY] = isDarkMode
        }
    }

    fun getTheme(context: Context): Flow<Boolean> {
        return context.dataStore.data.map { preferences ->
            preferences[THEME_KEY] ?: false
        }
    }
}
```

📌 **Explicación:**

- **`object UserPreferences`** → Garantiza que siempre haya **una única instancia**.
- **`context.dataStore`** → Se usa dentro de los métodos para acceder a DataStore.
- **`saveTheme(context, isDarkMode)`** → Guarda la preferencia en DataStore.
- **`getTheme(context)`** → Devuelve un `Flow<Boolean>` que notifica cambios automáticamente.

✅ **Ventaja:** **Cualquier parte de la app puede usar `UserPreferences` sin necesidad de instanciarlo.**

---

## **📍 Ejemplo 3: Usar el Singleton `UserPreferences` en una `Activity`**

📂 `MainActivity.kt`

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Guardar el tema oscuro
        lifecycleScope.launch {
            UserPreferences.saveTheme(this@MainActivity, true)
        }

        // Observar el valor del tema
        lifecycleScope.launch {
            UserPreferences.getTheme(this@MainActivity).collect { isDarkMode ->
                if (isDarkMode) {
                    AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
                } else {
                    AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
                }
            }
        }
    }
}
```

📌 **Explicación:**

- **`UserPreferences.saveTheme()`** se usa para guardar el tema sin necesidad de crear una instancia.
- **`UserPreferences.getTheme()`** devuelve el valor de DataStore y lo **observa en tiempo real**.
- **`lifecycleScope.launch {}`** maneja las corrutinas de forma segura dentro de la `Activity`.

✅ **Beneficio del Singleton en este caso:**  
✔ **No es necesario crear un `ViewModel` solo para leer DataStore.**  
✔ **Cualquier `Activity` o `Fragment` puede acceder a las preferencias fácilmente.**  
✔ **No se crean múltiples instancias innecesarias de `UserPreferences`.**

---

### **📌 Resumen**

✔ **Un Singleton es una clase que solo tiene una única instancia en toda la app.**  
✔ **Ideal para manejar configuraciones globales como DataStore, bases de datos, o conexiones a APIs.**  
✔ **Evita instancias innecesarias y optimiza la memoria.**  
✔ **En Android, un Singleton se usa mucho para manejar preferencias y configuraciones globales.**