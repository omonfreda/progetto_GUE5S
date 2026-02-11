from stats import GestoreStats

class Giocatore:
    def __init__(self, nome):
        self.nome = nome
        self.stats = GestoreStats()

    def scegli_mossa(self) -> str:

        return input(f"{self.nome}, inserisci parola: ")

    def aggiorna_dati(self, stato, tentativi):
        # passaggio del nome al gestore stats
        self.stats.salva_partita(self.nome, stato == 1, tentativi)

    def mostra_stats_personali(self):

        df = self.stats.get_dataframe()
        mie_stats = df[df['giocatore'] == self.nome]
        if not mie_stats.empty:
            media = mie_stats['tentativi'].mean()
            print(f"La tua media tentativi è: {media:.2f}")