import pytest

from barras import barra, porcentaje


def test_barra_al_empezar():
    assert barra(0, 10, ancho=4) == "[----]"


def test_barra_al_acabar():
    assert barra(10, 10, ancho=4) == "[####]"


def test_barra_a_la_mitad():
    assert barra(5, 10, ancho=4) == "[##--]"


def test_barra_no_se_sale_del_ancho():
    assert barra(30, 10, ancho=4) == "[####]"


def test_barra_rechaza_un_total_vacio():
    with pytest.raises(ValueError):
        barra(1, 0)


def test_porcentaje_redondea():
    assert porcentaje(1, 3) == "33%"


def test_porcentaje_con_decimales():
    assert porcentaje(1, 3, 1) == "33.3%"
