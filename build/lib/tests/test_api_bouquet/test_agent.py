import pytest

from src.api_backend_code.agent import *
from src.backend_code.utility.constants import menu1


def test_view_menu():
    output = view_menu()
    assert output == menu1


@pytest.mark.parametrize(
    "menu1, flower_list",
    [
        (menu1, ["Rose", "Lily", "Tulip", "Daisy", "Orchid"]),
    ],
)
def test_menu_flower_list(menu1, flower_list):
    output = menu_flower_list(menu1)
    assert output == flower_list


@pytest.mark.parametrize(
    "user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu",
    [
        ("ABCDE", menu1, [], "ABCDE", []),
        ("SGFGGT", menu1, ["S", "G", "F", "T"], "", []),
        ("ABBBBBDEV", menu1, ["V"], "ABBBBBDE", []),
        ("", menu1, [], "", []),
        ("AAAAAAACXDEAQ", menu1, ["X", "Q"], "AAAAACDE", ["A"]),
        (
            "AAAAAAABBBBBBBBSSSSXXXDDDDDDDDDDQQQZXX",
            menu1,
            ["S", "X", "Q", "Z"],
            "AAAAABBBBBDDDDD",
            ["A", "B", "D"],
        ),
    ],
)
def test_ordering(user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu):
    output = ordering(user_bouquet, menu1)
    assert output == (not_in_menu, stock_bouquet, overflow_menu)
