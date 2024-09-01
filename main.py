from sistema_bancario import SistemaBancario


def main():
    sistema = SistemaBancario()

    OPCOES = {
        "d": "Depositar",
        "s": "Sacar",
        "e": "Ver extrato",
        "q": "Sair",
    }

    while True:
        print("\nMENU PRINCIPAL")
        key = input(
            "\n".join([f"[{k}] -> {v}" for k, v in OPCOES.items()])
            + "\nDigite a opção desejada: "
        ).lower()

        if key in OPCOES.keys():
            print(f"\n{OPCOES[key].upper()}")

        if key == "q":
            print("Programa encerrado.")
            break

        elif key == "d":
            valor = float(input("Digite o valor a ser depositado: R$ "))
            if valor <= 0:
                print("Erro no depósito. O valor deve ser positivo.")
                continue
            sistema.depositar(valor)
            print("Depósito realizado com sucesso.")

        elif key == "s":
            if sistema.saques >= 3:
                print("Não é possível sacar no momento. Limite diário de 3 saques atingido.")
                continue
            valor = float(input("Digite o valor a ser sacado: R$ "))
            if valor > 500:
                print("Erro no saque. Valor máximo para saque: R$ 500.00.")
                continue
            if valor <= 0:
                print("Erro no saque. Valor muito baixo.")
                continue
            if valor > sistema.saldo:
                print("Erro no saque. Saldo insuficiente.")
                continue
            sistema.sacar(valor)
            print("Saque realizado com sucesso.")

        elif key == "e":
            print(sistema.ver_extrato())

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
