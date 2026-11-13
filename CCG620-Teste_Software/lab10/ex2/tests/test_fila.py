import pytest
from fila import Fila


def fila_com(*tipos):
    fila = Fila()
    for t in tipos:
        fila.emitir("normal" if t == "N" else "prioritaria")
    return fila


def chamadas(fila, n):
    return [fila.chamar() for _ in range(n)]


def test_fila_nova_nao_tem_ninguem_aguardando():
    assert Fila().aguardando == 0


def test_primeira_normal_e_n1():
    assert Fila().emitir("normal") == "N1"


def test_normais_sao_numeradas_em_sequencia():
    fila = Fila()
    assert [fila.emitir("normal"), fila.emitir("normal")] == ["N1", "N2"]


def test_numeracao_e_independente_por_tipo():
    fila = Fila()
    tipos = ("normal", "prioritaria", "normal", "prioritaria")
    assert [fila.emitir(t) for t in tipos] == ["N1", "P1", "N2", "P2"]


def test_tipo_invalido_lanca_value_error_e_nao_entra_na_fila():
    fila = Fila()
    with pytest.raises(ValueError):
        fila.emitir("vip")
    assert fila.aguardando == 0


def test_aguardando_conta_emitidas_e_desconta_chamadas():
    fila = fila_com("N", "P", "N")
    assert fila.aguardando == 3
    fila.chamar()
    assert fila.aguardando == 2


def test_chamar_fila_vazia_lanca_index_error():
    with pytest.raises(IndexError):
        Fila().chamar()


def test_normais_saem_na_ordem_de_chegada():
    assert chamadas(fila_com("N", "N"), 2) == ["N1", "N2"]


def test_prioritaria_passa_na_frente():
    assert fila_com("N", "P").chamar() == "P1"


def test_prioritarias_saem_na_ordem_de_chegada():
    assert chamadas(fila_com("P", "P"), 2) == ["P1", "P2"]


def test_depois_de_duas_prioritarias_chama_normal():
    fila = fila_com("N", "P", "P", "P")
    assert chamadas(fila, 4) == ["P1", "P2", "N1", "P3"]


def test_chamar_normal_zera_a_contagem():
    fila = fila_com("N", "N", "P", "P", "P", "P", "P")
    assert chamadas(fila, 7) == ["P1", "P2", "N1", "P3", "P4", "N2", "P5"]


def test_limite_de_duas_nao_vale_sem_normal_esperando():
    assert chamadas(fila_com("P", "P", "P"), 3) == ["P1", "P2", "P3"]


def test_contagem_vale_mesmo_se_a_normal_chegou_depois():
    fila = fila_com("P", "P", "P")
    assert chamadas(fila, 2) == ["P1", "P2"]
    fila.emitir("normal")
    assert fila.chamar() == "N1"
