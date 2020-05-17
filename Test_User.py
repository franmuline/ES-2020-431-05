from . import User


def test_user_ctor():
    # Test de la inicialització

    user = User('Jose Mari', '98765432J', 'C. MatalasCañas, 78', 'joselito@pepemail.com', '999666999')

    assert user.nomComplet == 'Jose Mari'
    assert user.DNI == '98765432J'
    assert user.direccio == 'C. MatalasCañas, 78'
    assert user.email == 'joselito@pepemail.com'
    assert user.telefon == '999666999'


