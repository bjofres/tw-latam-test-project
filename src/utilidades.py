# line_profiler y memory_profiler
import time
from typing import Callable


def time_it(func: Callable) -> Callable:
    """
    Decorador para medir el tiempo de ejecución de una función.
    
    Args:
        func (Callable): La función a decorar.
    
    Returns:
        Callable: Función decorada con medición de tiempo.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Inicio del temporizador
        result = func(*args, **kwargs)
        end_time = time.time()    # Fin del temporizador
        elapsed_time = end_time - start_time
        print(f"⏱️ Tiempo de ejecución de {func.__name__}: {elapsed_time:.4f} segundos")
        return result
    return wrapper