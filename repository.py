import os
import sys
from config import Config


class RepositoryParole:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._carica_dati()
        return cls._instance

    def _leggi_file(self, filename):
        parole = set()

        if not os.path.exists(filename):
            print(f"ERRORE CRITICO: File mancante -> {filename}")
            sys.exit(1)

        with open(filename, "r", encoding="utf-8") as f:
            for riga in f:
                parola = riga.strip().upper()
                if len(parola) == Config.LUNGHEZZA_PAROLA and parola.isalpha():
                    parole.add(parola)

        return parole

    def _carica_dati(self):
        self.parole_segrete = self._leggi_file(Config.FILE_PAROLE_SEGRETE)
        self.vocabolario = self._leggi_file(Config.FILE_VOCABOLARIO)

        # controllo della validazione della parole
        self.vocabolario |= self.parole_segrete

        if not self.parole_segrete:
            print("ERRORE: Nessuna parola segreta valida.")
            sys.exit(1)

    def get_parole_segrete(self) -> list:
        return list(self.parole_segrete)

    def valida(self, parola: str) -> bool:
        return parola.strip().upper() in self.vocabolario
