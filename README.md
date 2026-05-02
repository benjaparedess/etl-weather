$$ ETL OpenWeather

Proyecto "ETL" desarrollado en Python. Extrae datos del clima desde la API de OpenWeather, transforma la información relevante y la carga en una base de datos PostgreSQL.

$$ Objetivo del proyecto

Construir un pipeline básico que permita recolectar, limpiar y almacenar datos climáticos para su posterior análisis mediante SQL.

$$ Tecnologías utilizadas

- Python
- PostgreSQL
- OpenWeather API
- Pandas
- Requests
- psycopg2
- python-dotenv

$$ Arquitectura del proyecto

OpenWeather API → Extract → Transform → Load → PostgreSQL

$$ Estructura del proyecto

```plaintext
etl-weather-project/
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── data/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md


$$ Flujo del ETL 
1. extract
Aqui se conecta a la API de OpenWeather y se obtienen los datos climáticos en un formato .JSON

2. transform
Se seleccionan los campos relevantes que entrega el archivo .JSON y los convierte en un dataframe limpio.

3. load
Carga los datos transformados a una tabla en pgadmin llamada weather_data. 


$$ Variables de entorno
El proyecto utiliza un archivo .env para manejar credenciales y configuraciones personales/sensibles.



$$ Ejecución del proyecto
Instalar dependencias con el sgte comando en terminal: 

pip install -r requirements.txt

posteriormente ejecutar el proyecto con el sgte comando en terminal: 

python main.py