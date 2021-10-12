import pytest as pytest

from src.api_backend_code.api_order import checking_order, taking_order
from tests.parameter_test_api_bouquet.parameter_api_order import test_data_1, test_data_2


@pytest.mark.parametrize("user_bouquet, menu1, key, dict_user_bouquet", test_data_1)
def test_taking_order(user_bouquet, menu1, key, dict_user_bouquet):
    output = taking_order(user_bouquet, menu1)
    assert output == (key, dict_user_bouquet)


@pytest.mark.parametrize("key, dict_user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu", test_data_2)
def test_checking_order(key, dict_user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu):
    output = checking_order(key, dict_user_bouquet, menu1)
    assert output == (not_in_menu, stock_bouquet, overflow_menu)
