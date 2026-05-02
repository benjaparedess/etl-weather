import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


def load_weather_data(df):
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            country VARCHAR(10),
            temperature NUMERIC(5,2),
            feels_like NUMERIC(5,2),
            humidity INTEGER,
            pressure INTEGER,
            weather_description VARCHAR(100),
            wind_speed NUMERIC(5,2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather_data (
                city,
                country,
                temperature,
                feels_like,
                humidity,
                pressure,
                weather_description,
                wind_speed
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            row["city"],
            row["country"],
            row["temperature"],
            row["feels_like"],
            row["humidity"],
            row["pressure"],
            row["weather_description"],
            row["wind_speed"]
        ))

    conn.commit()

    cursor.close()
    conn.close()