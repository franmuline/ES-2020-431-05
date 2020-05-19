from unittest import TestCase
from User import User
from Viatge import Viatge

steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")
tipus_targeta=["VISA","IOs","Microsoft"]
num_targeta=[12345,54321.62,"You"]
codi_seguretat=[78365,53420987.67,"WW"]

v1=Viatge(steverogers,4,["Paris", "Roma"])
v2=Viatge(steverogers,10,["Moscu"])
v3=Viatge(steverogers,2,["Tokyo"])

class Test_Error_Pagament(TestCase):
    def test_error_pagament(self):
        assert v1.pagar(tipus_targeta[0],num_targeta[0],codi_seguretat[0])==True
        assert v1.pagar(tipus_targeta[1], num_targeta[0], codi_seguretat[0]) == False
        assert v1.pagar(tipus_targeta[0], num_targeta[1], codi_seguretat[2]) == False
        assert v1.pagar(tipus_targeta[1], num_targeta[2], codi_seguretat[1]) == False
        assert v2.pagar(tipus_targeta[0],num_targeta[0],codi_seguretat[0])==True
        assert v2.pagar(tipus_targeta[0], num_targeta[2], codi_seguretat[1]) == False
        assert v3.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0]) == True
        assert v3.pagar(tipus_targeta[2], num_targeta[0], codi_seguretat[0]) == False




