class Flights:

    def __init__(self, codi_vol, destinacio, num_passatgers, preu):
        self.codi_vol=codi_vol
        self.destinacio=destinacio
        self.num_passatgers=num_passatgers
        self.preu=preu

    def afegir_passatgers(self, passatgers):
        self.num_passatgers+=passatgers