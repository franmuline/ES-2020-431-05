from unittest import TestCase
from Viatge import Viatge
from User import User
steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")


v1=Viatge(steverogers,4,[])
v2=Viatge(steverogers,10,[])
v3=Viatge(steverogers,2,[])
v1.afegir_desti("Paris")
v2.afegir_desti("Moscu")
v3.afegir_desti("Tokyo")
#Si se pasan los tests uno por uno, el resultado es bueno
#Si los se ponen todos a la vez, falla y no sabemos porqué
class Test_Viatge_Afegir_Destins(TestCase):
    def test_afegir_destins_destins(self):
        assert v1.destins==['Paris']
        assert v2.destins==['Moscu']
        assert v3.destins==['Tokyo']
        v1.afegir_desti("Roma")
        assert v1.destins == ['Paris','Roma']

    def test_afegir_destins_vols(self):
        assert v1.vols[0].destinacio=="Paris"
        assert v2.vols[0].destinacio=="Moscu"
        assert v3.vols[0].destinacio=="Tokyo"
        v1.afegir_desti("Roma")
        assert v1.vols[1].destinacio=="Roma"

    def test_afegir_destins_preu(self):
        assert v1.preu==140*v1.num_viatgers
        assert v2.preu==140*v2.num_viatgers
        assert v3.preu==140*v3.num_viatgers
        v1.afegir_desti("Roma")
        assert v1.preu==280*v1.num_viatgers

