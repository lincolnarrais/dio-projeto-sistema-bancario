class SistemaBancario:
    def __init__(self) -> None:
        self.saldo = 0.0
        self.saques = 0
        self._extrato = []

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            self._extrato.append(f"Depósito realizado no valor de R$ {valor:.2f}")

    def sacar(self, valor: float) -> None:
        if 500 >= valor > 0 and valor <= self.saldo and self.saques < 3:
            self.saldo -= valor
            self._extrato.append(f"Saque realizado no valor de R$ {valor:.2f}")
            self.saques += 1

    def ver_extrato(self) -> str:
        result = "\n".join(self._extrato)
        result += f"\n{self._ver_saldo()}"
        return result

    def _ver_saldo(self) -> str:
        return f"Saldo atual: R$ {self.saldo:.2f}"
