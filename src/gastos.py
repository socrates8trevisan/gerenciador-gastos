import json
import os

ARQUIVO = "gastos.json"


def carregar_gastos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_gastos(gastos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)


def adicionar_gasto(descricao, valor, categoria):
    if not descricao or not descricao.strip():
        raise ValueError("Descrição não pode ser vazia.")
    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero.")

    gastos = carregar_gastos()
    gasto = {
        "id": len(gastos) + 1,
        "descricao": descricao.strip(),
        "valor": valor,
        "categoria": categoria.strip(),
    }
    gastos.append(gasto)
    salvar_gastos(gastos)
    return gasto


def listar_gastos():
    return carregar_gastos()


def total_gastos():
    gastos = carregar_gastos()
    return sum(g["valor"] for g in gastos)


def remover_gasto(gasto_id):
    gastos = carregar_gastos()
    novos_gastos = [g for g in gastos if g["id"] != gasto_id]
    if len(novos_gastos) == len(gastos):
        raise ValueError(f"Gasto com ID {gasto_id} não encontrado.")
    salvar_gastos(novos_gastos)
