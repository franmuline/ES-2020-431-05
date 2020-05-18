from User import User
from Flights import Flights
from Skyscanner import Skyscanner
from PaymentData import PaymentData
from Bank import Bank
class Viatge:
    def __init__(self, usuari: User, num_viatgers, destins):
        self.user=usuari
        self.num_viatgers = num_viatgers
        self.destins = destins
        self.vols=[]
        for desti in destins:
            self.vols.append(Flights(1234, desti, 160, 140))
        self.preu = 140*len(self.vols)

    def afegir_desti(self, desti):
        self.destins.append(desti)
        vol=Flights(1234, desti, 160, 140)
        self.vols.append(vol)
        self.preu+=vol.preu

    def treure_desti(self, desti):
        trobat=False
        i=0
        while trobat==False and i<len(self.vols):
            if self.vols[i].destinacio==desti:
                self.preu=self.preu-self.vols[i].preu
                self.vols.remove(self.vols[i])
                trobat=True
            else:
                i+=1
        self.destins.remove(desti)

    def confirma_reserva(self):
        skyscanner=Skyscanner()
        missatge_confirmacio=skyscanner.confirm_reserve(self.user,self.vols)
        return missatge_confirmacio

    def pagar(self, tipus_targeta, num_targeta, codi_seguretat):
        bank=Bank()
        paymentdata=PaymentData(tipus_targeta,self.user.nomComplet,num_targeta,codi_seguretat,self.preu)
        missatge_confirmacio=bank.do_payment(self.user,paymentdata)
        return missatge_confirmacio
