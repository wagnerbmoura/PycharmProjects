from abc import ABC, abstractmethod

class RepositorioContas(ABC):
    @abstractmethod
    def cadastra_conta(self, conta):
        pass

    @abstractmethod
    def procura_conta(self, numero):
        pass