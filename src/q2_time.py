import json
from collections import Counter
import emoji
from typing import List, Tuple

# función para extraer todos los emojis de un texto utilizando la librería emoji
# esto evita que tengamos que definir de manera manual arreglos o alguna lista de los caracteres unicode de los emojis
# se podría optimizar de alguna manera, ya que la función se evalua con cada tweet y su performance dependerá de cuantos tweets estemos procesando
def extract_emojis(text: str) -> List[str]:
    # usamos la función de la librería emoji "is_emoji" para extraer emojis del texto
    return [char for char in text if emoji.is_emoji(char)]

# función principal para contar los emojis más comunes en los tweets
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path, 'r', encoding='utf-8') as file:
        tweets = []
        for line in file:
            try:
                # si cada linea en el archivo es un objeto JSON por si mismo, este código maneja la lectura
                tweet = json.loads(line) 
                # agrega el nuevo objeto json al arreglo "tweets" para posteriormente evaluarlo
                tweets.append(tweet)
            except json.JSONDecodeError:
                print(f"Error en la línea: {line}")  # maneja errores si alguna línea no es JSON

    # inicializamos un contador para los emojis
    emoji_counter = Counter()

    # procesamos cada tweet y extraemos los emojis
    for tweet in tweets:
        content = tweet.get('content', '')  # ajusta el nombre de la clave si es diferente (ej. 'text')
        
        # extraer emojis del contenido del tweet
        emojis_in_tweet = extract_emojis(content)
        
        # contar los emojis extraídos
        emoji_counter.update(emojis_in_tweet)

    # devolvemos los 10 emojis más comunes
    return emoji_counter.most_common(10)
