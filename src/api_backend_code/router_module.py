from flask import render_template, request

from src.api_backend_code.agent import *
from src.backend_code.utility.constants import menu1


def configure_routes(app):
    @app.route("/")
    def welcome():
        return render_template("welcome.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/home")
    def home():
        return render_template("home.html")

    @app.route("/add_flower")
    def add_flower():
        return render_template("add_flower.html")

    @app.route("/add_confirmation", methods=["POST", "GET"])
    def add_confirmation():
        output = request.form.to_dict()
        f_code = output["f_code"].upper()
        f_quantity = output["f_quantity"]
        f_name = output["f_name"].capitalize()

        f_list = menu_flower_list(menu1)

        if f_code.isalpha() and f_quantity.isdigit() and f_name.isalpha():
            if 200 > int(f_quantity) > 0:
                if f_name not in f_list:
                    adding_flower(f_code, f_quantity, f_name)
                    return render_template(
                        "add_flower.html",
                        msg1="{} {} Added...".format(f_quantity, f_name),
                    )
                elif f_code in menu1.keys():
                    if f_name == menu1[f_code][1]:
                        adding_existing_flower(f_code, f_quantity)
                        return render_template(
                            "add_flower.html",
                            msg1="{} flowers added to {}...".format(f_quantity, f_name),
                        )
                    else:
                        return render_template(
                            "add_flower.html", msg="FLower name should be unique..."
                        )
                else:
                    return render_template(
                        "add_flower.html", msg="FLower name should be unique..."
                    )
            else:
                return render_template(
                    "add_flower.html",
                    msg="Quantity must be greater than zero & less than 200",
                )
        else:
            return render_template("add_flower.html", msg="Invalid input...")

    @app.route("/del_flower")
    def del_flower():
        return render_template("del_flower.html")

    @app.route("/del_confirmation", methods=["POST", "GET"])
    def del_confirmation():
        output = request.form.to_dict()
        f_code = output["f_code"].upper()

        if f_code in menu1:
            deleting_flower(f_code)
            return render_template("del_flower.html", f_code=f_code)
        else:
            return render_template(
                "del_flower.html", msg="Please input Correct Flower..."
            )

    @app.route("/display_menu")
    def display_menu():
        output = view_menu()
        return render_template("display_menu.html", output=output)

    @app.route("/user_bouquet_size_confirmation", methods=["POST", "GET"])
    def user_bouquet_size_confirmation():
        bouquet_size = request.form["bouquet_size"]
        output = view_menu()
        if bouquet_size.isdigit() and int(bouquet_size) > 0:
            return render_template(
                "display_menu.html", bouquet_size=bouquet_size, output=output
            )
        else:
            return render_template(
                "display_menu.html",
                msg1="Invalid Input...Select Bouquet size",
                output=output,
            )

    @app.route("/user_order_confirmation", methods=["POST", "GET"])
    def user_order_confirmation():
        output = request.form.to_dict()
        user_bouquet = output["user_bouquet"].upper()
        bouquet_size = output["bouquet_size"]
        output = view_menu()

        o1 = ordering(user_bouquet, menu1)
        not_in_menu = list(o1)[0]
        stock_bouquet = list(o1)[1]
        overflow_menu = list(o1)[2]

        if len(user_bouquet) != 0:
            if user_bouquet.isalpha():
                if len(user_bouquet) < int(bouquet_size):
                    return render_template(
                        "display_menu.html",
                        user_bouquet=user_bouquet,
                        not_in_menu=not_in_menu,
                        stock_bouquet=stock_bouquet,
                        len_stock_bouquet=len(stock_bouquet),
                        overflow_menu=overflow_menu,
                        output=output,
                        bouquet_size=bouquet_size,
                    )
                else:
                    return render_template(
                        "display_menu.html",
                        user_bouquet=user_bouquet,
                        not_in_menu=not_in_menu,
                        stock_bouquet=stock_bouquet,
                        len_stock_bouquet=len(stock_bouquet),
                        overflow_menu=overflow_menu,
                        output=output,
                        bouquet_size=int(bouquet_size),
                        user_bouquet_size=len(user_bouquet),
                    )
            else:
                return render_template(
                    "display_menu.html",
                    output=output,
                    msg2="Invalid Input...",
                    user_bouquet=user_bouquet,
                    bouquet_size=bouquet_size,
                )
        else:
            return render_template(
                "display_menu.html",
                output=output,
                msg2="User Bouquet can't be empty",
                user_bouquet=user_bouquet,
                bouquet_size=bouquet_size,
            )

    @app.route("/receipt", methods=["POST", "GET"])
    def receipt():
        output = request.form.to_dict()
        stock_bouquet = output["stock_bouquet"]
        deducting_stock(stock_bouquet)
        return render_template(
            "receipt.html",
            msg3="Your Order has been Placed Successfully...",
            stock_bouquet=stock_bouquet,
        )
