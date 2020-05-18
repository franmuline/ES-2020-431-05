from unittest import TestCase
from User import User
from Viatge import Viatge

steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")


v1=Viatge(steverogers,4,["Paris", "Roma"])
v2=Viatge(steverogers,10,["Moscu"])
v3=Viatge(steverogers,2,["Tokyo"])

class Test_Viatge_Confirmar_Reserva(TestCase):
    def test_reserva(self):
        assert v1.confirma_reserva()==True
        assert v2.confirma_reserva()==True
        assert v3.confirma_reserva()==True