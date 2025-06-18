## **✅ Ejercicio 2: Guardar y recuperar múltiples preferencias**

📌 **Objetivo:**  
Modificar `SettingsDataStore` para **guardar y leer múltiples valores**.

---

### **📍 Paso 1: Definir claves para cada preferencia**

```kotlin
companion object {
    private val THEME_KEY = booleanPreferencesKey("dark_mode")
    private val LANGUAGE_KEY = stringPreferencesKey("language")
    private val FONT_SIZE_KEY = intPreferencesKey("font_size")
}
```

📌 **Explicación:**

- Cada clave debe tener **un tipo de dato específico** (`Boolean`, `String`, `Int`).

---

### **📍 Paso 2: Implementar métodos para guardar valores**

```kotlin
suspend fun saveThemePreference(isDarkMode: Boolean) {
    context.dataStore.edit { preferences ->
        preferences[THEME_KEY] = isDarkMode
    }
}

suspend fun saveLanguage(language: String) {
    context.dataStore.edit { preferences ->
        preferences[LANGUAGE_KEY] = language
    }
}

suspend fun saveFontSize(fontSize: Int) {
    context.dataStore.edit { preferences ->
        preferences[FONT_SIZE_KEY] = fontSize
    }
}
```

📌 **Explicación:**

- Cada método usa `edit {}` para **modificar solo una preferencia específica**.

✅ **Alternativa más eficiente:** Guardar **todas las preferencias en una sola transacción**:

```kotlin
suspend fun savePreferences(isDarkMode: Boolean, language: String, fontSize: Int) {
    context.dataStore.edit { preferences ->
        preferences[THEME_KEY] = isDarkMode
        preferences[LANGUAGE_KEY] = language
        preferences[FONT_SIZE_KEY] = fontSize
    }
}
```

📌 **¿Por qué es mejor?**  
✔ **Menos escrituras en disco** → mejora el rendimiento.  
✔ **Transacción atómica** → garantiza que todos los valores se guarden juntos.

---

### **📍 Paso 3: Implementar `Flow` para leer los valores**

```kotlin
val themeFlow: Flow<Boolean?> = context.dataStore.data.map { preferences ->
    preferences[THEME_KEY]
}

val languageFlow: Flow<String?> = context.dataStore.data.map { preferences ->
    preferences[LANGUAGE_KEY]
}

val fontSizeFlow: Flow<Int?> = context.dataStore.data.map { preferences ->
    preferences[FONT_SIZE_KEY]
}
```

📌 **Explicación:**

- Se usa `Flow` para leer cada preferencia en **tiempo real**.
- Se devuelve `null` si el valor no ha sido guardado.

✅ **Con esto, ahora se pueden guardar y leer múltiples valores en DataStore.**

---
### **🚀 Conclusión**

✔ **Ejercicio 2:** Aprendiste a manejar múltiples preferencias en una sola transacción.  