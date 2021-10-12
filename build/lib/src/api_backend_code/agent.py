"""
This is agent module which takes backend methods and do modifications and then used by API
"""

from src.api_backend_code.api_order import checking_order, taking_order
from src.backend_code.utility.constants import flower_list, menu1


def view_menu() -> dict:
    # It returns menu which contains all flower name, flower code and flower quantity
    return menu1


def menu_flower_list(menu1: dict) -> list:
    #  it takes menu1 and returns list of flower names
    for value in menu1.values():
        flower_list.append(value[1])
    return flower_list


def adding_flower(f_code: str, f_quantity: str, f_name: str) -> None:
    #  adding flower_code, flower_quantity, flower_name to menu1
    menu1[f_code] = [f_quantity, f_name]


def adding_existing_flower(f_code: str, f_quantity: str) -> None:
    menu1[f_code][0] = int(menu1[f_code][0]) + int(f_quantity)


def deleting_flower(f_code: str) -> None:
    #  deleting flower from menu1
    del menu1[f_code]


def ordering(user_bouquet: str, menu1: dict) -> tuple:
    """
    :param user_bouquet: str, Entered by user
    :param menu1: dict
    :return: checking_object: tuple
                            (
                            Not_in_menu: list,
                            stock_bouquet: str
                            overflow_menu: list
                            )

    this function call two function back to back and output of 2nd function is returned and which is of tuple type
    """

    key, dict_user_bouquet = taking_order(user_bouquet, menu1)
    checking_object = checking_order(key, dict_user_bouquet, menu1)
    return checking_object


def deducting_stock(stock_bouquet: str) -> None:
    """
    :param stock_bouquet: str
    :return: None
    it deducts flower_quantity(f_quantity) after confirmation of order
    """
    key1 = []
    value1 = []
    for i in stock_bouquet:
        if i not in key1:
            key1.append(i)
            value1.append(stock_bouquet.count(i))
    #  zip key1 and value1 to create stock_bouquet_dict: dict and then subtract quantity from menu1: dict

    stock_bouquet_dict = dict(zip(key1, value1))
    for i in key1:
        menu1[i][0] = int(menu1[i][0]) - int(stock_bouquet_dict[i])
