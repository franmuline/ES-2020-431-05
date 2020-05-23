from unittest import TestCase
from User import User
from Viatge import Viatge

steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")
tipus_targeta1="VISA"
tipus_targeta2="MasterCard"
num_targeta=123456
codi_seguretat=13062091

v1=Viatge(steverogers,4,["Paris", "Roma"])
v2=Viatge(steverogers,10,["Moscu"])
v3=Viatge(steverogers,2,["Tokyo"])

#Controla que, quan es paga el viatge, es reporta que l'acció s'ha dut a terme correctament
class Test_Viatge_Pagament_Reserva(TestCase):
    def test_pagament(self):
        assert v1.pagar(tipus_targeta1,num_targeta,codi_seguretat)==True
        assert v2.pagar(tipus_targeta2,num_targeta,codi_seguretat)==True
        assert v3.pagar(tipus_targeta2,num_targeta,codi_seguretat)==True