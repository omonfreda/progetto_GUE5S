from config import Config

class TavoloGioco:
    def __init__(self, parola_segreta: str):
        self.parola_segreta = parola_segreta.upper()
        self.tentativi = []
        self.risolto = False

    def piazza_mossa(self, parola: str):
        if self.risolto or len(self.tentativi) >= Config.MAX_TENTATIVI:
            return

        self.tentativi.append(parola)

        if parola == self.parola_segreta:
            self.risolto = True

    def __str__(self):
        out = f"\n--- TAVOLO ({len(self.tentativi)}/{Config.MAX_TENTATIVI}) ---\n"

        for tentativo in self.tentativi:
            # creazione di una copia mutable della parola segreta per gestire le lettere doppie
            segreta_temp = list(self.parola_segreta)
            colori = [Config.GRIGIO] * 5

            # FASE 1: individuazione delle lettere VERDI (o Arancione se in Alto Contrasto)

            for i in range(5):
                if tentativo[i] == self.parola_segreta[i]:
                    colori[i] = Config.VERDE
                    segreta_temp[i] = None  # Rimuoviamo la lettera per non contarla di nuovo

            # FASE 2: individuazione delle lettere GIALLE (o Ciano se in Alto Contrasto)

            for i in range(5):

                if colori[i] == Config.GRIGIO and tentativo[i] in segreta_temp:
                    colori[i] = Config.GIALLO
                    # rimozzione della prima occorrenza trovata in segreta_temp
                    segreta_temp[segreta_temp.index(tentativo[i])] = None


            for i in range(5):
                out += f"{colori[i]}[{tentativo[i]}]{Config.RESET} "
            out += "\n"


        for _ in range(Config.MAX_TENTATIVI - len(self.tentativi)):
            out += "[_] " * 5 + "\n"

        return out

    def controlla_stato(self):

        # Ritorna:
        # 1  -> Vittoria
        # -1 -> Sconfitta (Tentativi esauriti)
        # 0  -> Partita in corso

        if self.risolto:
            return 1
        if len(self.tentativi) >= Config.MAX_TENTATIVI:
            return -1
        return 0

    def dichiara_esito(self, stato):
        if stato == 1:
            print(f"{Config.VERDE}HAI VINTO!{Config.RESET}")
        else:
            print(f"{Config.GRIGIO}PERSO! La parola era {self.parola_segreta}{Config.RESET}")