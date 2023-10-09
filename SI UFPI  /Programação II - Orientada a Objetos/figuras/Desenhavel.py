from abc import ABC, abstractmethod

class Desenhavel(ABC):
    @abstractmethod
    def desenha(self):
        pass
    