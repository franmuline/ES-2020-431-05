from unittest import TestCase
from Viatge import Viatge
from User import User
from Hotels import Hotels

steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")
v1=Viatge(steverogers,4,["Paris", "Roma"])
v2=Viatge(steverogers,10,["Moscu"])
v3=Viatge(steverogers,2,["Tokyo"])

hotel=[Hotels(1234,"Hotel Paris","Paris",100,45,4,60),Hotels(6798,"Hotel Roma","Roma",120,50,4,50),
       Hotels(4593,"Hotel Moscu","Moscu",150,70,4,100), Hotels(8023,"Hotel Tokyo","Tokyo",65,23,3,40)]


class Test_Afegir_Treure_Vehicles(TestCase):
    def test_afegir_treure_allotjament(self):
        v1.afegir_allotjament("Paris", hotel[0])
        assert v1.preu==140*2*v1.num_viatgers+v1.num_viatgers*hotel[0].preu
        v1.afegir_allotjament("Roma", hotel[1])
        assert v1.preu==140*2*v1.num_viatgers+v1.num_viatgers*(hotel[0].preu+hotel[1].preu)
        v2.afegir_allotjament("Moscu",hotel[2])
        assert v2.preu==140*v2.num_viatgers+v2.num_viatgers*hotel[2].preu
        v3.afegir_allotjament("Tokyo", hotel[3])
        assert v3.preu==140*v3.num_viatgers+v3.num_viatgers*hotel[3].preu
        v1.treure_allotjament("Paris")
        assert v1.preu==140*2*v1.num_viatgers+v1.num_viatgers*hotel[1].preu
        v1.treure_allotjament("Roma")
        assert v1.preu==140*2*v1.num_viatgers
        v2.treure_allotjament("Moscu")
        assert v2.preu==140*v2.num_viatgers
        v3.treure_allotjament("Tokyo")
        assert v3.preu==140*v3.num_viatgers