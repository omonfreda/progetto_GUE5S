class Config:
    # Colori Base (Default: Verde e Giallo)
    VERDE = '\033[92m'
    GIALLO = '\033[93m'
    GRIGIO = '\033[90m'
    RESET = '\033[0m'


    FILE_PAROLE_SEGRETE = "parole_segrete.txt"
    FILE_VOCABOLARIO = "vocabolario.txt"
    FILE_STATS = "history.pkl"


    MAX_TENTATIVI = 6
    LUNGHEZZA_PAROLA = 5

    @classmethod
    def imposta_alto_contrasto(cls, attivo: bool):

      #  se attivo=True, cambia i colori in Magenta (per Verde) e Ciano (per Giallo).

        if attivo:
            # Modalità Alto Contrasto
            cls.VERDE = '\033[95m'  # Magenta (Lettera Giusta)
            cls.GIALLO = '\033[96m'  # Ciano (Lettera Presente)
        else:
            # Modalità Standard
            cls.VERDE = '\033[92m'
            cls.GIALLO = '\033[93m'