class Cabina:
    def __init__(self, codice, letti, ponte, prezzo_base):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo_base = float(prezzo_base)
        self.disponibile = True

    def calcola_prezzo(self):
        return self.prezzo_base

    def __lt__(self, altra):
        return self.calcola_prezzo() < altra.calcola_prezzo()

    def __eq__(self, altra):
        return self.codice == altra.codice

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Occupata"
        return f"{self.codice}: Standard | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"


class CabinaAnimali(Cabina):
    def __init__(self, codice, letti, ponte, prezzo_base, max_animali):
        super().__init__(codice, letti, ponte, prezzo_base)
        self.max_animali = int(max_animali)

    def calcola_prezzo(self):
        return self.prezzo_base * (1 + 0.10 * self.max_animali)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Occupata"
        return f"{self.codice}: Animali | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.calcola_prezzo():.2f}€ - Max animali: {self.max_animali} - {stato}"


class CabinaDeluxe(Cabina):
    def __init__(self, codice, letti, ponte, prezzo_base, stile):
        super().__init__(codice, letti, ponte, prezzo_base)
        self.stile = stile

    def calcola_prezzo(self):
        return self.prezzo_base * 1.20

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Occupata"
        return f"{self.codice}: Deluxe ({self.stile}) | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"


class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina_assegnata = None

    def __str__(self):
        if self.cabina_assegnata:
            return f"{self.codice} - {self.nome} {self.cognome} → Cabina: {self.cabina_assegnata.codice}"
        else:
            return f"{self.codice} - {self.nome} {self.cognome}"

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.cabine = []
        self.passeggeri = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    def set_nome(self, nuovo_nome):
        self.nome = nuovo_nome


    def get_nome(self):
        return self.nome


    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for riga in file:
                    parti = riga.strip().split(",")
                    if not parti or parti[0] == "":
                        continue

                    if parti[0].startswith("CAB"):
                        codice = parti[0]
                        letti = int(parti[1])
                        ponte = int(parti[2])
                        prezzo_base = float(parti[3])

                        if len(parti) == 4:
                            cabina = Cabina(codice, letti, ponte, prezzo_base)
                        elif parti[4].isdigit():
                            cabina = CabinaAnimali(codice, letti, ponte, prezzo_base, int(parti[4]))
                        else:
                            cabina = CabinaDeluxe(codice, letti, ponte, prezzo_base, parti[4])

                        self.cabine.append(cabina)

                    elif parti[0].startswith("P"):
                        codice = parti[0]
                        nome = parti[1]
                        cognome = parti[2]
                        passeggero = Passeggero(codice, nome, cognome)
                        self.passeggeri.append(passeggero)

        except FileNotFoundError:
            raise FileNotFoundError("File non trovato")


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        cabina = None
        for c in self.cabine:
            if c.codice == codice_cabina:
                cabina = c
                break

        passeggero = None
        for p in self.passeggeri:
            if p.codice == codice_passeggero:
                passeggero = p
                break

        if cabina is None:
            raise ValueError("Cabina non trovata.")
        if passeggero is None:
            raise ValueError("Passeggero non trovato.")
        if not cabina.disponibile:
            raise ValueError("Cabina non disponibile.")
        if passeggero.cabina_assegnata is not None:
            raise ValueError("Passeggero già assegnato a una cabina.")

        passeggero.cabina_assegnata = cabina
        cabina.disponibile = False


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        return sorted(self.cabine)


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        if not self.passeggeri:
            print("Nessun passeggero registrato.")
        else:
            for p in self.passeggeri:
                print(p)

