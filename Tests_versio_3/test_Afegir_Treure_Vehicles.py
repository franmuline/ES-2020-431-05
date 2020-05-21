from unittest import TestCase
from Viatge import Viatge
from User import User
from Cars import Cars

steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")
v1=Viatge(steverogers,4,["Paris", "Roma"])
v2=Viatge(steverogers,10,["Moscu"])
v3=Viatge(steverogers,2,["Tokyo"])

cotxe=[Cars(12345,"Ford","Paris","Aeoroport Paris",4,100),Cars(6789,"Peugot","Roma","Aeroport Roma",4,80),
       Cars(2468,"Opel","Moscu","Aeroport Moscu",4,90), Cars(1357,"Audi","Tokyo","Aeroport Tokyo",3,120)]


class Test_Afegir_Treure_Vehicles(TestCase):
    def test_afegir_treure_vehicles(self):
        v1.afegir_cotxe("Paris", cotxe[0])
        assert v1.preu==140*2*v1.num_viatgers+cotxe[0].preu
        v1.afegir_cotxe("Roma", cotxe[1])
        assert v1.preu==140*2*v1.num_viatgers+cotxe[0].preu+cotxe[1].preu
        v2.afegir_cotxe("Moscu", cotxe[2])
        assert v2.preu==140*v2.num_viatgers+3*cotxe[2].preu
        v3.afegir_cotxe("Tokyo", cotxe[3])
        assert v3.preu==140*v3.num_viatgers+cotxe[3].preu
        v1.treure_cotxe("Paris")
        v1.treure_cotxe("Roma")
        assert v1.preu==140*2*v1.num_viatgers
        v2.treure_cotxe("Moscu")
        assert v2.preu==140*v2.num_viatgers
        v3.treure_cotxe("Tokyo")
        assert v3.preu==140*v3.num_viatgers


