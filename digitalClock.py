class DigitalClock:
    def __init__(self, h: int = 0, m: int = 0, s: int = 0) -> None:
        """Construye un objeto reloj digital desde el arbol
        
        Args:
            h (int, optional): La hora actual. Predeterminada en 0
            m (int, optional): Los minutos actuales. Predeterminada en 0
            s (int, optional): Los segundos actuales. Predeterminada en 0            
        """

        assert h < 24 and h >= 0
        self.__h = h
        assert m < 60 and m >= 0
        self.__m = m
        assert s < 60 and s >= 0
        self.__s = s
    
    def get_time(self) -> tuple[int, int, int]: # tuple: lista ordenada
        """Regresa el tiempo actual que el reloj muestra

        Regresa:
            una lista ordenada (tuple) tuple[int, int, int]: h, m, s, in 24-H formato
        """
        return self.__h, self.__m, self.__s 
    
    def clear_time(self) -> None:
        """Limpia la hora actual

        """
        self.__h, self.__m, self.__s = 0, 0, 0

    def increment(self) -> None:
        """Incrementa un segundo, un minuto y una hora en l timepo actual
        
        """
        self.__h = self.__h + 1 if self.__m == 59 and self.__s == 59 else self.__h
        self.__h = 0 if self.__h == 24 else self.__h

        self.__m = self.__m + 1 if self.__s == 59 else self.__m 
        self.__m = 0 if self.__m == 60 else self.__m 

        self.__s = self.__s + 1 if self.__s < 59 else 0 