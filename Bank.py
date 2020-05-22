from User import User
from PaymentData import PaymentData
import unittest

class Bank(unittest.TestCase):

    @classmethod
    def __init__(self):
        pass

    def do_payment(self, user: User, payment_data: PaymentData):
        return True