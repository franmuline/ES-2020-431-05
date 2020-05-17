from . import PaymentData

def test_payment_data_ctor():

    payment = PaymentData('Usuari', 8.50, '1234567', '787')
    assert p.usuari == 'Text pagament'
    assert p.cost != 0
    assert p.cost == 8.50
    assert p.numTargeta == '1234567'
    assert p.codiSeguretat == '787'




