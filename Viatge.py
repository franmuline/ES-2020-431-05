from User import User
from Flights import Flights
from Skyscanner import Skyscanner
from PaymentData import PaymentData
from src.Bank import Bank
from Cars import Cars
from Hotels import Hotels

class Viatge:

    def __init__(self, usuari: User, num_viatgers, destins):
        self.user=usuari
        self.num_viatgers = num_viatgers
        self.destins = destins
        self.vols=[]
        self.cotxes=[]
        self.hotels=[]
        i=0
        for desti in destins:  #Tots els vols tenen igual codi, mateix número passatgers(quan es creen) i mateix preu
            self.vols.append(Flights(1234, desti, 100, 140))
            self.vols[i].afegir_passatgers(self.num_viatgers)
        self.preu = 140*len(self.vols)*num_viatgers
        self.pagament_fet=False

    def afegir_desti(self, desti):
        self.destins.append(desti)
        vol=Flights(1234, desti, 160, 140)
        self.vols.append(vol)
        self.preu+=vol.preu*self.num_viatgers

    def treure_desti(self, desti):
        trobat=False
        i=0
        while trobat==False and i<len(self.vols):
            if self.vols[i].destinacio==desti:
                self.preu=self.preu-self.vols[i].preu*self.num_viatgers
                self.vols.remove(self.vols[i])
                trobat=True
            else:
                i+=1
        self.destins.remove(desti)
        return trobat

    def afegir_cotxe(self, desti, cotxe: Cars):
        self.cotxes.append(cotxe)
        if self.num_viatgers%4==0:
            self.preu+=cotxe.preu*(int(self.num_viatgers/4))
        else:
            self.preu+=cotxe.preu*(int(self.num_viatgers/4)+1)

    def treure_cotxe(self, desti):
        trobat=False
        i=0
        while trobat==False and i<len(self.cotxes):
            if self.cotxes[i].desti==desti:
                trobat=True
                if self.num_viatgers % 4 == 0:
                    self.preu = self.preu-self.cotxes[i].preu * (int(self.num_viatgers / 4))
                else:
                    self.preu = self.preu-self.cotxes[i].preu * (int(self.num_viatgers / 4) + 1)
                self.cotxes.remove(self.cotxes[i])
            else:
                i+=1
        return trobat

    def afegir_allotjament(self, desti, hotel: Hotels):
        self.hotels.append(hotel)
        self.preu+=self.num_viatgers*hotel.preu

    def treure_allotjament(self, desti):
        trobat=False
        i=0
        while trobat==False and i<len(self.hotels):
            if self.hotels[i].desti==desti:
                trobat=True
                self.preu=self.preu-self.num_viatgers*self.hotels[i].preu
                self.hotels.remove(self.hotels[i])
            else:
                i+=1
        return trobat

    def confirma_reserva(self):
        skyscanner=Skyscanner()
        missatge_confirmacio=False
        if len(self.vols)<=4 and self.pagament_fet==True:
            missatge_confirmacio=skyscanner.confirm_reserve(self.user,self.vols)
        return missatge_confirmacio

    def pagar(self, tipus_targeta, num_targeta, codi_seguretat):
        bank=Bank()
        missatge_confirmacio=False
        intents = 0
        if (tipus_targeta=="VISA" or tipus_targeta=="MasterCard") and (type(num_targeta) is int) and (type(codi_seguretat) is int):
            self.paymentdata=PaymentData(tipus_targeta,self.user.nomComplet,num_targeta,codi_seguretat,self.preu)
            while True:
                missatge_confirmacio=bank.do_payment(self.user,self.paymentdata)
                intents+=1
                if missatge_confirmacio:
                    self.pagament_fet=True
                if (self.pagament_fet == True) or (intents >= 3) or (self.num_viatgers <= 1) or (len(self.destins) <= 1):
                    break
        return missatge_confirmacio

