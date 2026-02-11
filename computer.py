from repository import RepositoryParole
from game_strategies import SelezioneRandom, SelezioneGiornaliera


class Computer:
    def __init__(self, difficoltà: int = 10):
        self.repo = RepositoryParole()
        self.parole_segrete = self.repo.get_parole_segrete()

        if difficoltà == 20:
            self.strategia = SelezioneGiornaliera()
        else:
            self.strategia = SelezioneRandom()

    def genera_parola(self) -> str:
        return self.strategia.seleziona(self.parole_segrete)

    def valida_input(self, parola: str) -> bool:
        return self.repo.valida(parola)
