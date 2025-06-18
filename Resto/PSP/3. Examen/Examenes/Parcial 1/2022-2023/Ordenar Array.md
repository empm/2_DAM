## Código

```java
package OrdenarArray;  
  
import java.util.ArrayList;  
import java.util.Collections;  
import java.util.List;  
  
public class main {  
    public static void main(String[] args) {  
        List<String> oroscopos = new ArrayList<String>();  
  
        // Agregamos los oroscopos.  
        oroscopos.add("Aries");  
        oroscopos.add("Tauro");  
        oroscopos.add("Geminis");  
        oroscopos.add("Cancer");  
        oroscopos.add("Leo");  
        oroscopos.add("Virgo");  
        oroscopos.add("Libra");  
        oroscopos.add("Escorpio");  
        oroscopos.add("Sagitario");  
        oroscopos.add("Capricornio");  
        oroscopos.add("Acuario");  
        oroscopos.add("Piscis");  
  
        // Metodo para ordenar un arraylist  
        Collections.sort(oroscopos);  
  
        // Imprimir y recorrer todos  
        for (String o : oroscopos){  
            System.out.println(o);  
        }  
  
    }  
}
```

## Descripción

**Importante:**
- Crear una lista de Array
