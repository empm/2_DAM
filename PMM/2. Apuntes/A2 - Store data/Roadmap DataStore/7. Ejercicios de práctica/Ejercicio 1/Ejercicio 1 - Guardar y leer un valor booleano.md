📌 **Objetivo:** Implementa un DataStore para guardar y recuperar una preferencia **"modo avión activado" (`airplane_mode`)**.

### **🔹 Pasos a seguir:**

1. **Crea una clase `AirplaneModeDataStore`.**
2. **Define una clave** `AIRPLANE_MODE_KEY`.
3. **Implementa un método `saveAirplaneMode(isEnabled: Boolean)`** que guarde el estado del modo avión en DataStore.
4. **Implementa un `Flow` llamado `airplaneModeFlow`** que devuelva el valor almacenado.
5. **Prueba llamando a la función de guardado y lectura en una `Activity` o `ViewModel`.**

🔹 **Pista:**

- Usa `booleanPreferencesKey("airplane_mode")` para definir la clave.
- La estructura será **idéntica a `SettingsDataStore`**, pero con otro nombre de clave.


# **🔹 ¿Cómo practicar estos ejercicios?**

✔ Empieza con **el ejercicio 1** y asegúrate de que puedes **guardar y leer datos en DataStore**.  
✔ Luego, en **el ejercicio 2**, **maneja múltiples preferencias** y observa cómo se organizan en el archivo de DataStore.  
✔ Finalmente, en **el ejercicio 3**, usa **ViewModel y LiveData** para aplicar lo aprendido en un entorno real con UI.
