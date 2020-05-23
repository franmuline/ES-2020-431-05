import unittest
from unittest import mock
import User as us
from Viatge import Viatge


u= us.User("Cliente De Ejemplo", "420","City","cnu@gmail.com","2343")
tipus_targeta=["VISA","InvaCard","MasterCard"]
num_targeta=[24352,234254,2456342,975674]
codi_seguretat=[23142,"34",324342, 1324]

v1=Viatge(u,2,["Palma", "Reus","New York", "Dublín"])
v2=Viatge(u,6,["Madrid","BCN"])
v3=Viatge(u,3,["Madrid","Palma"])

print(v1.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]))#bbb
print(v2.pagar(tipus_targeta[1], num_targeta[2], codi_seguretat[3]))#bmb
print(v3.pagar(tipus_targeta[2], num_targeta[3], codi_seguretat[1]))#bmb

class test_Reintentar_PagamentCoche(unittest.TestCase):

    @mock.patch('Rentalcars.Rentalcars.confirm_reserve')

    def test_Reintentar_PagamentC(self, mock_Rentalcars):

        self.assertTrue(v1.confirma_reserva_coche())
        self.assertFalse(v2.confirma_reserva_coche())
        self.assertFalse(v3.confirma_reserva_coche())

        mock_Rentalcars.return_value = False

        self.assertFalse(v1.confirma_reserva_coche())
        self.assertFalse(v2.confirma_reserva_coche())
        self.assertFalse(v3.confirma_reserva_coche())
        

if __name__ == '__main__':
    unittest.main()