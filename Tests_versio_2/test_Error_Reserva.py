from unittest import TestCase
from User import User
from Viatge import Viatge

steverogers=User("Steve Grant Rogers", "471","Brooklyn","sgr@gmail.com","983")
tipus_targeta=["VISA","VISA","MasterCard"]
num_targeta=[12345,54321,2456342]
codi_seguretat=[78365,53420987,23452325]

v1=Viatge(steverogers,4,["Paris", "Roma","New York", "Buenos Aires", "Rio de Janeiro"])
v2=Viatge(steverogers,10,["Moscu","Atenas","Milan","Londres"])
v3=Viatge(steverogers,2,["Tokyo"])
v4=Viatge(steverogers,4,["Paris", "Roma","New York", "Buenos Aires"])

v1.pagar("VISA",24352,22452)
v2.pagar("MasterCard",234254,789080)
v4.pagar("VISA", 975674,523467)
#Per confirmar la reserva cal que el numero de destins sigui <=4 i
#hagis pagat el viatge amb anterioritat

#Controla que, quan hi ha un error a la reserva de vols, es reporti de l'acció
class Test_Error_Reserva(TestCase):
    def test_error_reserva(self):
        assert v1.confirma_reserva()==False
        assert v2.confirma_reserva()==True
        assert v3.confirma_reserva()==False
        assert v4.confirma_reserva()==True
