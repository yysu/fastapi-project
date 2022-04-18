import pytest


def add(num1: int, num2: 2):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2


def divide(num1: int, num2: int):

    return num1 / num2


class InsufficientFunds(Exception):
    pass


class BankAccount():
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds in account")

        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1


@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 1),
    (7, 1, 6),
    (4, 12, -8)
])
def test_subtract(num1, num2, expected):
    assert subtract(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 6),
    (7, 1, 7),
    (4, -12, -48)
])
def test_multiply(num1, num2, expected):
    assert multiply(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 1),
    (7, 1, 7),
    (4, 12, 0)
])
def test_divde(num1, num2, expected):
    assert num1//num2 == expected


def test_bank_set_initial_amount(bank_account):

    assert bank_account.balance == 50


def test_bank_default_amount(zero_bank_account):
    print("testing my bank account")
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):

    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):

    bank_account.deposit(30)
    assert bank_account.balance == 80


def test_collect_interest(bank_account):

    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)

])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
