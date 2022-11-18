import pytest
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('Parker')
        self.a2 = Account('Ashley')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init_(self):
        assert self.a1.get_name() == 'Parker'
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == 'Ashley'
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-1) == False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(1) == True
        assert self.a1.get_balance() == 1
        assert self.a1.deposit(0) == False
        assert self.a1.get_balance() == 1
        assert self.a1.deposit(1.5) == True
        assert self.a1.get_balance() == pytest.approx(2.5, abs=0.001)

        assert self.a2.deposit(-1) == False
        assert self.a2.get_balance() == 0
        assert self.a2.deposit(1) == True
        assert self.a2.get_balance() == 1
        assert self.a2.deposit(0) == False
        assert self.a2.get_balance() == 1
        assert self.a2.deposit(1.5) == True
        assert self.a2.get_balance() == pytest.approx(2.5, abs=0.001)

    def test_withdraw(self):
        self.a1.deposit(2)
        assert self.a1.withdraw(-1) == False
        assert self.a1.get_balance() == 2
        assert self.a1.withdraw(0) == False
        assert self.a1.get_balance() == 2
        assert self.a1.withdraw(1) == True
        assert self.a1.get_balance() == 1

        self.a1.deposit(5)
        assert self.a1.withdraw(1.5) == True
        assert self.a1.get_balance() == pytest.approx(4.5, abs=0.001)



        self.a2.deposit(2)
        assert self.a2.withdraw(-1) == False
        assert self.a2.get_balance() == 2
        assert self.a2.withdraw(0) == False
        assert self.a2.get_balance() == 2
        assert self.a2.withdraw(1) == True
        assert self.a2.get_balance() == 1

        self.a2.deposit(5)
        assert self.a2.withdraw(1.5) == True
        assert self.a2.get_balance() == pytest.approx(4.5, abs=0.001)
