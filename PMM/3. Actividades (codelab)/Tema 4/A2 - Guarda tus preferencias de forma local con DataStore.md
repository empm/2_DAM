El componente DataStore de Jetpack es una excelente forma de almacenar conjuntos de datos pequeños y simples con baja sobrecarga. 

DataStore tiene dos implementaciones diferentes: `Preferences DataStore` y `Proto DataStore`

- `Preferences DataStore` almacena pares clave-valor. Los valores pueden ser los tipos de datos básicos de Kotlin, como `String`, `Boolean` y `Integer`. No almacena conjuntos de datos complejos. No requiere un esquema predefinido. El caso de uso principal de `Preferences Datastore` es almacenar las preferencias del usuario en su dispositivo.
- `Proto DataStore` almacena tipos de datos personalizados. Requiere un esquema predefinido que asigne definiciones de proto con estructuras de objetos.

### Dependencias

```kotlin
implementation("androidx.datastore:datastore-preferences:1.0.0")
```


1. En el paquete `data`, crea una nueva clase llamada `UserPreferencesRepository`.

![c4c2e90902898001.png](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-datastore/img/c4c2e90902898001.png?hl=es-419)

2. En el constructor `UserPreferencesRepository`, define una propiedad de valor privado para representar una instancia del objeto `DataStore` con un tipo `Preferences`.

```kotlin
class UserPreferencesRepository(    
	private val dataStore: DataStore<Preferences>
){}
```

> [!Nota]
> Asegúrate de usar la importación 
> `androidx.datastore.preferences.core.Preferences` para la clase Preferences.

`DataStore` almacena pares clave-valor. Para acceder a un valor, debes definir una clave.

3. Crea un `companion object` dentro de la clase `UserPreferencesRepository`.
4. Usa la función `booleanPreferencesKey()` para definir una clave y pasarle el nombre `is_linear_layout`. Al igual que los nombres de tablas de SQL, la clave debe usar un formato de guion bajo. Esta clave se usa para acceder a un valor booleano que indica si se debe mostrar el diseño lineal.
## Escribe en DataStore

Para crear y modificar los valores en un `DataStore`, pasa una lambda al método `edit()`. La lambda recibe una instancia de `MutablePreferences`, que puedes usar para actualizar valores en `DataStore`. Todas las actualizaciones dentro de esta lambda se ejecutan como una sola transacción. Dicho de otro modo, la actualización es _atómica_: todo ocurre al mismo tiempo. Este tipo de actualización evita una situación en la que algunos valores se actualizan, pero otros no.

1. Crea una función de suspensión y llámala `saveLayoutPreference()`.
2. En la función `saveLayoutPreference()`, llama al método `edit()` en el objeto `dataStore`.
3. Para que tu código sea más legible, define un nombre para `MutablePreferences` que se proporciona en el cuerpo de la lambda. Usa esa propiedad para configurar un valor con la clave que definiste y el booleano que se pasó a la función `saveLayoutPreference()`.

> [!Note]
> El valor no existe en DataStore hasta que se llama a esta función y se configura el valor. Cuando configuras el par clave-valor en el método `edit()`, se define e inicializa el valor hasta que se borran la caché o los datos de la app.


La propiedad `data` es un `Flow` de objetos `Preferences`. El objeto `Preferences` contiene todos los pares clave-valor en DataStore. Cada vez que se actualizan los datos de DataStore, se emite un nuevo objeto `Preferences` en `Flow`.

3. Usa la función de asignación para convertir `Flow<Preferences>` en `Flow<Boolean>`.

Esta función acepta una expresión lambda con el objeto `Preferences` actual como parámetro. Puedes especificar la clave que definiste antes para obtener la preferencia de diseño. Ten en cuenta que es posible que el valor no exista si aún no se llamó a `saveLayoutPreference`, por lo que también debes proporcionar un valor predeterminado.

4. Especifica `true` para que se establezca la vista de diseño lineal como predeterminada.

## Manejo de excepciones

Cada vez que interactúas con el sistema de archivos en un dispositivo, es posible que falle algo. Por ejemplo, puede que un archivo no exista o que el disco esté lleno o desactivado. A medida que `DataStore` lee y escribe datos de archivos, pueden ocurrir `IOExceptions` cuando se accede a `DataStore`. Usa el operador `catch{}` para detectar excepciones y controlar estas fallas.

## [5. Inicializa DataStore](https://developer.android.com/codelabs/basic-android-kotlin-compose-datastore?hl=es-419&continue=https%3A%2F%2Fdeveloper.android.com%2Fcourses%2Fpathways%2Fandroid-basics-compose-unit-6-pathway-3%3Fhl%3Des-419%23codelab-https%3A%2F%2Fdeveloper.android.com%2Fcodelabs%2Fbasic-android-kotlin-compose-datastore#4)

