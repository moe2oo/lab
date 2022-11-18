import pytest
from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('Jane')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'Jane'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(500) is True
        assert self.p1.get_balance() == 500
        assert self.p1.deposit(-30) is False
        assert self.p1.get_balance() == 500
        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == 500

        assert self.p1.deposit(3.5) is True
        assert self.p1.get_balance() == pytest.approx(503.5, abs = 0.001)


    def test_withdraw(self):

        assert self.p1.withdraw(600) is False
        assert self.p1.get_balance() == 0
        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == 0
        assert self.p1.withdraw(-2) is False
        assert self.p1.get_balance() == 0

        self.p1.deposit(30)
        assert self.p1.withdraw(2.5) is True
        assert self.p1.get_balance() == pytest.approx(27.5, abs = 0.001)
        assert self.p1.withdraw(1) is True
        assert self.p1.get_balance() == pytest.approx(26.5, abs = 0.001)

