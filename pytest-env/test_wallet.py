#test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Returns an empty wallet'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a wallet with 400'''
    return Wallet(400)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 400

def test_add_cash(wallet):
    wallet.add_cash(300)
    assert wallet.balance == 700

def test_spend_cash(wallet):
    wallet.spend_cash(200)
    assert wallet.balance == 200

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)