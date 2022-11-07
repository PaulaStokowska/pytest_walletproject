#test_wallet_parametrized

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.mark.parametrize("spent, earned, expected", [
    (50, 100, 50),
    (4, 16, 12)
])

def test_transactions(spent, earned, expected):
    wallet = Wallet()
    wallet.add_cash(earned)
    wallet.spend_cash(spent)
    assert wallet.balance == expected
