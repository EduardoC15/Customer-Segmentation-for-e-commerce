# Customer Segmentation for E-Commerce

## Descripción
Este proyecto analiza datos transaccionales de un minorista en línea con sede en el Reino Unido para segmentar clientes utilizando algoritmos de clustering. El objetivo principal es mejorar la efectividad del marketing y aumentar las ventas mediante la identificación de perfiles de clientes distintos basados en su comportamiento de compra.

## Dataset
El dataset proviene del **UCI Machine Learning Repository** y contiene transacciones realizadas entre 2010 y 2011. Incluye las siguientes columnas:

- **InvoiceNo**: Identificador único de cada transacción. Si comienza con 'C', indica una cancelación.
- **StockCode**: Código único asignado a cada producto.
- **Description**: Descripción del producto.
- **Quantity**: Cantidad de unidades compradas en la transacción.
- **InvoiceDate**: Fecha y hora de la transacción.
- **UnitPrice**: Precio unitario del producto en libras esterlinas.
- **CustomerID**: Identificador único del cliente.
- **Country**: País del cliente.

Enlace al dataset: [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)

El archivo utilizado en este proyecto es `online_retail_II.xlsx`, específicamente la hoja `Year 2010-2011`.

## Metodología
El análisis se llevó a cabo en las siguientes etapas:

1. **Limpieza de Datos**:
   - Eliminación de valores nulos (24.93% en `Customer ID` y 0.27% en `Description`).
   - Eliminación de duplicados (10,147 filas duplicadas identificadas).
   - Manejo de transacciones canceladas (2.21% del total).

2. **Ingeniería de Características**:
   - Creación de características centradas en el cliente, incluyendo:
     - **Recency**: Días desde la última compra.
     - **Total_Transactions**: Número total de transacciones por cliente.
     - **Total_Products_Purchased**: Total de productos comprados.
     - **TotalPrice**: Gasto total por cliente.
     - **Average_Transaction_Value**: Valor promedio por transacción.
     - **Unique_Products_Purchased**: Número de productos únicos comprados.
     - **Average_Days_Between_Purchases**: Promedio de días entre compras consecutivas.
     - **Day_Of_Week**: Día de la semana favorito para comprar.
     - **Hour**: Hora del día favorita para comprar.

3. **Clustering**:
   - Aplicación del algoritmo K-means para segmentar a los clientes en función de las características generadas.

## Resultados
Soon

## Visualizaciones
Las visualizaciones generadas durante el análisis incluyen:
- Gráficos de dispersión para explorar las relaciones entre características como `Recency`, `TotalPrice` y `Total_Transactions`.
- Representaciones de los clusters resultantes (se recomienda incluir capturas de pantalla o enlaces a los gráficos en el notebook).

Estas visualizaciones están disponibles en el notebook `e-commerce_RFM_Segmentation.ipynb`.

## Requisitos
Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:
- Python 3.12+
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- scikit-learn (para K-means)
- openpyxl (para leer archivos `.xlsx`)

Instala las dependencias con:
```bash
pip install -r requirements.txt