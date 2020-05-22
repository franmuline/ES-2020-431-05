from unittest import TestCase
from Viatge import Viatge
from User import User
from Hotels import Hotels

steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")
v1=Viatge(steverogers,4,["Paris", "Roma"])
v2=Viatge(steverogers,10,["Moscu"])
v3=Viatge(steverogers,2,["Tokyo"])

hotel=[Hotels(1234,"Hotel Paris","Paris",100,45,4,60),Hotels(6798,"Hotel Roma","Roma",120,50,4,50),
       Hotels(4593,"Hotel Moscu","Moscu",150,70,4,100), Hotels(8023,"Hotel Tokyo","Tokyo",65,23,3,40),
       Hotels("Tuto", "Hotel Paris", "Paris", 100, 45, 4, 60), Hotels(6798, "Hotel Roma", "Roma", "LL", 50, 4, 50),
       Hotels(4593, "Hotel Moscu", "Moscu", 150, 70, 4, "Z"), Hotels(8023, "Hotel Tokyo", "Tokyo", 65, 23, "X", 40)]

class Test_Confirmacio_Error_Reserva_Hotels(TestCase):
    #Aquest test comprova que les dades dels diferents hotels siguin correctes (en aquest cas
    #els primers 4 hotels tenen dades correctes i els 4 últims no, per exemple, el codi del hotel
    #amb index 5 es "Tuto", quan hauria de ser un int), que si es vol reservar un hotel amb destí
    #"Moscu" pel destí "París" no es pugui i que si ja s'ha reservat hotel per un destí, no es puguin reservar més
    #Quan la funcio retorna False significa que hi ha un error a la reserva i, a través de la
    #interficie d'usuari, s'avisaria al client de que hi ha un error
    def test_confirmacio_error_reserva_hotels(self):
        assert v1.afegir_allotjament("Paris", hotel[1]) == False
        assert v1.afegir_allotjament("Paris", hotel[4]) == False
        assert v1.afegir_allotjament("Paris", hotel[6]) == False
        assert v1.afegir_allotjament("Moscu", hotel[0]) == False
        assert v1.afegir_allotjament("Paris", hotel[0]) == True
        assert v1.afegir_allotjament("Roma", hotel[1]) == True
        assert v1.afegir_allotjament("Paris", hotel[1]) == False
        assert v1.afegir_allotjament("Roma", hotel[3]) == False
        assert v2.afegir_allotjament("Moscu", hotel[1]) == False
        assert v2.afegir_allotjament("Moscu", hotel[6]) == False
        assert v2.afegir_allotjament("Moscu", hotel[2]) == True
        assert v3.afegir_allotjament("Tokyo", hotel[1]) == False
        assert v3.afegir_allotjament("Tokyo", hotel[7]) == False
        assert v3.afegir_allotjament("Tokyo", hotel[3]) == True
        assert v3.afegir_allotjament("Tokyo", hotel[3]) == False