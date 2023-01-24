import pytest
from Teme_ITF.Tema_8.app.tema8_2 import Employee, ContBancar


class TestEmployee:
    def setup_method(self):
        self.employee = Employee('Cristescu', 'Andrei', 3500)

    def test_descriere(self):
        assert self.employee.descriere() == 'Numele: Cristescu, Prenumele: Andrei, Salariul: 3500'

    def test_nume_complet(self):
        assert self.employee.nume_complet() == 'Cristescu Andrei'

    def test_salariu_lunar(self):
        assert self.employee.salariu_lunar() == 3500

    def test_salariu_anual(self):
        assert self.employee.salariu_anual() == 42000

    @pytest.mark.parametrize('percentage, expected', [
        (100, 7000),
        (0, 3500),
        (-50, 1750)
    ])
    def test_revizuire_salariu(self, percentage, expected):
        self.employee.revizuire_salariu(percentage)
        assert self.employee.salary == expected


class TestBankAccount:
    def setup_method(self):
        self.Titular_cont = ContBancar('RO01234567890RO', 'Florin Costea', 5300.00)

    def test_show_balance(self):
        assert self.Titular_cont.show_balance() == 'Titularul contului Florin Costea cu IBAN RO01234567890RO, are in cont 5300.0 RON'

    @pytest.mark.parametrize('amount, expected', [
        (300, 5000),
        (1300, 4000),
        (0.50, 5299.5),
        (0, 5300)
    ])
    def test_debit(self, amount, expected):
        self.Titular_cont.debit(amount)
        assert self.Titular_cont.balance == expected

    @pytest.mark.parametrize('amount, expected', [
        (700, 6000),
        (0, 5300),
        (0.50, 5300.50)
    ])
    def test_credit(self, amount, expected):
        self.Titular_cont.credit(amount)
        assert self.Titular_cont.balance == expected
