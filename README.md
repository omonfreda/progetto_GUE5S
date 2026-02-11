
Progetto_GUE5S
===============
Il software GUE5S permette di indovinare una parola segreta, evidenziando le lettere corrette in verde, quelle presenti ma nella posizione sbagliata in giallo e quelle assenti in grigio. Registra le statistiche di gioco in modo persistente e include un pannello amministratore con classifiche e grafici dei giocatori.

# Features

* Gioco interattivo direttamente nel terminale
    * Evidenzia le lettere corrette, presenti o assenti
    * Feedback immediato per ciascun tentativo
* Statistiche persistenti
    * Salvataggio dei punteggi e degli esiti delle partite
    * Consultazione delle classifiche
    * Percentuali di vittoria e grafici delle performance
* Pannello amministratore dedicato
    * Visualizzazione completa delle prestazioni dei giocatori nel tempo
      

# Install

Per installare, eseguire nel terminale:

    $ git clone https://github.com/omonfreda/guessword.git
    $ cd GUE5S
    $ python -m venv venv
    $ venv\Scripts\activate   
    $ pip install -r requirements.txt
    

# Start Game

Una volta attivato l'ambiente e installato le dipendenze, puoi avviare il gioco con il seguente comando:

    $ python main.py


# Example

--- BENVENUTO A GUE5S ---

Inserisci il tuo nome giocatore:
> Pippo

Ciao Pippo, vuoi attivare la modalità ALTO CONTRASTO? [S/N]
> N

Tentativo 1/6:

[A][E][R][E][O]  (Input utente)

🟨 ⬛ 🟩 ⬛ 🟩 

(Feedback: Giallo, Grigio, Verde...)

...

Tentativo 4/6:

[M][A][R][C][O]

🟩 🟩 🟩 🟩 🟩  

(Vittoria!)

Complimenti Pippo! Hai indovinato la parola in 4 tentativi.


# Terminology

* Lettera **corretta**: lettera presente nella parola e nella posizione giusta (verde/magenta)
* Lettera **presente**: lettera presente ma nella posizione sbagliata (giallo/ciano)
* Lettera **assente**: lettera non presente nella parola (grigio)


# Setup

* Lunghezza parola: 5 lettere
* Tentativi massimi: 6
* Salvataggio dei dati: persistente tramite file


# Performance

* Monitoraggio delle statistiche dei giocatori
* Percentuale di vittoria calcolata automaticamente
* Classifiche aggiornate in tempo reale

# Credits

Ornella Monfreda

Esame di Programmazione Object Oriented

CdL Ingegneria Informatica (L8)

AA 2025/26



