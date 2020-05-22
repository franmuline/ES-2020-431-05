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
v3=Viatge(u1,1,["Barcelona","Paris"])

class Test_Reintentar_PagamentViatge(TestCase):

    @mock.patch('Bank.Bank.do_payment')
    def test_Reintentar_PagamentViatge(self, mock_bank):

        #Abans de res, mencionar que si el pagament retorna false, qui s'encargara demostrar el missatge per
        #pantalla del error i on esta el error sera la interficie

        #Dades pagament valides + numero viatgers > 1 + numero destins > 1 + return funcio pagar de la classe Bank = True
        self.assertTrue(v1.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]))
        #Dades pagament valides + numero viatgers = 1 + numero destins = 1 + return funcio pagar de la classe Bank = True
        self.assertTrue(v2.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]))
        # Dades pagament valides + numero viatgers = 1 + numero destins > 1 + return funcio pagar de la classe Bank = True
        self.assertTrue(v3.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]))
        # Dades pagament incorrectes + numero viatgers = 1 + numero destins = 1 + return funcio pagar de la classe Bank = True
        self.assertFalse(v2.pagar(tipus_targeta[2], num_targeta[2], codi_seguretat[0]))
        # Dades pagament incorrectes + numero viatgers > 1 + numero destins > 1 + return funcio pagar de la classe Bank = True
        self.assertFalse(v1.pagar(tipus_targeta[2], num_targeta[2], codi_seguretat[0]))
        # Dades pagament incorrectes + numero viatgers = 1 + numero destins > 1 + return funcio pagar de la classe Bank = True
        self.assertFalse(v3.pagar(tipus_targeta[2], num_targeta[2], codi_seguretat[0]))

        mock_bank.return_value = False
        # Dades pagament coherents + numero viatgers > 1 + numero destins > 1 + return funcio pagar de la classe Bank = False
        self.assertFalse(v1.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]))
        # Dades pagament coherents + numero viatgers = 1 + numero destins = 1 + return funcio pagar de la classe Bank = False
        self.assertFalse(v2.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]))
        # Dades pagament coherents + numero viatgers = 1 + numero destins > 1 + return funcio pagar de la classe Bank = False
        self.assertFalse(v3.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]))
        # Dades pagament no coherents + numero viatgers = 1 + numero destins = 1 + return funcio pagar de la classe Bank = False
        self.assertFalse(v2.pagar(tipus_targeta[2], num_targeta[2], codi_seguretat[0]))
        # Dades pagament no coherents + numero viatgers > 1 + numero destins > 1 + return funcio pagar de la classe Bank = False
        self.assertFalse(v1.pagar(tipus_targeta[2], num_targeta[2], codi_seguretat[0]))
        # Dades pagament no coherents + numero viatgers = 1 + numero destins > 1 + return funcio pagar de la classe Bank = False
        self.assertFalse(v3.pagar(tipus_targeta[2], num_targeta[2], codi_seguretat[0]))
