```kotlin
package com.eperez.preparacionexamen  
  
import android.content.Context  
import androidx.datastore.core.DataStore  
import androidx.datastore.preferences.core.Preferences  
import androidx.datastore.preferences.preferencesDataStore  
import androidx.test.core.app.ApplicationProvider  
import com.eperez.preparacionexamen.data.AirplaneModeDataStore  
import kotlinx.coroutines.flow.first  
import kotlinx.coroutines.runBlocking  
import org.junit.Assert.*  
  
import org.junit.Before  
import org.junit.Test  
  
  
class AirplaneModeDataStoreTest {  
  
    private lateinit var airplaneModeDataStore: AirplaneModeDataStore  
    private val context: Context = ApplicationProvider.getApplicationContext()  
    private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "settings")  
  
    @Before  
    fun setUp() {  
        airplaneModeDataStore = AirplaneModeDataStore(context)  
    }  
  
    @Test  
    fun saveAirplaneMode() = runBlocking {  
        val isEnabled = true  
  
        airplaneModeDataStore.saveAirplaneMode(isEnabled)  
  
        val retrievedIsEnabled = airplaneModeDataStore.airplaneModeFlow.first()  
        assertEquals(isEnabled, retrievedIsEnabled)  
    }  
  
    @Test  
    fun getAirplaneModeFlow() = runBlocking {  
        val isEnabled = true  
  
        airplaneModeDataStore.saveAirplaneMode(isEnabled)  
        val retrievedIsEnabled = airplaneModeDataStore.airplaneModeFlow.first()  
          
    }  
}
```