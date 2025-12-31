from typing import Callable, Any
from functools import wraps
from fastapi import HTTPException, status


def handle_not_found(resource_name: str):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Originale Funktion aufrufen
            result = func(*args, **kwargs)

            # Prüfen, ob result None ist
            if result is None:
                # 404 Error auslösen
                detail = f"{resource_name} not found"
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail=detail
                )

            return result

        return wrapper

    return decorator
