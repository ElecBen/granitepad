import pytest

from barras import barra, girador, linea, porcentaje, restante


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


def test_linea_junta_las_tres_piezas():
    assert linea("bajar", 5, 10, ancho=4) == "bajar [##--]  50%"


def test_linea_reserva_sitio_para_el_cien():
    assert linea("x", 10, 10, ancho=2).endswith("100%")


def test_restante_a_la_mitad():
    assert restante(5, 10, 2.0) == 2.0


def test_restante_sin_nada_hecho():
    assert restante(0, 10, 2.0) is None


def test_restante_al_acabar():
    assert restante(10, 10, 2.0) == 0.0


def test_girador_empieza_por_el_primero():
    assert girador(0) == "."


def test_girador_da_la_vuelta():
    assert girador(4) == girador(0)


def test_girador_acepta_otros_marcos():
    assert girador(3, marcos="ab") == "b"
