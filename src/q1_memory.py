import json
from collections import defaultdict
from datetime import datetime
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str, int]]:
    # Diccionario para almacenar el conteo de tweets por fecha y usuario
    tweet_count_by_date_user = defaultdict(lambda: defaultdict(int))

    # Abrir el archivo JSON y procesarlo línea por línea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)  # Cargar cada línea como JSON
                tweet_date = tweet.get('date')  # Obtener la fecha
                user = tweet.get('user', {}).get('username')  # Obtener el username

                # Verificamos si tenemos fecha y username válidos
                if tweet_date and user:
                    # Convertir la fecha a formato datetime.date
                    tweet_date = datetime.strptime(tweet_date, '%Y-%m-%dT%H:%M:%S%z').date()

                    # Actualizar el contador de tweets por fecha y usuario
                    tweet_count_by_date_user[tweet_date][user] += 1
            except (json.JSONDecodeError, TypeError, ValueError):
                print(f"Error al procesar una línea del archivo.")

    # Preparar la lista de resultados con el usuario más frecuente por fecha
    result = []
    for date, users in tweet_count_by_date_user.items():
        # Seleccionar el usuario con más tweets para esa fecha
        most_frequent_user = max(users, key=users.get)
        result.append((date, most_frequent_user, users[most_frequent_user]))

    return result
