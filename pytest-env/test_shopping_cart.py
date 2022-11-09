import pytest
from shopping_cart import ShoppingCart
from item_db import ItemDatabase
from unittest.mock import Mock


@pytest.fixture
def cart():
    return ShoppingCart()

def test_add(cart):
    size = cart.size()
    cart.add("apple")
    assert cart.size() == size + 1

def test_if_item_inside(cart):
    cart.add("grape")
    assert "grape" in cart.get_items()

def test_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    item_db = ItemDatabase()
    item_db.get = Mock(return_value=1.0)
    assert cart.get_total_price(price_map) == 3.0

@pytest.mark.parametrized("item, size", [("juice", 1), ("milk", 2), ("soap", 3)])
def test_size(item, size):
    cart = ShoppingCart()
    cart.add(item)
    assert cart.size() == size

def test_max_cart_size(cart):
    for _ in range(5):
        cart.add("juice")

    with pytest.raises(OverflowError):
        cart.add("some item")
        cart.add("some item")








