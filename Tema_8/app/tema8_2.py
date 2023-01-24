from dataclasses import dataclass


@dataclass
class Employee:
    nume: str
    prenume: str
    salary: float

    def descriere(self):
        return f'Numele: {self.nume}, Prenumele: {self.prenume}, Salariul: {self.salary}'

    def nume_complet(self):
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return self.salary

    def salariu_anual(self):
        return self.salary * 12

    def revizuire_salariu(self, percentage):
        recomputed_salary = self.salary * (percentage * 0.01)
        self.salary = self.salary + int(recomputed_salary)


@dataclass
class ContBancar:
    iban: str
    Titular_cont: str
    balance: float

    def show_balance(self):
        return f'Titularul contului {self.Titular_cont} cu IBAN {self.iban}, are in cont {self.balance} RON'

    def debit(self, amount):
        if amount > self.balance:
            print('Insufficient funds!')
        else:
            self.balance -= amount
            print(f"The amount of: {amount} RON, was debited from the account")

    def credit(self, amount):
        self.balance = self.balance + amount
