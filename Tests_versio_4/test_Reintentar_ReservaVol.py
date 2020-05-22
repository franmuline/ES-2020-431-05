from unittest import mock
from User import User
from Viatge import Viatge
from unittest import TestCase
from Skyscanner import Skyscanner

u1 = User("George Hill Rogers", "47117447J", "Brooklyn", "rubiioo00_fcb_@hotmail.com", "983")
tipus_targeta = ["VISA", "PagosPaco", "MasterCard"]
num_targeta = [12345, 54321, 2456342]
codi_seguretat = [78365, 53420987, 23452325]

v1 = Viatge(u1, 2, ["Paris"])
v2 = Viatge(u1, 3, ["New York", "Buenos Aires"])
v3 = Viatge(u1, 2, ["Paris", "Roma", "Tokio, Buenos Aires"])
v4 = Viatge(u1, 6, ["Paris", "Roma","New York", "Buenos Aires", "Tokio"])
v5 = Viatge(u1, 4, ["Paris", "Roma", "Tokio, Buenos Aires"])

v1.pagar(tipus_targeta[1], num_targeta[2], codi_seguretat[0])
v2.pagar(tipus_targeta[2], num_targeta[2], codi_seguretat[0])
v4.pagar(tipus_targeta[0], num_targeta[2], codi_seguretat[0])
v5.pagar(tipus_targeta[0], num_targeta[2], codi_seguretat[0])

class test_Reintentar_PagamentViatge(unittest.TestCase):

    @mock.patch('Skyscanner.Skyscanner.confirm_reserve')

    def test_Reintentar_PagamentViatge(self, mock_skyscanner):

        assert v1.confirma_reserva() == False
        assert v2.confirma_reserva() == True
        assert v3.confirma_reserva() == False
        assert v4.confirma_reserva() == False
        assert v5.confirma_reserva() == True

        # A continuacio es prova amb skyscanner retornant false amb la funció confirm_reserve

        mock_skyscanner.return_value = False

        assert v2.confirma_reserva() == False
        assert v5.confirma_reserva() == False




