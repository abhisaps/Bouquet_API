"""
this module performs:
        1. takes order from user
        2. checks order taken from user to our stock menu
"""


def taking_order(user_bouquet: str, menu1: dict) -> tuple:
    """
    :param user_bouquet: str
    :param menu1: dict
    :return: key: list
             dict_user_bouquet: dict, convert that user_bouquet to dict

                e.g- user_bouquet = "AABCCDEEE"
                     dict_user_bouquet = {'A': 2, 'B':1, 'C': 2, 'D': 1, 'E': 3}
                     key = ['A', 'B', 'C', 'D', 'E']
    """
    key = []
    value = []
    for i in user_bouquet:
        if i not in key:
            key.append(i)
            value.append(user_bouquet.count(i))
    dict_user_bouquet = dict(zip(key, value))
    checking_order(key, dict_user_bouquet, menu1)
    return key, dict_user_bouquet


def checking_order(key: list, dict_user_bouquet: dict, menu1: dict) -> tuple:
    """
    :param key: list
    :param dict_user_bouquet: dict
    :param menu1: dict
    :return: not_in_menu: list
             stock_bouquet: str
             overflow_menu: list

    1st it checks the each elements key whether it present in menu.keys() or not,
        if not, append to not_in_menu list
        if yes,
                then it checks the quantity = values = dict_user_bouquet[f_code] of dict_user_bouquet to our stock menu1[f_code][0]
                if dict_user_bouquet[f_code] is less than or equal to stock_menu
                    then add f_code * f_quantity in stock_bouquet
                if dict_user_bouquet[f_code] exceed to stock_menu
                    then add f_code * menu's quantity
    """
    stock_bouquet = ""
    not_in_menu1 = []
    overflow_menu = []
    for i in key:
        if i not in menu1.keys():
            not_in_menu1.append(i)
        else:
            if int(dict_user_bouquet[i]) <= int(menu1[i][0]):
                stock_bouquet = stock_bouquet + (i * dict_user_bouquet[i])
            else:
                overflow_menu.append(i)
                if menu1[i][0] != 0:
                    stock_bouquet = stock_bouquet + (i * menu1[i][0])

    return not_in_menu1, stock_bouquet, overflow_menu
