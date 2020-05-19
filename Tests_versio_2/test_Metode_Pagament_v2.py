from unittest import TestCase
from User import User
from Viatge import Viatge

steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")
tipus_targeta=["VISA","MasterCard","MasterCard"]
num_targeta=[12345,54321,78953]
codi_seguretat=[78365,53420987,194249]

v1=Viatge(steverogers,4,["Paris", "Roma"])
v2=Viatge(steverogers,10,["Moscu"])
v3=Viatge(steverogers,2,["Tokyo"])

class Test_Metode_Pagament(TestCase):
    def test_metode_pagament(self):
        v1.pagar(tipus_targeta[0],num_targeta[0],codi_seguretat[0])
        assert v1.paymentdata.tipus_targeta==tipus_targeta[0]
        v2.pagar(tipus_targeta[1],num_targeta[1],codi_seguretat[1])
        assert v2.paymentdata.tipus_targeta==tipus_targeta[1]
        v3.pagar(tipus_targeta[2], num_targeta[2], codi_seguretat[2])
        assert v3.paymentdata.tipus_targeta == tipus_targeta[2]

