import os
import pandas as pd
import numpy as np
from config import Config


class GestoreStats:
    def __init__(self):
        # definizione delle colonne, compreso "giocatore"
        self.cols = ["giocatore", "esito", "tentativi"]

        if os.path.exists(Config.FILE_STATS):
            self.df = pd.read_pickle(Config.FILE_STATS)
            # se nel file precedente non è stata inserita la colonna 'giocatore, per compatibilità viene aggiunta
            if "giocatore" not in self.df.columns:
                self.df["giocatore"] = "Anonimo"
        else:
            self.df = pd.DataFrame(columns=self.cols)

    def salva_partita(self, nome_giocatore, vittoria, tentativi):
        nuova = pd.DataFrame([{
            "giocatore": nome_giocatore,
            "esito": 1 if vittoria else 0,
            "tentativi": tentativi
        }])

        self.df = pd.concat([self.df, nuova], ignore_index=True)
        self.df.to_pickle(Config.FILE_STATS)

    def get_dataframe(self):
        return self.df