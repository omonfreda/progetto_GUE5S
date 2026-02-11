import sys
from computer import Computer
from tavolo_gioco import TavoloGioco
from giocatore import Giocatore
from config import Config
from admin import AdminDashboard

def mostra_legenda():

    print("\n--- LEGENDA COLORI ---")
    print(f"{Config.VERDE}■{Config.RESET} Lettera GIUSTA al posto GIUSTO")
    print(f"{Config.GIALLO}■{Config.RESET} Lettera PRESENTE ma al posto SBAGLIATO")
    print(f"{Config.GRIGIO}■{Config.RESET} Lettera ASSENTE")
    print("----------------------\n")

if __name__ == "__main__":
    print("--- BENVENUTO A WORDLE PYTHON ---")

    # inserimento del nome dell'utentte
    print("Inserisci il tuo nome giocatore:")
    nome_utente = input("> ").strip()
    if not nome_utente:
        nome_utente = "Ospite"

    # modalità Alto Contrasto
    print(f"\nCiao {nome_utente}, vuoi attivare la modalità ALTO CONTRASTO? [S/N]")
    scelta_colore = input("> ").strip().lower()

    if scelta_colore == 's':
        Config.imposta_alto_contrasto(True)
        print("Modalità Alto Contrasto: ATTIVATA (Arancione / Ciano)")
    else:
        Config.imposta_alto_contrasto(False)
        print("Modalità Standard: ATTIVATA (Verde / Giallo)")

    # mostra la legenda in base alla scelta dei colori
    mostra_legenda()

    # admin
    admin = AdminDashboard()

    while True:

        print(f"Menu principale - Giocatore: {Config.VERDE}{nome_utente}{Config.RESET}")
        print("[1] Nuova Partita (Random)")
        print("[2] Sfida del giorno")
        print(f"[3] {Config.GIALLO}Area ADMIN (Statistiche){Config.RESET}")
        print("[0] Esci")

        scelta = input("> ")

        if scelta == "0":
            print("Alla prossima!")
            sys.exit()

        elif scelta == "3":

            admin.mostra_menu()
            continue

        elif scelta in ["1", "2"]:
            difficoltà = 20 if scelta == "2" else 10

            computer = Computer(difficoltà)
            parola_segreta = computer.genera_parola()


            giocatore = Giocatore(nome_utente)
            tavolo = TavoloGioco(parola_segreta)

            # opzione della partita singola
            while True:
                print(tavolo)
                mossa = giocatore.scegli_mossa().upper().strip()

                if mossa == "ESCI":
                    print("Partita interrotta.")
                    break

                if len(mossa) != 5:
                    print("La parola deve avere 5 lettere")
                    continue

                if not computer.valida_input(mossa):
                    print("Parola non valida nel vocabolario")
                    continue

                tavolo.piazza_mossa(mossa)
                stato = tavolo.controlla_stato()

                if stato != 0:
                    print(tavolo)
                    tavolo.dichiara_esito(stato)
                    # salvataggio dei dati
                    giocatore.aggiorna_dati(stato, len(tavolo.tentativi))
                    break
        else:
            print("Opzione non valida.")