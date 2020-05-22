from User import User
from Flights import Flights
from Skyscanner import Skyscanner
from PaymentData import PaymentData
from Bank import Bank
from Cars import Cars
from Hotels import Hotels
from Rentalcars import Rentalcars
from Booking import Booking

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

    def afegir_desti(self, desti): #Afegeix desti a la llista de destins i el vol corresponent a la llista de vols
                                   #augmentant el preu de la manera corresponent
        self.destins.append(desti)
        vol=Flights(1234, desti, 160, 140)
        self.vols.append(vol)
        self.preu+=vol.preu*self.num_viatgers

    def treure_desti(self, desti):  #Treu el desti de la llista de destins i el vol corresponent de la llista de vols,
                                    #disminuent el preu de la manera corresponent. Retorna True si s'ha eliminat i False
                                    #si no s'ha pogut eliminar
        trobat=False
        i=0
        while trobat==False and i<len(self.vols):
            if self.vols[i].destinacio==desti:
                self.preu=self.preu-self.vols[i].preu*self.num_viatgers
                self.vols.remove(self.vols[i])
                self.destins.remove(desti)
                trobat=True
            else:
                i+=1

        return trobat

    def afegir_cotxe(self, desti, cotxe: Cars):     #Afegeix cotxe a la llista de cotxes del viatge al desti que es demana.
                                                    #Comprova que el desti es troba al viatge, que el cotxe es pugui reservar i
                                                    #al desti demanat. La confirmacio o error en la reserva del cotxe es
                                                    #realitza també en aquest métode, cridant a un objecte de la clase Rentalcars
                                                    #Comprova que totes les dades del cotxe
                                                    #siguin del tipus corresponent (explicat als fitxers dels tests de confirmacio-error de cotxes).
                                                    #Augmenta el preu del viatge de la forma corresponent i retorna True si
                                                    #la reserva es realitza correctament i False si no ho fa
        missatge_confirmacio=False
        rentalcars=Rentalcars()
        trobat=False
        i=0
        if desti in self.destins:
            while trobat==False and i<len(self.cotxes):
                if desti == self.cotxes[i].desti:
                    trobat=True
                else:
                    i+=1
            if trobat==False:
                if desti==cotxe.desti and type(cotxe.preu) is int and type(cotxe.desti) is str and \
                        type(cotxe.durada_reserva) is int and type(cotxe.lloc_recollida) is str and \
                        type(cotxe.codi) is int and type(cotxe.marca) is str:
                    self.cotxes.append(cotxe)
                    if self.num_viatgers%4==0:
                        self.preu+=cotxe.preu*(int(self.num_viatgers/4))
                    else:
                        self.preu+=cotxe.preu*(int(self.num_viatgers/4)+1)
                    missatge_confirmacio=rentalcars.confirm_reserve(self.user,cotxe)
        return missatge_confirmacio

    def treure_cotxe(self, desti):      #Treu el cotxe del desti demanat, si es que hi havia un cotxe demanat per el
                                        #desti. Retorna True si la operacio s'ha realitzat correctament i False si no
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

    def afegir_allotjament(self, desti, hotel: Hotels): #Afegeix hotel corresponent al desti corresponent.
                                                        #Igual que amb els cotxes, la confirmació o error en la reserva
                                                        #es realitza en aquest métode, cridant a un objecte de la clase Booking.
                                                        #Si la reserva es confirma correctament, es retorna True, i si no,
                                                        #False. També comprova que dades de l'hotel siguin correctes
                                                        #(explicat al document de tests de confirmacio-error hotels)
        booking=Booking()
        missatge_confirmacio = False
        trobat = False
        i = 0
        if desti in self.destins:
            while trobat == False and i < len(self.hotels):
                if desti == self.hotels[i].desti:
                    trobat=True
                else:
                    i+=1
            if trobat==False:
                if desti==hotel.desti and type(hotel.preu) is int and type(hotel.desti) is str \
                    and type(hotel.codi) is int and type(hotel.num_hostes) is int and type(hotel.num_habitacions) is int \
                    and type(hotel.nom) is str and type(hotel.durada_reserva) is int:
                    self.hotels.append(hotel)
                    self.preu+=self.num_viatgers*hotel.preu
                    missatge_confirmacio=booking.confirm_reserve(self.user,hotel)
        return missatge_confirmacio

    def treure_allotjament(self, desti):    #Treu l'hotel del desti que es pasa com a parámetre. Comprova si existeix
                                            #un hotel reservat en el desti corresponent i l'elimina de la llista d'hotels,
                                            #disminuint el preu del viatge de la forma corresponent
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

    def confirma_reserva(self): #Confirma la reserva dels vols un cop pagat el viatge. Té en compte que el número
                                #de vols es igual o menor a 4. Crida a la funcio de confirmar reserva d'un objecte de
                                #la clase skyscanner i retorna True si s'ha confirmat correctament i False si no
        skyscanner=Skyscanner()
        missatge_confirmacio=False
        if len(self.vols)<=4 and self.pagament_fet==True:
            missatge_confirmacio=skyscanner.confirm_reserve(self.user,self.vols)
        return missatge_confirmacio

    def pagar(self, tipus_targeta, num_targeta, codi_seguretat):    #Paga el viatge cridant al métode do_payment
                                                                #d'un objecte de la clase Bank. Retorna True si s'ha produit correctament
                                                                #i False si hi ha un error
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

