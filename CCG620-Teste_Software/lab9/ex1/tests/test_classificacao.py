import pytest

from classificacao import classificar_aluno


# ---------------------------------------------------------------------------
# Suíte inicial (2 testes do enunciado)
# ---------------------------------------------------------------------------
def test_aprovado():
    assert classificar_aluno(8.0, 80) == "Aprovado"


def test_reprovado():
    assert classificar_aluno(3.0, 90) == "Reprovado"


# ---------------------------------------------------------------------------
# Acrescentados no item (c): matam os mutantes vivos
# ---------------------------------------------------------------------------

# --- validação da média: fronteiras 0 e 10 -------------------------------
@pytest.mark.parametrize("media", [-0.1, -1, 10.1, 11])
def test_media_fora_do_intervalo_levanta_erro(media):
    # -0.1 / 10.1 ficam colados na fronteira (matam "<= 0", ">= 10", "> 11");
    # -1 e 11 garantem que o "or" não virou "and".
    with pytest.raises(ValueError) as exc:
        classificar_aluno(media, 80)
    # comparação exata: mata None, "XX...XX", minúsculas e maiúsculas
    assert str(exc.value) == "Media invalida"


def test_media_zero_e_valida():
    # mata "media <= 0" e "media < 1"
    assert classificar_aluno(0, 100) == "Reprovado"


def test_media_dez_e_valida():
    # mata "media >= 10"
    assert classificar_aluno(10, 100) == "Aprovado"


# --- validação da presença: fronteiras 0 e 100 ---------------------------
@pytest.mark.parametrize("presenca", [-1, 101, 150])
def test_presenca_fora_do_intervalo_levanta_erro(presenca):
    # -1 e 101 matam "<= 0", "< 1", ">= 100", "> 101"; -1 e 150 matam "and"
    with pytest.raises(ValueError) as exc:
        classificar_aluno(8.0, presenca)
    assert str(exc.value) == "Presenca invalida"


def test_presenca_zero_e_valida():
    # mata "presenca <= 0" e "presenca < 1"
    assert classificar_aluno(8.0, 0) == "Reprovado por falta"


def test_presenca_cem_e_valida():
    # mata "presenca >= 100"
    assert classificar_aluno(8.0, 100) == "Aprovado"


# --- limite de presença: 75 -----------------------------------------------
def test_presenca_74_reprova_por_falta():
    assert classificar_aluno(10, 74) == "Reprovado por falta"


def test_presenca_75_nao_reprova_por_falta():
    # mata "presenca <= 75" e "presenca < 76"
    assert classificar_aluno(8.0, 75) == "Aprovado"


# --- limites de média: 7.0 e 5.0 -------------------------------------------
def test_media_7_e_aprovado():
    # mata "media > 7.0" e "media >= 8.0"
    assert classificar_aluno(7.0, 80) == "Aprovado"


def test_media_abaixo_de_7_e_recuperacao():
    assert classificar_aluno(6.9, 80) == "Recuperacao"


def test_media_5_e_recuperacao():
    # mata "media > 5.0" e "media >= 6.0" (e as strings de "Recuperacao")
    assert classificar_aluno(5.0, 80) == "Recuperacao"


def test_media_abaixo_de_5_e_reprovado():
    assert classificar_aluno(4.9, 80) == "Reprovado"
