from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('Jane', 10)

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'Jane'
        assert self.p1.get_balance() == 10

    def test_deposit(self):
        assert self.p1.deposit(500) == True
        assert self.p1.deposit(-30) == False
        assert self.p1.deposit(0) == False

    def test_withdraw(self):
        assert self.p1.withdraw(500) == False
        assert self.p1.withdraw(0) == False
        assert self.p1.withdraw(2) == False

