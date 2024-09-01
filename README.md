# Sistema Bancário

Este projeto foi desenvolvido durante o [Bootcamp NTT DATA - Engenharia de Dados com Python](https://web.dio.me/track/953ab0a9-6d55-4e00-ab7f-5ed855d288ca) na [DIO](https://web.dio.me/).

## Funções

O sistema deve executar 3 funções:
1. [Depositar](#depositar)
2. [Sacar](#sacar)
3. [Ver extrato](#ver-extrato).

### Depositar

* O sistema deve aceitar apenas depósitos com valores positivos.
* O sistema deve registrar o depósitos para serem exibidos no extrato.

### Sacar

* O sistema deve aceitar apenas saques com valores positivos.
* O usuário pode realizar até 3 saques por dia.
* Cada saque é limitado a 500,00.
* Caso não haja saldo suficiente, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
* O sistema deve registrar o saques para serem exibidos no extrato.

### Ver extrato

* O extrato deve listar todos os depósitos e saques realizados na conta.
* Ao fim da listagem, exibir o salto atual da conta, no formato R$ \#\#\#.\#\#
