#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase
from unittest import mock
from User import User
from Viatge import Viatge



steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")
tipus_targeta=["VISA","PacoCard","MasterCard"]
num_targeta=[24352,234254,2456342,975674]
codi_seguretat=[22452,78365,523467,975674, 789080]

v1=Viatge(steverogers,4,["Paris", "Roma","New York", "Buenos Aires", "Rio de Janeiro"])
v2=Viatge(steverogers,10,["Moscu","Atenas","Milan","Londres"])
v3=Viatge(steverogers,2,["Tokyo"])
v4=Viatge(steverogers,4,["Paris", "Roma","New York", "Buenos Aires"])
v5=Viatge(steverogers,2, ["Paris", "Milan", "Roma"])
v6=Viatge(steverogers,1,["Roma"])

v1.pagar(tipus_targeta[0], num_targeta[0], codi_seguretat[0])
v2.pagar(tipus_targeta[2], num_targeta[1], codi_seguretat[4])
v4.pagar(tipus_targeta[0], num_targeta[3], codi_seguretat[2])
v5.pagar(tipus_targeta[1], num_targeta[1], codi_seguretat[4])
v6.pagar(tipus_targeta[2], num_targeta[1], codi_seguretat[4])


class test_Reintentar_PagamentViatge(unittest.TestCase):

    #@mock.patch('Skyscanner.Skyscanner.confirm_reserve')

    def test_Reintentar_PagamentViatge(self):

        assert v2.confirma_reserva() == True
        assert v4.confirma_reserva() == True
        assert v6.confirma_reserva() == True
        assert v1.confirma_reserva() == False
        assert v3.confirma_reserva() == False
        assert v5.confirma_reserva() == False



