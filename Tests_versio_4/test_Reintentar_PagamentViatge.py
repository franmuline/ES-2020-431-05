from unittest import mock
from User import User
from Viatge import Viatge
from unittest import TestCase

u1 =User("Jofre Gomez Gonzalez", "123456789","Algo","sgr@gmail.com","933123456")
tipus_targeta=["VISA","IOs","Microsoft"]
num_targeta=[12345,54321.62,"XXXXX"]
codi_seguretat=[78365,53420987.67,"FF"]

v1=Viatge(u1,10,["Barcelona","Paris"])
v2=Viatge(u1,1,["Madrid"])

class Test_Reintentar_PagamentViatge(TestCase):

    @mock.patch('src.Bank')
    def test_Reintentar_PagamentViatge(self, mock_bank):

        #Abans de res, mencionar que si el pagament retorna false, qui s'encargara demostrar el missatge per
        #pantalla del error i on esta el error sera la interficie

        #Dades pagament valides + numero viatgers > 1 +
        assert v1.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]) == True

        assert v1.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]) == False