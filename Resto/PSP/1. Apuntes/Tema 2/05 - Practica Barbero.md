## Proyecto: Problema del barbero

- **Situación**:
    - Una barbería con **1 butaca** y **N cadires** (sillas) de espera.
    - Si no hay clientes, el barbero duerme.
    - Si la sala de espera está llena, los clientes se van.
    - Si hay espacio, el cliente se sienta y espera su turno.
    - Si el barbero está dormido, el cliente lo despierta.

- **Clases principales**:
    - **ButacaBarber** (silla del barbero).
    - **CadiresEspera** (cadires de espera).
    - **Barber** (barbero como hilo).
    - **Client** (clientes como hilos).

- **Tiempo**:
    - El barbero tarda 2 segundos en cortar el pelo.
    - Los clientes llegan cada 1 segundo.

- **Resultados**:
    - Salidas como "Cliente X se sienta", "Barbero corta a X", "Cliente se va".
