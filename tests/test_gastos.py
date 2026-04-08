import pytest
from src.gastos import adicionar_gasto, listar_gastos, remover_gasto, total_gastos


def setup_function():
    """Limpa os gastos antes de cada teste."""
    import os
    if os.path.exists("gastos.json"):
        os.remove("gastos.json")


def test_adicionar_gasto_valido():
    gasto = adicionar_gasto("Almoço", 25.50, "alimentação")
    assert gasto["descricao"] == "Almoço"
    assert gasto["valor"] == 25.50
    assert gasto["categoria"] == "alimentação"


def test_adicionar_gasto_valor_negativo():
    with pytest.raises(ValueError):
        adicionar_gasto("Erro", -10, "teste")


def test_adicionar_gasto_descricao_vazia():
    with pytest.raises(ValueError):
        adicionar_gasto("", 10, "teste")


def test_total_gastos():
    adicionar_gasto("Almoço", 20.00, "alimentação")
    adicionar_gasto("Ônibus", 5.00, "transporte")
    assert total_gastos() == 25.00


def test_remover_gasto_inexistente():
    with pytest.raises(ValueError):
        remover_gasto(999)