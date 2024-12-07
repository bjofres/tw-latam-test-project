from typing import List, Tuple
import json
from collections import Counter
import re

# función para extraer menciones (@usuario) de un texto
def extract_mentions(text: str) -> List[str]:
    # expresión regular para la busqueda de menciones
    # @ inicio de la mención | \S cualquier caracter, incluyendo puntos y guiones (util para casos de nombres de usuario) | + para completar el registro hasta el espacio
    return re.findall(r"@\S+", text)

# función principal
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # inicia un collection de contador para menciones
    mention_counter = Counter()

    # carga tweets del archivo JSON línea por línea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)  # cargar cada línea como un objeto JSON
                content = tweet.get('content', '')  # obtener el contenido del tweet
                mentions = extract_mentions(content)  # extrae menciones
                mention_counter.update(mentions)  # actualiza contador
            except json.JSONDecodeError:
                print(f"Error al procesar una línea: {line}")

    # retorna el top 10 de menciones
    return mention_counter.most_common(10)
