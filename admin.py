import matplotlib.pyplot as plt
import pandas as pd
from stats import GestoreStats
from config import Config


class AdminDashboard:
    def __init__(self):
        self.gestore = GestoreStats()
        self.df = self.gestore.get_dataframe()

    def mostra_menu(self):
        # ricarica i dati ogni volta prima di accedere nel menu
        self.df = self.gestore.get_dataframe()

        if self.df.empty:
            print(f"\n{Config.GIALLO}Nessun dato storico trovato.{Config.RESET}")
            return

        while True:
            print(f"\n{Config.VERDE}--- PANNELLO ADMIN ---{Config.RESET}")
            print("[1] Classifica Giocatori (Tabella)")
            print("[2] Grafico: Vittorie vs Sconfitte")
            print("[3] Grafico: Distribuzione Tentativi (con Sconfitte)")
            print("[0] Torna al Menu Principale")

            scelta = input("> ")

            if scelta == "1":
                self.leaderboard()
            elif scelta == "2":
                self.grafico_win_loss()
            elif scelta == "3":
                self.grafico_tentativi()
            elif scelta == "0":
                break
            else:
                print("Scelta non valida.")

    def leaderboard(self):
        print("\n--- CLASSIFICA ---")
        # raggruppa i dati in base al nome del giocatore
        stats = self.df.groupby("giocatore").agg(
            Partite=('esito', 'count'),
            Vittorie=('esito', 'sum'),
            Media_Tentativi=('tentativi', 'mean')
        )

        # calcolo delle sconfitte sottraendo alle partite totale le vittorie effettuate
        stats['Sconfitte'] = stats['Partite'] - stats['Vittorie']

        # calcolo della percentuale
        stats['Win_Rate %'] = (stats['Vittorie'] / stats['Partite'] * 100).round(1)
        stats['Media_Tentativi'] = stats['Media_Tentativi'].round(2)

        # ordina in base al numero delle vittorie (decrescente)
        stats = stats.sort_values(by="Vittorie", ascending=False)

        # inserimento della colonna sconfitte
        print(stats[["Partite", "Vittorie", "Sconfitte", "Win_Rate %", "Media_Tentativi"]])
        input("\nPremi INVIO per tornare al menu admin...")

    def grafico_win_loss(self):
        # raggruppamento in base al giocatore e agli esiti (0=Perso, 1=Vinto)
        conteggi = self.df.groupby(['giocatore', 'esito']).size().unstack(fill_value=0)

        # controllo della presenza delle colonne (0 e 1)
        if 0 not in conteggi.columns:
            conteggi[0] = 0
        if 1 not in conteggi.columns:
            conteggi[1] = 0

        # rinominazione delle colonne
        conteggi = conteggi.rename(columns={0: 'Sconfitte', 1: 'Vittorie'})

        plt.figure(figsize=(10, 6))

        # creazione del grafico a barre, le vittorie in verde e le sconfitte in rosso

        conteggi[['Vittorie', 'Sconfitte']].plot(kind='bar', stacked=True, color=['#4CAF50', '#F44336'],
                                                 edgecolor='black')

        plt.title('Bilancio Vittorie vs Sconfitte per Giocatore')
        plt.ylabel('Numero Partite')
        plt.xlabel('Giocatore')
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.legend()
        plt.tight_layout()

        print("Sto aprendo il grafico Vittorie vs Sconfitte...")
        plt.show()

    def grafico_tentativi(self):
        plt.figure(figsize=(10, 6))

        # 1. conto delle vittorie per numero di tentativi (1-6)
        vittorie = self.df[self.df['esito'] == 1]
        conteggi_vittorie = vittorie['tentativi'].value_counts().sort_index()

        # 2. totale delle sconfitte (Esito 0)
        sconfitte_totali = self.df[self.df['esito'] == 0].shape[0]

        # 3. distribuzione dei dati per l'asse X e Y
        # asse X: da 1 a 6 + "X" per le sconfitte
        x_labels = [str(i) for i in range(1, 7)] + ["X (Sconfitte)"]

        # 3. asse Y: conteggio per ogni tentativo (o 0 se manca) + le sconfitte
        y_values = [conteggi_vittorie.get(i, 0) for i in range(1, 7)] + [sconfitte_totali]

        # 4. definizione dei colori: Arancione per le vittorie, Rosso per le sconfitte
        colori = ['orange'] * 6 + ['red']

        # creazione del grafico
        plt.bar(x_labels, y_values, color=colori, edgecolor='black')

        plt.title('Distribuzione Tentativi (Inclusi fallimenti)')
        plt.xlabel('Tentativi impiegati')
        plt.ylabel('Quantità Partite')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        print("Sto aprendo il grafico Distribuzione...")
        plt.show()