from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    def __init__(self):
        self.on = False

    @abstractmethod
    def power(self):
        pass

# Exemplo de uma subclasse específica (TV)
class ControleRemotoTV(ControleRemoto):
    def power(self):
        self.on = not self.on
        if self.on:
            print("A TV está ligada")
        else:
            print("A TV está desligada")

# Exemplo de uma subclasse específica (Ar Condicionado)
class ControleRemotoArCondicionado(ControleRemoto):
    def power(self):
        self.on = not self.on
        if self.on:
            print("O Ar Condicionado está ligado")
        else:
            print("O Ar Condicionado está desligado")

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    def __init__(self):
        self.on = False

    @abstractmethod
    def power(self):
        pass

# Subclasse ControleTV
class ControleTV(ControleRemoto):
    def __init__(self, volume_max, canal_max):
        super().__init__()
        self.volume = 0
        self.volume_max = volume_max
        self.canal = 1
        self.canal_max = canal_max

    def power(self):
        self.on = not self.on
        if self.on:
            print("A TV está ligada")
        else:
            print("A TV está desligada")

    def aumentar_volume(self):
        if self.on and self.volume < self.volume_max:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")

    def diminuir_volume(self):
        if self.on and self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")

    def aumentar_canal(self):
        if self.on:
            self.canal = (self.canal % self.canal_max) + 1
            print(f"Canal aumentado para {self.canal:02d}")

    def diminuir_canal(self):
        if self.on:
            self.canal = (self.canal - 2) % self.canal_max + 1
            print(f"Canal diminuído para {self.canal:02d}")

# Subclasse ControleAC
class ControleAC(ControleRemoto):
    def __init__(self, temperatura_min, temperatura_max):
        super().__init__()
        self.temperatura = 25  # Definindo uma temperatura padrão
        self.temperatura_min = temperatura_min
        self.temperatura_max = temperatura_max

    def power(self):
        self.on = not self.on
        if self.on:
            print("O Ar Condicionado está ligado")
        else:
            print("O Ar Condicionado está desligado")

    def aumentar_temperatura(self):
        if self.on and self.temperatura < self.temperatura_max:
            self.temperatura += 1
            print(f"Temperatura aumentada para {self.temperatura}°C")

    def diminuir_temperatura(self):
        if self.on and self.temperatura > self.temperatura_min:
            self.temperatura -= 1
            print(f"Temperatura diminuída para {self.temperatura}°C")

## Exemplos de Uso ##
# Uso das classes
controle_tv = ControleRemotoTV()
controle_tv.power()  # Liga a TV
controle_tv.power()  # Desliga a TV

controle_ar = ControleRemotoArCondicionado()
controle_ar.power()  # Liga o Ar Condicionado

# Uso da subclasse ControleTV
controle_tv = ControleTV(volume_max=50, canal_max=50)

controle_tv.power()  # Liga a TV
controle_tv.aumentar_volume()  # Aumenta o volume para 1
controle_tv.aumentar_canal()  # Aumenta o canal para 2
controle_tv.diminuir_canal()  # Diminui o canal para 01 (circular)
controle_tv.diminuir_volume()  # Diminui o volume para 0
controle_tv.power()  # Desliga a TV

# Uso da subclasse ControleTV
controle_tv = ControleTV(volume_max=10, canal_max=10)

controle_tv.power()  # Liga a TV
controle_tv.aumentar_volume()  # Aumenta o volume para 1
controle_tv.aumentar_canal()  # Aumenta o canal para 2
controle_tv.diminuir_canal()  # Diminui o canal para 01 (circular)
controle_tv.diminuir_volume()  # Diminui o volume para 0
controle_tv.power()  # Desliga a TV