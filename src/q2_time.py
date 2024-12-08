import json
from collections import Counter
import emoji
from typing import List, Tuple

# Función para extraer todos los emojis de un texto utilizando la librería emoji
def extract_emojis(text: str) -> List[str]:
    # Usamos la función de la librería emoji "is_emoji" para extraer emojis del texto
    return [char for char in text if emoji.is_emoji(char)]

# Función principal para contar los emojis más comunes en los tweets
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)  # Cargar cada línea como un objeto JSON
                content = tweet.get('content', '')  # Obtener el contenido del tweet
                emojis_in_tweet = extract_emojis(content)  # Extraer emojis del contenido del tweet
                emoji_counter.update(emojis_in_tweet)  # Contar los emojis extraídos
            except json.JSONDecodeError:
                continue  # Ignorar líneas que no son JSON válidos

    # Devolver los 10 emojis más comunes
    return emoji_counter.most_common(10)