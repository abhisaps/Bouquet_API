import pytest

from src.api_backend_code.agent import *
from tests.parameter_test_api_bouquet.parameter_test_agent import test_data_1, test_data_2


def test_view_menu():
    output = view_menu()
    assert output == menu1


@pytest.mark.parametrize("menu1, flower_list", test_data_1)
def test_menu_flower_list(menu1, flower_list):
    output = menu_flower_list(menu1)
    assert output == flower_list


@pytest.mark.parametrize("user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu", test_data_2)
def test_ordering(user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu):
    output = ordering(user_bouquet, menu1)
    assert output == (not_in_menu, stock_bouquet, overflow_menu)
