from unittest import TestCase
from Viatge import Viatge
from User import User
from Cars import Cars

steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")
v1=Viatge(steverogers,4,["Paris", "Roma"])
v2=Viatge(steverogers,10,["Moscu"])
v3=Viatge(steverogers,2,["Tokyo"])

cotxe=[Cars(23456,"Ford","Paris","Aeoroport Paris",4,100),Cars(6789,"Peugot","Roma","Aeroport Roma",4,80),
       Cars(2468,"Opel","Moscu","Aeroport Moscu",4,90), Cars(1357,"Audi","Tokyo","Aeroport Tokyo",3,120),
       Cars("Sicilia","Ford","Paris","Aeoroport Paris",4,100),Cars("GUI","Peugot","Roma","Aeroport Roma",4,80),
       Cars(2468,"Opel","Moscu","Aeroport Moscu",4,"Tot"), Cars(1357,"Audi","Tokyo","Aeroport Tokyo","Ups",120)]

class Test_Confirmacio_Error_Reserva_Vehicles(TestCase):
    #Aquest test comprova que les dades dels diferents cotxes siguin correctes (en aquest cas
    #els primers 4 cotxes tenen dades correctes i els 4 últims no, per exemple, el preu per dia del cotxe
    #amb index 7 es "Tot"), que si es vol reservar un cotxe amb destí "Moscu" pel destí "París" no
    #es pugui i que si ja s'han reservat cotxes per un destí, no es puguin reservar més
    #Quan la funcio retorna False significa que hi ha un error a la reserva i, a través de la
    #interficie d'usuari, s'avisaria al client de que hi ha un error
    def test_confirmacio_error_reserva_vehicles(self):
        assert v1.afegir_cotxe("Paris",cotxe[1])==False
        assert v1.afegir_cotxe("Paris",cotxe[4])==False
        assert v1.afegir_cotxe("Paris", cotxe[6])==False
        assert v1.afegir_cotxe("Moscu",cotxe[0])==False
        assert v1.afegir_cotxe("Paris",cotxe[0])==True
        assert v1.afegir_cotxe("Roma",cotxe[1])==True
        assert v1.afegir_cotxe("Paris",cotxe[1])==False
        assert v1.afegir_cotxe("Roma", cotxe[3])==False
        assert v2.afegir_cotxe("Moscu",cotxe[1])==False
        assert v2.afegir_cotxe("Moscu",cotxe[6])==False
        assert v2.afegir_cotxe("Moscu", cotxe[2]) == True
        assert v3.afegir_cotxe("Tokyo",cotxe[1])==False
        assert v3.afegir_cotxe("Tokyo",cotxe[7])==False
        assert v3.afegir_cotxe("Tokyo",cotxe[3])==True
        assert v3.afegir_cotxe("Tokyo", cotxe[3]) == False




