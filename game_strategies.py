import random
from datetime import date


class StrategiaSelezione:
    def seleziona(self, lista_parole: list) -> str:
        raise NotImplementedError


class SelezioneRandom(StrategiaSelezione):
    def seleziona(self, lista_parole: list) -> str:
        return random.choice(lista_parole)


class SelezioneGiornaliera(StrategiaSelezione):
    def seleziona(self, lista_parole: list) -> str:
        indice = date.today().toordinal() % len(lista_parole)
        return lista_parole[indice]
