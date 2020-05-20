class Cars:

    def __init__(self, codi, marca,desti, lloc_recollida, durada_reserva, preu_dia):
        self.codi=codi
        self.marca=marca
        self.desti=desti
        self.lloc_recollida=lloc_recollida
        self.durada_reserva=durada_reserva
        self.preu=self.durada_reserva*preu_dia
