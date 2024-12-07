import pandas as pd
from typing import List, Tuple
from datetime import datetime

def q1_time(file_path: str) -> List[Tuple[datetime.date, str, int]]:
    # lee archivo usando pandas
    df = pd.read_json(file_path, lines=True)
    
    # asegura que la columna date esté en formato datetime
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    # extrae username de la columna user
    df['username'] = df['user'].apply(lambda x: x.get('username') if isinstance(x, dict) else None)
    
    # agrupar por fecha y username y contar los tweets
    df_agrupado = df.groupby(['date', 'username']).size().reset_index(name='tweet_count')
    
    # seleccionamos los usuarios más frecuentes por fecha
    result = df_agrupado.groupby('date').apply(lambda x: x.loc[x['tweet_count'].idxmax()]).reset_index(drop=True)
    
    # convertir el resultado en una lista de tuplas
    result = result[['date', 'username', 'tweet_count']]
    result = [tuple(x) for x in result.values]
    
    return result
