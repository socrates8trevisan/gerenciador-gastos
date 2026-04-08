from src.gastos import adicionar_gasto, listar_gastos, total_gastos, remover_gasto


def exibir_menu():
    print("\n===== Gerenciador de Gastos =====")
    print("1. Adicionar gasto")
    print("2. Listar gastos")
    print("3. Ver total gasto")
    print("4. Remover gasto")
    print("0. Sair")
    print("=================================")


def executar():
    print("Bem-vindo ao Gerenciador de Gastos Pessoais!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            descricao = input("Descrição: ")
            try:
                valor = float(input("Valor (R$): "))
                categoria = input("Categoria (ex: alimentação, transporte): ")
                gasto = adicionar_gasto(descricao, valor, categoria)
                print(f"\n✅ Gasto '{gasto['descricao']}' adicionado com sucesso!")
            except ValueError as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "2":
            gastos = listar_gastos()
            if not gastos:
                print("\nNenhum gasto registrado ainda.")
            else:
                print("\n--- Seus gastos ---")
                for g in gastos:
                    linha = f"[{g['id']}] {g['descricao']} - R$ {g['valor']:.2f}"
                    print(f"{linha} ({g['categoria']})")

        elif opcao == "3":
            total = total_gastos()
            print(f"\n💰 Total gasto: R$ {total:.2f}")

        elif opcao == "4":
            try:
                gasto_id = int(input("ID do gasto a remover: "))
                remover_gasto(gasto_id)
                print("\n✅ Gasto removido com sucesso!")
            except ValueError as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "0":
            print("\nAté logo!")
            break

        else:
            print("\n⚠️ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar()
