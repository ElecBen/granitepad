from barras import barra


def test_barra_al_empezar():
    assert barra(0, 10, ancho=4) == "[----]"


def test_barra_al_acabar():
    assert barra(10, 10, ancho=4) == "[####]"


def test_barra_a_la_mitad():
    assert barra(5, 10, ancho=4) == "[##--]"


def test_barra_no_se_sale_del_ancho():
    assert barra(30, 10, ancho=4) == "[####]"
