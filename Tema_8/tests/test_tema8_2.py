import unittest
from parameterized import parameterized
from Teme_ITF.Tema_8.app.tema8_2 import Employee, ContBancar


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Cristescu', 'Andrei', 3500)

    def test_descriere(self):
        self.assertEqual(self.employee.descriere(), 'Numele: Cristescu, Prenumele: Andrei, Salariul: 3500')

    def test_nume_complet(self):
        self.assertEqual(self.employee.nume_complet(), 'Cristescu Andrei')

    def test_salariu_lunar(self):
        self.assertEqual(self.employee.salariu_lunar(), 3500)

    def test_annual_salary(self):
        self.assertEqual(self.employee.salariu_anual(), 42000)

    @parameterized.expand([
        (100, 7000),
        (0, 3500),
        (-50, 1750)
    ])
    def test_revizuire_salariu(self, percentage, expected):
        self.employee.revizuire_salariu(percentage)
        self.assertEqual(self.employee.salary, expected)


class TestContBancar(unittest.TestCase):
    def setUp(self):
        self.Titular_cont = ContBancar('RO01234567890RO', 'Florin Costea', 5300.00)

    def test_show_balance(self):
        self.assertEqual(self.Titular_cont.show_balance(),
                         'Titularul contului Florin Costea cu IBAN RO01234567890RO, are in cont 5300.0 RON')

    @parameterized.expand([
        (800, 4500),
        (1500, 3800),
        (0.90, 5299.1),
        (0, 5300)
    ])
    def test_debit(self, amount, expected):
        self.Titular_cont.debit(amount)
        self.assertEqual(self.Titular_cont.balance, expected)

    @parameterized.expand([
        (300, 5600),
        (0, 5300),
        (0.90, 5300.9)
    ])
    def test_credit(self, amount, expected):
        self.Titular_cont.credit(amount)
        self.assertEqual(self.Titular_cont.balance, expected)
