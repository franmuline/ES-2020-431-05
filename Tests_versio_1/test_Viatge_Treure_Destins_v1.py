from unittest import TestCase
from Viatge import Viatge
from User import User
steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")


v1=Viatge(steverogers,4,["Paris", "Roma"])
v2=Viatge(steverogers,10,["Moscu"])
v3=Viatge(steverogers,2,["Tokyo"])
v1.treure_desti("Roma")
v2.treure_desti("Moscu")
v3.treure_desti("Tokyo")

class Test_Viatge_Treure_Destins(TestCase):
    #Controla que, quan es treuen destins, la llista de destins sigui la corresponent
    def test_treure_destins_destins(self):
        assert v1.destins==['Paris']
        assert v2.destins==[]
        assert v3.destins==[]

    #Controla que, quan es treuen destins, la llista de vols es la esperada
    def test_treure_destins_vols(self):
        assert v2.vols==[]
        assert v3.vols==[]
        assert len(v1.vols)==1
        assert v1.vols[0].destinacio=="Paris"

    #Controla que, quan es treuen destins, el preu sigui el corresponent
    def test_treure_destins_preu(self):
        assert v1.preu==140*v1.num_viatgers
        assert v2.preu==0
        assert v3.preu==0