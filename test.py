""" Este programa es por si falla todo. Hace una prueba de la funcionalidad 
del proyecto
"""

from digitalClock import DigitalClock as DC
from utime import sleep

def clock_test() -> None:
    clock = DC(23, 59, 40)
    while True:
        h, m, s = clock.get_time()
        time = f'{h:02} : {m:02} : {s:02}'
        print(time)
        sleep(1)
        clock.increment()
        
