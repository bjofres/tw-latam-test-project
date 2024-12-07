import json
from collections import Counter
import emoji
from typing import List, Tuple

# Función para extraer todos los emojis de un texto
def extract_emojis(text: str) -> List[str]:
    """
    Extrae todos los emojis de un texto usando la librería emoji.
    """
    return [char for char in text if emoji.is_emoji(char)]

# Función principal optimizada para memoria
def q2_memory(file_path: str, batch_size: int = 1000) -> List[Tuple[str, int]]:
    """
    Calcula el top 10 de emojis más usados, optimizado para memoria.
    
    Args:
        file_path: Ruta del archivo JSON línea por línea.
        batch_size: Número de líneas procesadas por lote.
    
    Returns:
        Una lista con los 10 emojis más frecuentes.
    """
    emoji_counter = Counter()  # Contador para emojis
    buffer = []  # Buffer para procesamiento por lotes

    # Procesar el archivo en lotes
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)  # Procesar línea como JSON
                content = tweet.get('content', '')  # Obtener el contenido del tweet
                buffer.append(content)

                # Procesar cuando se llena el buffer
                if len(buffer) >= batch_size:
                    for text in buffer:
                        emojis = extract_emojis(text)  # Extraer emojis
                        emoji_counter.update(emojis)  # Actualizar el contador
                    buffer.clear()  # Vaciar el buffer
            except json.JSONDecodeError:
                print(f"Error procesando una línea: {line.strip()}")

        # Procesar el buffer restante
        for text in buffer:
            emojis = extract_emojis(text)
            emoji_counter.update(emojis)

    return emoji_counter.most_common(10)
