class Hotels:

    def __init__(self, codi, nom,desti, num_hostes,num_habitacions,durada_reserva,preu_dia_persona):
        self.codi=codi
        self.nom=nom
        self.desti=desti
        self.num_hostes=num_hostes
        self.num_habitacions=num_habitacions
        self.durada_reserva=durada_reserva
        self.preu=self.durada_reserva*preu_dia_persona