En este codelab, debes controlar la inserción de dependencias de forma manual. Por lo tanto, debes proporcionar manualmente la clase `Preferences DataStore` con `UserPreferencesRepository`. Sigue estos pasos para insertar `DataStore` en `UserPreferencesRepository`.

1. Busca el paquete `dessertrelease`.
2. Dentro de este directorio, crea una nueva clase llamada `DessertReleaseApplication` y, luego, implementa la clase `Application`. Este es el contenedor para tu DataStore.

```kotlin
class DessertReleaseApplication: Application() {}
```

3. Dentro del archivo `DessertReleaseApplication.kt`, pero fuera de la clase `DessertReleaseApplication`, declara un `private const val` llamado `LAYOUT_PREFERENCE_NAME`.
4. Asigna a la variable `LAYOUT_PREFERENCE_NAME` el valor de cadena `layout_preferences`, que puedes usar como nombre del `Preferences Datastore` del que creaste una instancia en el siguiente paso.

```kotlin
private const val LAYOUT_PREFERENCE_NAME = "layout_preferences"
```

5. Aún fuera del cuerpo de la clase `DessertReleaseApplication`, pero en el archivo `DessertReleaseApplication.kt`, crea una propiedad de valor privado de tipo `DataStore<Preferences>` llamada `Context.dataStore` con el delegado `preferencesDataStore`. Pasa `LAYOUT_PREFERENCE_NAME` para el parámetro `name` del delegado `preferencesDataStore`.

```kotlin
private const val LAYOUT_PREFERENCE_NAME = "layout_preferences"private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(    name = LAYOUT_PREFERENCE_NAME)
```

6. Dentro del cuerpo de la clase `DessertReleaseApplication`, crea una instancia `lateinit var` de `UserPreferencesRepository`.

```kotlin
private const val LAYOUT_PREFERENCE_NAME = "layout_preferences"private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(    name = LAYOUT_PREFERENCE_NAME)class DessertReleaseApplication: Application() {    lateinit var userPreferencesRepository: UserPreferencesRepository}
```

7. Anula el método `onCreate()`.

```kotlin
private const val LAYOUT_PREFERENCE_NAME = "layout_preferences"private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(    name = LAYOUT_PREFERENCE_NAME)class DessertReleaseApplication: Application() {    lateinit var userPreferencesRepository: UserPreferencesRepository    override fun onCreate() {        super.onCreate()    }}
```

8. Dentro del método `onCreate()`, inicializa `userPreferencesRepository` construyendo un `UserPreferencesRepository` con `dataStore` como su parámetro.

```kotlin
private const val LAYOUT_PREFERENCE_NAME = "layout_preferences"private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(    name = LAYOUT_PREFERENCE_NAME)class DessertReleaseApplication: Application() {    lateinit var userPreferencesRepository: UserPreferencesRepository    override fun onCreate() {        super.onCreate()        userPreferencesRepository = UserPreferencesRepository(dataStore)    }}
```

9. Agrega la siguiente línea dentro de la etiqueta `<application>` en el archivo `AndroidManifest.xml`.

```kotlin
<application    android:name=".DessertReleaseApplication"    ...</application>
```

Este enfoque define la clase `DessertReleaseApplication` como punto de entrada de la app. El propósito de este código es inicializar las dependencias definidas en la clase `DessertReleaseApplication` antes de iniciar `MainActivity`.


## [6. Usa UserPreferencesRepository](https://developer.android.com/codelabs/basic-android-kotlin-compose-datastore?hl=es-419&continue=https%3A%2F%2Fdeveloper.android.com%2Fcourses%2Fpathways%2Fandroid-basics-compose-unit-6-pathway-3%3Fhl%3Des-419%23codelab-https%3A%2F%2Fdeveloper.android.com%2Fcodelabs%2Fbasic-android-kotlin-compose-datastore#5)

## Proporciona el repositorio al ViewModel

Ahora que `UserPreferencesRepository` está disponible a través de la inserción de dependencias, puedes usarlo en `DessertReleaseViewModel`.

1. En el `DessertReleaseViewModel`, crea una propiedad `UserPreferencesRepository` como parámetro de constructor.

```kotlin
class DessertReleaseViewModel(    private val userPreferencesRepository: UserPreferencesRepository) : ViewModel() {    ...}
```

2. Dentro del objeto complementario de `ViewModel`, en el bloque `viewModelFactory initializer`, obtén una instancia de `DessertReleaseApplication` con el siguiente código.

