# Gerenciador de Gastos Pessoais

![CI](https://github.com/socrates8trevisan/gerenciador-gastos/actions/workflows/ci.yml/badge.svg)

## Descrição do Problema
Muitas pessoas, especialmente estudantes, perdem o controle dos gastos mensais
e não sabem para onde o dinheiro vai. Isso dificulta o planejamento financeiro
e causa endividamento desnecessário.

## Solução
Aplicação CLI simples para registrar, listar e controlar gastos pessoais
de forma rápida e organizada.

## Público-alvo
Estudantes e jovens adultos que querem controlar melhor suas finanças.

## Funcionalidades
- Adicionar gasto com descrição, valor e categoria
- Listar todos os gastos registrados
- Ver o total gasto
- Remover um gasto pelo ID

## Tecnologias Utilizadas
- Python 3.11
- pytest (testes automatizados)
- ruff (linting)
- GitHub Actions (CI)

## Instalação
```bash
git clone https://github.com/socrates8trevisan/gerenciador-gastos.git
cd gerenciador-gastos
pip install -r requirements.txt
```

## Execução
```bash
python -m src.app
```

## Rodando os Testes
```bash
python -m pytest tests/ -v
```

## Rodando o Lint
```bash
python -m ruff check src/
```

## Versão
1.0.0

## Autor
socrates8trevisan

## Repositório
https://github.com/socrates8trevisan/gerenciador-gastos
