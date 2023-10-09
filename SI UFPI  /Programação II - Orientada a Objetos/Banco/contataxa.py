class ContaTaxa(Conta):
    def saca(self, valor: float):
        super().saca(valor)
        self._saldo -= 4.00