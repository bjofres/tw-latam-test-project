import json
import re
from collections import Counter
from typing import List, Tuple

# Función para extraer menciones (@usuario) de un texto
def extract_mentions(text: str) -> List[str]:
    # Usamos una expresión regular para la búsqueda de menciones
    return re.findall(r"@\S+", text)

# Función principal optimizada para usar menos memoria
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()

    # Abrir el archivo JSON línea por línea, sin cargar todo el archivo a la vez en memoria
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)  # Procesamos cada línea del archivo
                content = tweet.get('content', '')  # Extraemos el contenido del tweet
                mentions = extract_mentions(content)  # Extraemos las menciones
                mention_counter.update(mentions)  # Actualizamos el contador de menciones
            except json.JSONDecodeError:
                continue  # Si hay error en el JSON, simplemente continuamos con la siguiente línea

    # Devolvemos las menciones más comunes
    return mention_counter.most_common(10)
