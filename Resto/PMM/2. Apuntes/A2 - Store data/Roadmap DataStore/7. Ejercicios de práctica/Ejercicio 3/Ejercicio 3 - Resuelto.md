## **✅ Ejercicio 3: Implementar DataStore en ViewModel y observar cambios en la UI**

📌 **Objetivo:**  
Hacer que los cambios en DataStore **actualicen automáticamente la UI** usando **ViewModel y LiveData**.

---

### **📍 Paso 1: Crear `SettingsViewModel`**

```kotlin
class SettingsViewModel(private val settingsDataStore: SettingsDataStore) : ViewModel() {
```

📌 **Explicación:**

- `SettingsViewModel` usa `SettingsDataStore` para manejar las preferencias.
- Se inyecta `settingsDataStore` en el constructor (buena práctica).

---

### **📍 Paso 2: Convertir `Flow` en `LiveData`**

```kotlin
val themeLiveData: LiveData<Boolean?> = settingsDataStore.themeFlow.asLiveData()
val languageLiveData: LiveData<String?> = settingsDataStore.languageFlow.asLiveData()
val fontSizeLiveData: LiveData<Int?> = settingsDataStore.fontSizeFlow.asLiveData()
```

📌 **Explicación:**

- `asLiveData()` convierte `Flow` en `LiveData` para que pueda observarse en la UI.

---

### **📍 Paso 3: Métodos para modificar las preferencias**

```kotlin
fun updateTheme(isDarkMode: Boolean) {
    viewModelScope.launch {
        settingsDataStore.saveThemePreference(isDarkMode)
    }
}

fun updateLanguage(language: String) {
    viewModelScope.launch {
        settingsDataStore.saveLanguage(language)
    }
}

fun updateFontSize(fontSize: Int) {
    viewModelScope.launch {
        settingsDataStore.saveFontSize(fontSize)
    }
}
```

📌 **Explicación:**

- `viewModelScope.launch {}` ejecuta la escritura en una **corrutina**, evitando bloqueos en la UI.

---

### **📍 Paso 4: Observar los cambios en una `Activity`**

```kotlin
class MainActivity : AppCompatActivity() {

    private lateinit var viewModel: SettingsViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val settingsDataStore = SettingsDataStore(this)
        viewModel = SettingsViewModel(settingsDataStore)

        viewModel.themeLiveData.observe(this) { isDarkMode ->
            if (isDarkMode != null) {
                aplicarTemaOscuro(isDarkMode)
            }
        }

        findViewById<Button>(R.id.toggleThemeButton).setOnClickListener {
            viewModel.updateTheme(true)
        }
    }
}
```

📌 **Explicación:**

- `observe(this) {}` actualiza la UI cuando los valores cambian en DataStore.
- **Cada cambio en DataStore se refleja automáticamente en la UI.**

---

### **🚀 Conclusión**

✔ **Ejercicio 3:** Aprendiste a conectar DataStore con **ViewModel y UI reactiva**.