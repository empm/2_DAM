📌 **Objetivo:** Usa `SettingsDataStore` en un `ViewModel` para que la UI de la app **cambie automáticamente cuando el usuario modifica las preferencias**.

### **🔹 Pasos a seguir:**

1. **Crea un `ViewModel` llamado `SettingsViewModel`**.
2. **En el `ViewModel`, usa `SettingsDataStore`** para obtener `themeFlow`, `languageFlow` y `fontSizeFlow`.
3. **Convierte cada `Flow` en `LiveData`** para que pueda observarse desde la UI.
4. **Implementa métodos `toggleDarkMode()`, `setLanguage()`, `setFontSize()`** para modificar cada preferencia.
5. **En una `Activity` o `Fragment`**, observa los cambios en `LiveData` y actualiza la interfaz de usuario cuando cambien.

🔹 **Pista:**

- Usa `asLiveData()` en el `ViewModel` para convertir `Flow` en `LiveData`.
- En la `Activity`, usa `observe {}` para reaccionar a los cambios de configuración.

✅ **¿Bonus?**  
🔹 **Agrega un `Switch` en la UI** que permita activar/desactivar el **modo oscuro** y guarde la preferencia en DataStore.

# **🔹 ¿Cómo practicar estos ejercicios?**

✔ Empieza con **el ejercicio 1** y asegúrate de que puedes **guardar y leer datos en DataStore**.  
✔ Luego, en **el ejercicio 2**, **maneja múltiples preferencias** y observa cómo se organizan en el archivo de DataStore.  
✔ Finalmente, en **el ejercicio 3**, usa **ViewModel y LiveData** para aplicar lo aprendido en un entorno real con UI.
