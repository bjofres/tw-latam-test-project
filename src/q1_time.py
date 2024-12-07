import pandas as pd
from collections import defaultdict
from datetime import datetime
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str, int]]:
    tweet_count_by_date_user = defaultdict(lambda: defaultdict(int))

    # Usamos chunksize para leer el archivo en trozos más pequeños
    chunksize = 10000  # Por ejemplo, leemos 10,000 líneas a la vez
    for chunk in pd.read_json(file_path, lines=True, chunksize=chunksize):
        # Convertir la columna 'date' a datetime
        chunk['date'] = pd.to_datetime(chunk['date']).dt.date

        # Extraer 'username'
        chunk['username'] = chunk['user'].apply(lambda x: x.get('username') if isinstance(x, dict) else None)

        # Agrupar por fecha y usuario y actualizar el contador
        grouped = chunk.groupby(['date', 'username']).size().reset_index(name='tweet_count')
        for _, row in grouped.iterrows():
            tweet_count_by_date_user[row['date']][row['username']] += row['tweet_count']

    # Preparar el resultado con el usuario más frecuente por fecha
    result = []
    for date, users in tweet_count_by_date_user.items():
        most_frequent_user = max(users, key=users.get)
        result.append((date, most_frequent_user, users[most_frequent_user]))

    return result