```kotlin
    ...    companion object {        val Factory: ViewModelProvider.Factory = viewModelFactory {            initializer {                val application = (this[APPLICATION_KEY] as DessertReleaseApplication)                ...            }        }    }}
```

3. Crea una instancia de `DessertReleaseViewModel` y pasa el `userPreferencesRepository`.

```kotlin
    ...    companion object {        val Factory: ViewModelProvider.Factory = viewModelFactory {            initializer {                val application = (this[APPLICATION_KEY] as DessertReleaseApplication)                DessertReleaseViewModel(application.userPreferencesRepository)            }        }    }}
```

Ahora, ViewModel puede acceder a `UserPreferencesRepository`. Los siguientes pasos son usar las capacidades de lectura y escritura del `UserPreferencesRepository` que implementaste antes.

## Cómo almacenar la preferencia de diseño

1. Edita la función `selectLayout()` en `DessertReleaseViewModel` para acceder al repositorio de preferencias y actualizar la preferencia de diseño.
2. Recuerda que escribir en `DataStore` se realiza de forma asíncrona con una función `suspend`. Inicia una nueva corrutina para llamar a la función `saveLayoutPreference()` del repositorio de preferencias.

```kotlin
fun selectLayout(isLinearLayout: Boolean) {    viewModelScope.launch {        userPreferencesRepository.saveLayoutPreference(isLinearLayout)    }}
```

## Cómo leer la preferencia de diseño

En esta sección, refactorizarás el `uiState: StateFlow` existente en `ViewModel` para reflejar el `isLinearLayout: Flow` del repositorio.

1. Borra el código que inicializa la propiedad `uiState` en `MutableStateFlow(DessertReleaseUiState)`.

```kotlin
val uiState: StateFlow<DessertReleaseUiState> =
```

La preferencia de diseño lineal del repositorio tiene dos valores posibles, true o false, con el formato de `Flow<Boolean>`. Este valor debe asignarse a un estado de IU.

2. Establece `StateFlow` en el resultado de la transformación de la colección `map()` a la que se llama en `isLinearLayout Flow`.

```kotlin
val uiState: StateFlow<DessertReleaseUiState> =    userPreferencesRepository.isLinearLayout.map { isLinearLayout ->}
```

3. Muestra una instancia de la clase de datos `DessertReleaseUiState` y pasa el `isLinearLayout Boolean`. La pantalla usa este estado de la IU para determinar las cadenas y los íconos correctos que se mostrarán.

```kotlin
val uiState: StateFlow<DessertReleaseUiState> =    userPreferencesRepository.isLinearLayout.map { isLinearLayout ->        DessertReleaseUiState(isLinearLayout)    }
```

`UserPreferencesRepository.isLinearLayout` es un `Flow` que es [_frío_](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow?hl=es-419#sharein). Sin embargo, para proporcionar el estado a la IU, es mejor usar un _flujo caliente_, como `StateFlow`, de modo que el estado siempre esté disponible de inmediato para la IU.

4. Usa la función `stateIn()` para convertir un `Flow` en un `StateFlow`.
5. La función `stateIn()` acepta tres parámetros: `scope`, `started` y `initialValue`. Pasa `viewModelScope`, `SharingStarted.WhileSubscribed(5_000)` y `DessertReleaseUiState()` para estos parámetros, respectivamente.

```kotlin
val uiState: StateFlow<DessertReleaseUiState> =    userPreferencesRepository.isLinearLayout.map { isLinearLayout ->        DessertReleaseUiState(isLinearLayout)    }.stateIn(        scope = viewModelScope,        started = SharingStarted.WhileSubscribed(5_000),        initialValue = DessertReleaseUiState()    )
```

**Nota:** Lee [Migración de LiveData a flujo de Kotlin](https://medium.com/androiddevelopers/migrating-from-livedata-to-kotlins-flow-379292f419fb) para obtener más información sobre el parámetro `started` y por qué se le pasa `SharingStarted.WhileSubscribed(5_000)`.

6. Inicia la app. Observa que puedes hacer clic en el ícono para alternar entre un diseño de cuadrícula y uno lineal.

**Nota:** Intenta activar o desactivar el diseño y cerrar la app. Vuelve a abrirla y observa que se guardó tu preferencia de diseño.

![b6e4bd0e50915b81.png](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-datastore/img/b6e4bd0e50915b81.png?hl=es-419) ![24a261db4cf2c6b8.png](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-datastore/img/24a261db4cf2c6b8.png?hl=es-419)

¡Felicitaciones! Agregaste `Preferences DataStore` a tu app de forma correcta para guardar la preferencia de diseño del usuario.