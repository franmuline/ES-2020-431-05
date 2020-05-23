from unittest import TestCase
from Viatge import Viatge
from User import User
steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")


v1=Viatge(steverogers,4,[])
v2=Viatge(steverogers,10,[])
v3=Viatge(steverogers,2,[])
class Test_Viatge_Inicialitzacio(TestCase):
    #Controla que el número de viatgers sigui l'esperat al inicialitzar l'objecte
    def test_num_viatgers(self):
        assert v1.num_viatgers==4
        assert v2.num_viatgers==10
        assert v3.num_viatgers==2

    #Controla que la llista de destins está buida si el viatge no té destins
    def test_destins(self):
        assert v1.destins==[]
        assert v2.destins==[]
        assert v3.destins==[]

    #Controla que la llista de vols estigui buida si el viatge no té destins
    def test_vols(self):
        assert v1.vols==[]
        assert v2.vols==[]
        assert v3.vols==[]

    #Controla que el preu del viatge sigui 0 si el viatge no té destins
    def test_preu(self):
        assert v1.preu==0
        assert v2.preu==0
        assert v3.preu==0