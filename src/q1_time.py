import pandas as pd
import orjson
from collections import defaultdict
from datetime import datetime
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str, int]]:
    # Diccionario para almacenar el conteo de tweets por fecha y usuario
    tweet_count_by_date_user = defaultdict(lambda: defaultdict(int))
    chunksize = 10000  # Leer 10,000 líneas a la vez

    def process_chunk(chunk):
        # Convertir la columna 'date' a datetime y extraer 'username'
        chunk['date'] = pd.to_datetime(chunk['date']).dt.date
        chunk['username'] = chunk['user'].apply(lambda x: x.get('username') if isinstance(x, dict) else None)

        # Agrupar por fecha y usuario y contar tweets
        grouped = chunk.groupby(['date', 'username']).size().reset_index(name='tweet_count')
        for _, row in grouped.iterrows():
            tweet_count_by_date_user[row['date']][row['username']] += row['tweet_count']

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = []
        for line in file:
            # Cargar cada línea como un objeto JSON usando orjson
            lines.append(orjson.loads(line))
            if len(lines) >= chunksize:
                # Convertir las líneas cargadas en un DataFrame de pandas
                chunk = pd.DataFrame(lines)
                # Procesar el chunk para contar los tweets por fecha y usuario
                process_chunk(chunk)
                # Reiniciar la lista de líneas
                lines = []
        if lines:
            # Procesar el último chunk si hay líneas restantes
            chunk = pd.DataFrame(lines)
            process_chunk(chunk)

    # Preparar el resultado con el usuario más frecuente por fecha
    result = []
    for date, users in tweet_count_by_date_user.items():
        # Seleccionar el usuario con más tweets para esa fecha
        most_frequent_user = max(users, key=users.get)
        result.append((date, most_frequent_user, users[most_frequent_user]))

    return result
