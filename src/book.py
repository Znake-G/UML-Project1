from abc import ABC
from typing import Any, List

class Libro (ABC):

    def __init__(self, titulo: str, isbn: str, genero: str, formato: str, valor: float, **kwargs:Any) -> None:
        super().__init__(**kwargs)
        self._titulo = titulo
        self._autores: List["Autores"] = []
        self._isbn = isbn
        self._genero = genero
        self._formato = formato
        self._valor = valor
        self._editorial: "Editorial" = None

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._titulo},{self._isbn})'

class Libroimpreso(Libro):

    def __init__(self, paginas: int, num_ejemplares: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__paginas = paginas
        self.__num_ejemplares = num_ejemplares




class Librodigital(Libro):

    def __init__(self, has_hipervinculo: bool, **kwargs:Any) -> None:
        super().__init__(**kwargs)
        self.__has_hipervinculo = has_hipervinculo
        self.__hipervinculos: List[str] = []


class Audiolibro(Libro):

    def __init__(self, duracion: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__