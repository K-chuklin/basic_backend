from utils import utils
from .test_get_data import *


def test_get_data():
    assert utils.get_data() == data


def test_get_filtered_data():
    assert utils.get_filtered_data(utils.get_data()) == filtered_data


def test_get_sorted_data():
    assert utils.get_sorted_data(utils.get_filtered_data(utils.get_data())) == sorted_data


def test_get_formatted():
    assert utils.get_formatted(data[0]['date']) == '26.08.2019'


def test_hide_card_info():
    assert utils.hide_card_info(data[0]['from']) == 'Maestro 1596 83** **** 5199'
    assert utils.hide_card_info(data[5]['from']) == 'Счет **4719'
    assert utils.hide_card_info(card_data[0]['from']) == 'data error'
