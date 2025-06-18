📌 **Objetivo:** Modifica la clase `SettingsDataStore` para permitir guardar y leer **dos preferencias adicionales**:

1. **Idioma de la aplicación (`language`)** (tipo `String`)
2. **Tamaño de fuente (`font_size`)** (tipo `Int`)

### **🔹 Pasos a seguir:**

1. **Agrega dos claves adicionales** en `companion object`:
    - `LANGUAGE_KEY = stringPreferencesKey("language")`
    - `FONT_SIZE_KEY = intPreferencesKey("font_size")`
2. **Modifica `SettingsDataStore`** para:
    - Implementar métodos `saveLanguage(String)` y `saveFontSize(Int)`.
    - Implementar `languageFlow` y `fontSizeFlow` para recuperar cada valor.
3. **Prueba tu implementación** llamando a los métodos desde una `Activity` o `ViewModel`.

🔹 **Pista:**

- `stringPreferencesKey("language")` para almacenar una `String`.
- `intPreferencesKey("font_size")` para almacenar un `Int`.

✅ **¿Bonus?**  
🔹 Modifica `savePreferences()` para **guardar los tres valores juntos** en una sola transacción atómica.


# **🔹 ¿Cómo practicar estos ejercicios?**

✔ Empieza con **el ejercicio 1** y asegúrate de que puedes **guardar y leer datos en DataStore**.  
✔ Luego, en **el ejercicio 2**, **maneja múltiples preferencias** y observa cómo se organizan en el archivo de DataStore.  
✔ Finalmente, en **el ejercicio 3**, usa **ViewModel y LiveData** para aplicar lo aprendido en un entorno real con UI.
