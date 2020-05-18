from unittest import TestCase
from Viatge import Viatge
from User import User
steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")


v1=Viatge(steverogers,4,[])
v2=Viatge(steverogers,10,[])
v3=Viatge(steverogers,2,[])
class Test_Viatge_Inicialitzacio(TestCase):
    def test_num_viatgers(self):
        assert v1.num_viatgers==4
        assert v2.num_viatgers==10
        assert v3.num_viatgers==2

    def test_destins(self):
        assert v1.destins==[]
        assert v2.destins==[]
        assert v3.destins==[]

    def test_vols(self):
        assert v1.vols==[]
        assert v2.vols==[]
        assert v3.vols==[]

    def test_preu(self):
        assert v1.preu==0
        assert v2.preu==0
        assert v3.preu==0