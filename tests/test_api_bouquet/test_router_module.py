import requests
from flask import Flask
from src.api_backend_code.router_module import configure_routes

app = Flask(__name__, template_folder="./templates")
configure_routes(app)
client = app.test_client()
base_url = "http://127.0.0.1:5000"


def test_welcome():
    url = base_url + "/"
    response = requests.get(url)
    assert response.status_code == 200


def test_about():
    url = base_url + "/about"
    response = requests.get(url)
    assert response.status_code == 200


def test_home():
    url = base_url + "/home"
    response = requests.get(url)
    assert response.status_code == 200


def test_add_flower():
    url = base_url + "/add_flower"
    response = requests.get(url)
    assert response.status_code == 200


def test_add_confirmation():
    url = base_url + "/add_confirmation"
    mock_request_data = {"f_code": "z", "f_quantity": "5", "f_name": "zzz"}
    response = requests.get(url, data=mock_request_data)
    assert response.status_code == 200


def test_del_flower():
    url = base_url + "/del_flower"
    response = requests.get(url)
    assert response.status_code == 200


def test_del_confirmation():
    url = base_url + "/del_confirmation"
    response = requests.post(url, data={"f_code": "z"})
    assert response.status_code == 200


def test_display_menu():
    url = base_url + "/display_menu"
    response = requests.get(url)
    assert response.status_code == 200


def test_user_bouquet_size_confirmation():
    url = base_url + "/user_bouquet_size_confirmation"
    mock_request_data = {"bouquet_size": "5"}
    response = requests.post(url, data=mock_request_data)
    assert response.status_code == 200


def test_user_order_confirmation():
    url = base_url + "/user_order_confirmation"
    mock_request_data = {"user_bouquet": "ABCDE", "bouquet_size": "5"}
    response = requests.post(url, data=mock_request_data)
    assert response.status_code == 200


def test_receipt():
    url = base_url + "/receipt"
    mock_request_data = {"stock_bouquet": "ABCDE"}
    response = requests.get(url, data=mock_request_data)
    assert response.status_code == 200
